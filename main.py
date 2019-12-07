from random import choice as rand


def run():
    print("Welcome! This program can generate mad libs for you by replacing words in a passage.")
    choice = -1
    while choice not in ['0', '1', '2']:
        print("How would you like the mad libs to be generated?")
        print("0 - choose from available passages")
        print("1 - provide your own passage")
        print("2 - random")
        choice = input("Please enter the number of your choice: ")
    if choice == '0':
        process_passage(choose_passage())
    elif choice == '1':
        process_passage(input("Please paste your passage:\n"))
    else:
        pass


def choose_passage():
    """Prints list of available passages and returns the text of the file the user chooses"""
    pass


def process_passage(text):
    """placeholder for the function that accepts the raw text of a passage as a string and processes the passage
    might be better to put this in a separate class
    """
    pass


if __name__ == '__main__':
    run()