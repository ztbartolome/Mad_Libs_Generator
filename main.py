from random import choice as rand
import text_processor
import descriptions

tag_names = {'NN': 'Singular Noun'}  # dictionary with the names of each tag that we want to show the user


def run():
    text_processor.train()
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
            print(tag_names[tag], end=': ')

            # to do: print helpful description

            user_input = input()
        words.append(user_input)


if __name__ == '__main__':
    run()