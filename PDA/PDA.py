#  Copyright (C) 2015 RJ Russell

import json


class PDAMachine:
    """
        Initializes a PDA object, processes the input string, compares
        it to the JSON grammar, and returns the result.
    """

    pda_info = None
    input_alphabet = None
    start_variable = None
    variables = None
    grammar = None

    def __init__(self, file_name):
        """
            Loads data from PDA JSON file and initializes the data members.
        """
        pda_object = json.load(open(file_name))
        self.pda_info = pda_object["pda_info"]
        self.input_alphabet = pda_object["input_alph"]
        self.start_variable = pda_object["start_variable"]
        self.variables = pda_object["variables"]
        self.grammar = pda_object["grammar"]


    def start_pda(self, input_stack):
        """
            Processes the input through the PDA simulator.
            Looks at top of each stack:
                If top of stack is a variable, finds the corresponding
                    rule that coincides with the symbol at the top of input.
                If a terminal on top of stack, checks
                    If matches with top of input stack,
                    If matches, pops and discards both.
                Repeats process until either both stacks are empty or until
                a symbol in the sequence is not in the CFG.
            Returns the result to the calling method.
        """
        if not input_stack:
            return False

        # Starts with empty stack and pushes the Start Variable.
        stack = []
        stack.append(self.start_variable)

        # Loops while each stack has symbols or the process returns.
        while input_stack and stack:

            # Pops teh symbol on each stack so it can be looked at.
            stack_letter = stack.pop()
            symbol = input_stack.pop()

            # Checks if input symbol is valid
            if symbol not in self.input_alphabet:
                return symbol

            # Checks that the top of stack is not a terminal
            # (ie. Top of the stack is a variable and pushes the coinciding rule)
            if symbol != stack_letter:
                # Since top of stack is a variable, pushes the input symbol back on the
                # input stack for the next loop.:
                input_stack.append(symbol)

                # Checks if the rule is in the stack alphabet,
                # Pushes the coinciding rule on the stack in reverse order
                # to simulate stack-like behavior.
                if stack_letter in self.variables:
                    for rule in self.grammar[stack_letter]:
                        if symbol == rule[0]:
                            for letter in rule[::-1]:
                                stack.append(letter)
                            break
                    # Returns false if there is no rule for the symbol from the input stack
                    else:
                        return False
                # Stack symbol is not a variable, and the stack symbol and
                # input symbol aren't a match (if they match this isn't reached).
                else:
                    return False


        # checks if stacks are empty or not and returns the result.
        return (not input_stack) and (not stack)

