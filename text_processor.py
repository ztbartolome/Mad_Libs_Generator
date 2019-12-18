from random import random

import nltk
from nltk import DefaultTagger, BigramTagger, TrigramTagger, UnigramTagger
from nltk.corpus import brown
from pickle import dump, load

tags_to_replace = []    # put the tags we want to replace in here


def train():
    """Trains the tagger on the Brown corpus"""
    tagged_sents = brown.tagged_sents()
    t0 = DefaultTagger('NN')  # last resort, tag everything left as NN
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
        self.raw    # may be unnecessary idk
        self.tagged_tokens
        self.word_replacements = {}  # will be a list of dictionaries of the form {(word, tag): replacement}

    def tag_passage(self, passage):
        """Tag the tokens in the passage"""
        tagger = load_tagger()
        tagger.tag(nltk.word_tokenize(passage))
        # todo: intransitive/transitive verb tagging

    def process_passage(self):
        """
        Takes a string with the raw text of a passage and removes random nouns/verbs/adjectives/adverbs,
        storing each removed word and its tag
        """

        for (token, tag) in self.tagged_tokens:
            if tag in tags_to_replace and random() > .5:
                self.word_replacements[(token, tag)] = None

    def replace(self, replacements):
        """Accepts a list of words entered by the user and replaces the corresponding words in the passage"""
        i = 0
        for key in self.word_replacements:
            self.word_replacements[key] = replacements[i]
            i += 1
        for token in self.tagged_tokens():
            if token in self.word_replacements:
                # todo: replace the word with self.word_replacements[token]
                pass
