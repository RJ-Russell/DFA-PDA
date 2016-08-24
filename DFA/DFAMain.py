#  Copyright (C) 2015 RJ Russell

import os.path
from DFA import DFAMachine


def main():
    """
        Loads JSON formatted DFA text file, sends to DFAMachine,
        processes return value and displays accept/reject message.
    """

    # Stores DFA JSON object.
    dfa_param = None

    # Stores if user wants to run machine again.
    again = True

    while again:
        file_name = choose_dfa()

        if file_name == "EXIT":
            exit_program()


        # If filename is valid, sends filename to DFA module to be loaded,
        # Then stores the returned initialized DFA object
        # if os.path.isfile(file_name):

        dfa_param = DFAMachine(file_name).load_dfa_data

        print(dfa_param.dfa_info + "\n")
        user_string = str(input("Enter test string for the DFA: "))

        # starts the DFA Machine, passes the user input,
        # stores and displays the result.
        result = dfa_param.start_machine(user_string)
        if result == "accepted":
            print("\nINPUT ACCEPTED...")
            print("Input IS in the language recognized by this DFA! :) ")
        elif result == "failed":
            print("\nINPUT REJECTED...")
            print("Input is NOT in the language recognized by this DFA! :( ")
        else:
            print("\nSymbol '", result, "' is not in the alphabet set.")
            print("\nDFA processing halted...")

        if not go_again():
            again = False
            exit_program()


def choose_dfa():
    """
        Gives list of files to pipe through the DFA, error checks user selection,
        and returns filename.
    """

    response = None
    print("\nChoose from the following list of DFAs:")
    print(
        """
            1. a^nb^n, 0<= n <= 3
            2. Binary Multiple of 5
            3. (a|b)*abb
            4. Even zeros or three ones
            5. Using ! = 0, ? = 1, binary multiples of 4
            6. EXIT
        """
    )

    flag = True
    while flag:
        try:
            response = int(input("\nChoose a number: "))
            if not response:
                raise ValueError("empty string")
            else:
                flag = False
        except ValueError as e:
            print(e)

        if response not in range(1, 7):
            print("Invalid Selection. Try Again...\n\n")
            flag = True

        if response == 1:
            return "json_files/anbn.txt"
        elif response == 2:
            return "json_files/binarymultiple5.txt"
        elif response == 3:
            return "json_files/ab_abb.txt"
        elif response == 4:
            return "json_files/even0three1.txt"
        elif response == 5:
            return "json_files/quest_mark_binmult4.txt"
        elif response == 6:
            return "EXIT"
        else:
            print("*** File choice Not Valid: Try again! ***\n\n")


def go_again():
    """Controls if user wants to re-run a DFA"""
    response = None
    while response not in ("Y", "N"):
        response = input("\n\nWould you like to start the Machine again? (Y/N): ").upper()
    if response == "Y":
        return True
    else:
        return False


def exit_program():
    """Exits the program"""
    print("Shutting down DFA...")
    input("\nPress <Enter> to EXIT program...")
    exit()


if __name__ == "__main__":
    main()
