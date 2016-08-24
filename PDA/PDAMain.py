# Copyright (C) 2015 RJ Russell


# This program uses the PYTHON 3.4.3 interpreter.

from PDA import PDAMachine
import os


def main():
    """
        Asks for the file name and checks to make sure the file exists in the path given.
        Catches the return value, an displays result.
    """

    again = True
    # Continues to loop until user chooses to exit
    while again:
        clear_screen()
        instructions()

        file_name = input("Enter file name (including the path) or enter EXIT to quit program: ")
        if file_name.upper() == "EXIT":
            exit_program()

            # Ensures that the file path to the file entered is valid
        if not os.path.isfile(file_name):
            print("File does not exist")
            again = True
        else:
            run(file_name)

        again = go_again("\n\nTry Another PDA encoding? (Y/N): ")
        if not again:
            exit_program()


def run(file_name):
    """
        Opens file and loads in the PDA formatted JSON file.
        Takes input, and sends input to PDA.py to be processed.
    """
    again = True
    while again:
        # Variable to store PDA JSON when read in from file
        pda_params = None
        input_tape = []

        # Stores the file data into variable and displays the general PDA information
        pda_params = PDAMachine(file_name)
        print(pda_params.pda_info)

        # Takes in user input, stores in the list passed in
        get_input(input_tape)

        # Starts the PDA Machine and catches the return value.
        # Displays the result based on the return value
        result = pda_params.start_pda(input_tape)
        if result is True:
            print("String IS in the grammar!!!")
        elif result is False:
            print("String IS NOT the grammar!!! :)")
        else:
            print("Input '", result, "' is not in the alphabet")

        again = go_again("Run the same PDA encoding again? (Y/N): ")
        if not again:
            return


def get_input(input_tape):
    """
        Gets the string from user, reverses the input, and stores in the
        list passed in to be used as a stack.
    """

    user_input = input("Enter a string to check: ")
    for symbol in reversed(user_input):
        input_tape.append(symbol)


def instructions():
    print("""
            PDA Simulator

            All accompanying files are located in the json_files folder (be sure to
            include this folder in the file path).

            json_files/ab.json
            json_files/abc.json
            json_files/wwr.json
            json_files/01.json

            To test your own file, just type in the path to where the file is located.

        """)


def go_again(prompt):
    """ Controls if user wants to re-run PDA """

    response = 'n'
    while response not in ('Y', 'N'):
        response = input(prompt)
        response = response.upper()

    return response == "Y"


def exit_program():
    """ Exits the Program """

    print("Shutting down PDA...")
    input("Press <Enter> to EXIT program...")
    exit()


def clear_screen():
    """ Clears the screen for readability purposes """
    for i in range(1, 50):
        print("\n")


if __name__ == "__main__":
    main()
