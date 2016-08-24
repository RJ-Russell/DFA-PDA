# Copyright (C) 2015 RJ Russell

import json


class DFAMachine:
    """Initializes a DFA object, parses and processes it, returns the result"""
    dfa_info = None
    states = None
    alphabet = None
    transition_table = None
    start_state = None
    accept_states = None

    def __init__(self, file_name):
        """Loads text file with json formatting, initializes data members"""
        dfa_object = json.load(open(file_name))
        self.dfa_info = dfa_object["dfa_info"]
        self.states = dfa_object["state_list"]
        self.alphabet = dfa_object["alph_list"]
        self.transition_table = dfa_object["transition_dict"]
        self.start_state = dfa_object["start_state"]
        self.accept_states = dfa_object["accept_list"]

    @property
    def load_dfa_data(self):
        """Returns the initialized DFA object back to the calling method"""
        return self

    def start_machine(self, user_string):
        """
        Parses user input through the loaded DFA,
        tracks and moves to each state based on DFA definitions and
        the next symbol in the user input, returns outputs and returns
        final results.
        """
        current_state = self.start_state
        print("Initializing the Machine...")
        print("\nStart State ---->", current_state)

        for symbol in user_string:
            if symbol not in self.transition_table[current_state]:
                return symbol

            transition_state = self.transition_table[current_state][symbol]
            print("Input:", symbol, "-> Transitioning:", current_state,
                  "---->", transition_state)

            current_state = transition_state

        if current_state in self.accept_states:
            print("\n" + current_state, "is an ACCEPT STATE...")
            return "accepted"
        else:
            print("\n" + current_state, "is NOT an ACCEPT STATE...")
            return "failed"
