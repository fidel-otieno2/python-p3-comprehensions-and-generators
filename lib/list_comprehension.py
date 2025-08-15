#!/usr/bin/env python3

def return_evens(num_list):
    """Return a list of even numbers from the input list."""
    return [num for num in num_list if num % 2 == 0]

def make_exclamation(sentence_list):
    """Return a list of sentences with exclamation marks added."""
    return [sentence + "!" for sentence in sentence_list]
