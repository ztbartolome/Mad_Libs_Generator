import io
from contextlib import redirect_stdout
from random import choice as rand
import text_processor
import descriptions
import nltk

tag_names = {'NN': 'Singular Noun'}  # dictionary with the names of each tag that we want to show the user
tag_examples = None


def run():
    text_processor.train()
    make_tag_examples()
    print("Welcome! This program can generate mad libs for you by replacing words in a passage.")
    choice = -1
    mad_libs = text_processor.MadLibs()
    while choice not in ['0', '1', '2']:
        print("How would you like the mad libs to be generated?")
        print("0 - choose from available passages")
        print("1 - provide your own passage")
        print("2 - random")
        choice = input("Please enter the number of your choice: ")
    if choice == '0':
        mad_libs.process_passage(choose_passage())
    elif choice == '1':
        mad_libs.process_passage(input("Please paste your passage:\n"))
    elif choice == '2':
        pass
    else:
        pass


def choose_passage():
    """Prints list of available passages and returns the text of the file the user chooses"""
    pass


def enter_words(tags):
    """Prompt the user to enter a word for each tag in the list tags"""
    words = []
    print("Please enter a word for each prompt, or enter 'h' for help")
    for tag in tags:
        print(tag_names[tag], end=': ')
        user_input = input()
        while user_input == 'h':
            print('Examples of', tag_names[tag], end=': ')
            print(text_processor.tag_examples_dict[tag])
            user_input = input()
        words.append(user_input)


def make_tag_examples():
    tags = text_processor.tags_to_replace
    for t in tags:
        if t not in text_processor.tag_examples_dict:
            f = io.StringIO()
            with redirect_stdout(f):
                nltk.help.upenn_tagset(t)
            help_output = f.getvalue()
            index_start = help_output.find('    ') + 4
            index_end = help_output.find('    ', index_start) - 1
            text_processor.tag_examples_dict[t] = help_output[index_start:index_end]


if __name__ == '__main__':
    run()
