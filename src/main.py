# Import necessary modules
import os

# Import necessary helper classes
from splitter import Splitter
from messenger import Messenger
from logger import Logger

# main
def main():
    # Set working directory to project folder
    os.chdir('../.')
    print(os.getcwd())

    # Create Logger File to track all changes
    logger = Logger(os)

    # Create a list of words for parser to ignore
    stop_words = []#['PSY', 'STAT']

    ninja = Splitter(stop_words)

    ans = input('Do you want to manually input lines? ')

    # Create Messenger Object to ask prompts
    if 'y' in ans or 'Y' in ans:
        messenger = Messenger()

        line = ''
        exit = False

        while not exit:
            line = messenger.collect_input()

            if line == 'quit' or line == 'exit':
                exit = True
            else:
                # Output would be collected here
                print(ninja.split_line(line))
    #else:


    print('Exiting code')


main()
