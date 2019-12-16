from random import random


tags_to_replace = []    # put the tags we want to replace in here

def train():
    """Trains the tagger on the Brown corpus"""
    pass


class MadLibs(object):
    def __init__(self):
        self.raw    # may be unnecessary idk
        self.tagged_tokens
        self.word_replacements = {}  # will be a list of dictionaries of the form {(word, tag): replacement}

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
