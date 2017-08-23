# Author: Joris Rietveld <jorisrietveld@gmail.com>
# Created: 23-08-2017 13:38
# Licence: GPLv3 - General Public Licence version 3
from core import Interpreter


def main():
    continue_running = True

    while continue_running:
        try:
            # Read user input and try to parse and execute it.
            text = input('[pascal interpreter] << ')

        # When something goes wrong, let pythons exception handler handle the mess.
        except EOFError:
            break
        # When no user input is entered? Just keep starting over until something gets passed or continue waiting to some
        # time before the heat death of the universe when the humanity chances to interpret awesome code are gone. (or
        # when someone just cuts the power, but the head death thing sounds more dramatic)
        if not text:
            continue

        if text == 'q' or text == 'quit' or text == 'quit()' or text == 'exit':
            continue_running = False
            print('Thanks for using my pascal interpreter, goodbye!')
            continue

        # Create an new Interpreter instance and pass it some code to interpret.
        interpreter = Interpreter(text)
        result = interpreter.expression()
        print(result)

if __name__ == '__main__':
    main()
