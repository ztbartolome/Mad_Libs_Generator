from random import random
from string import punctuation
import nltk
from nltk import DefaultTagger, BigramTagger, TrigramTagger, UnigramTagger
from nltk.corpus import brown
from pickle import dump, load

# put the tags of replaceable words here
tags_to_replace = {'CD', 'JJ', 'JJR', 'JJS', 'NN', 'NNS', 'NNP', 'NNPS', 'RB', 'RBR', 'RBR', 'UH', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'}
tag_examples = dict()
tag_names = dict()
verb_tags = {'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'}
tags_to_replace.update({tag + '-T' for tag in verb_tags})
tags_to_replace.update({tag + '-IT' for tag in verb_tags})


def train():
    """Trains the tagger on the Brown corpus"""
    brown_tagged_sents = brown.tagged_sents()
    tagged_sents = []
    suffixes = {'+', '$', '-'}
    for sent_index in range(len(brown_tagged_sents)):
        tagged_sents.append([])
        sent = brown_tagged_sents[sent_index]
        for word_index in range(len(sent)):
            word, tag = sent[word_index]
            if tag not in punctuation:
                for symbol in suffixes:
                    if symbol in tag:
                        tag = tag[:tag.find(symbol)]
            tagged_sents[sent_index].append((word, tag))
    t0 = DefaultTagger('XX')  # last resort, tag everything left as NN
    t1 = UnigramTagger(tagged_sents, backoff=t0)  # backoff to default tagger if necessary
    t2 = BigramTagger(tagged_sents, backoff=t1)  # backoff to unigram tagger if necessary
    t3 = TrigramTagger(tagged_sents, backoff=t2)  # backoff to trigram tagger if necessary
    tagger_output = open('pos_tagger_brown.pkl', 'wb')
    dump(t3, tagger_output, -1)
    tagger_output.close()
    return t3


def load_tagger():
    try:
        tagger_input = open('pos_tagger_brown.pkl', 'rb')
    except FileNotFoundError:
        return train()
    tagger = load(tagger_input)
    tagger_input.close()
    return tagger


class MadLibs(object):
    def __init__(self):
        self.raw = None    # may be unnecessary idk
        self.tagged_tokens = None
        self.word_replacements = {}  # will be a dictionary of the form {(word, tag): replacement}
        self.replaced_tokens = []

    def tag_passage(self):
        """Tag the tokens in the passage"""
        tagger = load_tagger()
        self.tagged_tokens = tagger.tag(self.tokenize_with_newline())
        self.determine_transitive()

    def tokenize_with_newline(self):
        """Split raw text into tokens which are either words, punctuation, or \n"""
        lines = self.raw.split('\n')
        tokens = []
        for line in lines:
            tokens += nltk.word_tokenize(line) + ['\n']
        return tokens

    def process_passage(self, raw_text):
        """
        Takes a string with the raw text of a passage and removes random nouns/verbs/adjectives/adverbs/interjections,
        storing each removed word and its tag
        """
        self.raw = raw_text
        self.tag_passage()
        for (token, tag) in self.tagged_tokens:
            if tag in tags_to_replace and random() > .5:
                self.word_replacements[(token, tag)] = None

    def replace(self, replacements):
        """Accepts a list of words entered by the user and replaces the corresponding words in the passage"""
        i = 0
        for key in self.word_replacements:
            self.word_replacements[key] = replacements[i]
            i += 1
        for orig, tag in self.tagged_tokens:
            if (orig, tag) in self.word_replacements.keys():
                self.replaced_tokens.append('*' + self.word_replacements[(orig, tag)] + '*')
            else:
                self.replaced_tokens.append(orig)

    def to_string(self):
        """Converts replaced_tokens to a string that can be printed for the user"""
        if len(self.replaced_tokens) == 0:
            return
        output = self.replaced_tokens[0]
        for token in self.replaced_tokens[1:]:
            if token not in punctuation:
                output += ' '
            output += token
        return output

    def determine_transitive(self):
        """Adds '-T' or '-IT' to the end of each verb tag depending on whether it is transitive or intransitive"""
        i = 0
        verb_index = -1
        while i < len(self.tagged_tokens):
            current_tag = self.tagged_tokens[i][1]
            if current_tag[:2] == 'VB':
                if verb_index > -1:
                    # mark the previous verb as intransitive
                    self.append_to_tag(verb_index, '-IT')
                verb_index = i
            elif current_tag[:2] == 'NN' and verb_index > -1:
                # mark the most recent verb as transitive
                self.append_to_tag(verb_index, '-T')
                verb_index = -1
            elif (current_tag == 'IN' or current_tag == 'CC' or current_tag in punctuation)and verb_index > -1:
                # mark the most recent verb as intransitive
                self.append_to_tag(verb_index, '-IT')
                verb_index = -1
            i += 1

    def append_to_tag(self, index, end):
        """Appends some string to the end of the tag at the given index of self.tagged_tokens"""
        self.tagged_tokens[index] = (self.tagged_tokens[index][0], self.tagged_tokens[index][1] + end)
