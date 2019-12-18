import io
from contextlib import redirect_stdout
from random import choice as rand
import text_processor
import descriptions
import nltk
import os


def run():
    text_processor.load_tagger()
    make_tag_examples()
    print("Welcome! This program can generate mad libs for you by replacing words in a passage.")
    choice = ''
    mad_libs = text_processor.MadLibs()
    while not choice.isnumeric() or choice == '' or int(choice) not in range(3):
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
        mad_libs.process_passage(random_passage())
    tags_to_replace = [tag for (token, tag) in mad_libs.word_replacements.keys()]
    print(mad_libs.replace(enter_words(tags_to_replace)))


def choose_passage():
    """Prints list of available passages and returns the text of the file the user chooses"""
    print("Here are the available passages:")
    files = list(os.listdir('passages'))
    for i in range(len(files)):
        # print number, name of file, and first 50 characters of file
        print(i, files[i], '\t', repr(open(os.path.join('passages', files[i]), 'r').read()[:50]), '...')
    choice = ''
    while not choice.isnumeric() or choice == '' or int(choice) not in range(len(files)):
        choice = input('Please enter the number for the passage of your choice: ')
    return open(os.path.join('passages', files[int(choice)]), 'r').read()


def random_passage():
    """Returns the text of a random passage from the passages folder"""
    files = list(os.path.join('passages', filename) for filename in os.listdir('passages'))
    return open(rand(files), 'r').read()


def enter_words(tags):
    """Prompt the user to enter a word for each tag in the list tags"""
    words = []
    print("Please enter a word for each prompt, or enter 'h' for help")
    for tag in tags:
        print(text_processor.tag_names[tag], end=': ')
        user_input = input()
        while user_input == 'h':
            print('Examples of', text_processor.tag_names[tag], end=': ')
            print(text_processor.tag_examples[tag])
            user_input = input()
        words.append(user_input)
    return words


def make_tag_examples():
    tags = text_processor.tags_to_replace
    for t in tags:
        if t.find('-') > -1:
            t_pref = t[:t.find('-')]
            t_suff = t[t.find('-') + 1:]
        else:
            t_pref = t
            t_suff = ''
        f = io.StringIO()
        with redirect_stdout(f):
            nltk.help.upenn_tagset(t_pref)
        help_output = f.getvalue()
        ex_start = help_output.find('    ') + 4
        ex_end = help_output.find('\n', ex_start)
        name_start = help_output.find(': ') + 2
        name_end = help_output.find('\n')
        text_processor.tag_examples[t] = help_output[ex_start:ex_end]
        text_processor.tag_names[t] = help_output[name_start:name_end]
        if t_suff == 'T':
            text_processor.tag_names[t] += ' (transitive)'
        elif t_suff == 'IT':
            text_processor.tag_names[t] += ' (intransitive)'


if __name__ == '__main__':
    run()
