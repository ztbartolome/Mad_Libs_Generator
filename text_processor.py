from random import random


tags_to_replace = []    # put the tags we want to replace in here

def train():
    """Trains the tagger on the Brown corpus"""
    pass


class MadLibs(object):
    def __init__(self):
        self.raw    # or maybe it would be better to store a list of tokens
        self.word_replacements = []  # will be a list of dictionaries of the form {'og':(word,tag), 'new':word}

    def process_passage(self):
        """
        Takes a string with the raw text of a passage and removes random nouns/verbs/adjectives/adverbs,
        storing each removed word and its tag
        """
        tagged_tokens = []  # placeholder

        for (token, tag) in tagged_tokens:
            if tag in tags_to_replace and random() > .5:
                self.word_replacements.append({'og': (token, tag)})


    def replace(self, replacements):
        """"""
        for i in range(self.word_replacements):
            self.word_replacements[i]['new'] = replacements[i]
