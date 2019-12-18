# Mad_Libs_Generator

This is a Mad Libs generator based on the game Mad Libs in which one person prompts others to fill in the blanks of a 
passage according to parts of speech. This generator randomly takes out words from a passage for the user to replace.

## Requirements for Running the Program
Python 3

NLTK

## How to Run
Enter 'python main.py' or 'python3 main.py' in your command line to run the program.

Follow the printed prompts for input.


## Files
The repository contains the files
* `main.py` which runs the program and handles user interaction
* `text_processor.py` which deals with training, tagging, and replacing words in passages
* `pos_tagger_brown.pkl` which stores the POS tagger
* the `passages` folder which contains .txt files that can be used to generate Mad Libs
(see the Sources section below for the source of each .txt file)


## Libraries Used
* nltk
* string
* pickle
* io
* os
* contextlib
* random

## Sources
* `all_star.txt`: from *All Star* (by Smashmouth)
* `do_not_go_gentle.txt`: from *Do Not Go Gentle Into That Good Night* (by Dylan Thomas)
* `doctor_who.txt`: from *Doctor Who*
* `famous_blue_raincoat`: from *Famous Blue Raincoat* (by Leonard Cohen)
* `moana.txt`: from *How Far I'll Go* (by Lin-Manuel Miranda)
* `pain.txt`: from *The Princess Bride* (by William Goldman)
* `shia.txt`: from *Shia LaBeouf* (by Rob Cantor)
* `true_detective.txt`: from *True Detective*
* `unfortunate_events.txt`: from *A Series of Unfortunate Events: The Slippery Slope* (by Lemony Snicket)
* `zelda.txt`: from *The Legend of Zelda: A Link to the Past*
* `zootopia.txt`: from *Zootopia*
