from random import random
from string import punctuation


tags_to_replace = []    # put the tags we want to replace in here

def train():
    """Trains the tagger on the Brown corpus"""
    pass


class MadLibs(object):
    def __init__(self):
        self.raw    # may be unnecessary idk
        self.tagged_tokens
        self.word_replacements = {}  # will be a dictionary of the form {(word, tag): replacement}

    def tag_passage(self):
        """Tag the tokens in the passage"""
        pass

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
                # to do: replace the word with self.word_replacements[token]
                pass

    def determine_transitive(self):
        """Adds '-T' or '-IT' to the end of each verb tag depending on whether it is transitive or intransitive"""
        # for (token, tag) in self.tagged_tokens:
        #     transitive =
        #     if tag[:2] == 'VB':

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


