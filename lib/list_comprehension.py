#!/usr/bin/env python3

def return_evens(num_list):
    # even_numbers = [(n % 2 == 0) for n in num_list] boyle yazinca boolean true/false oalrak evaluate ediypr ve number yerine true false return yapiyor.
    even_numbers = [n for n in num_list if n % 2 == 0]
    if even_numbers:
        return even_numbers
    else:
        return []


def make_exclamation(sentence_list):
    # checks if the sentence_list empty
    if not sentence_list:
         return []
    exclamation_added = []
    for sentence in sentence_list:
            if sentence.endswith("!"):
                exclamation_added.append(sentence)
            else:
                 exclamation_added.append(sentence + "!")
    return exclamation_added

    
# Users can use the If with not in Python to check whether the variable is empty or assigned with some values.

# returns list of sentences with exclamation marks
#     create a variable has an empty array 
#     for each sentence in sentence list append sentence with ! to that variable
