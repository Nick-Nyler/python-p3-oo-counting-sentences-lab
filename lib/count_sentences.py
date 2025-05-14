#!/usr/bin/env python3

import re
import sys

class MyString:
    def __init__(self, value=''):
        if isinstance(value, str):
            self._value = value
        else:
            print("The value must be a string.")
            self._value = ''

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")
            self._value = ''

    def is_sentence(self):
        return self._value.endswith('.')

    def is_question(self):
        return self._value.endswith('?')

    def is_exclamation(self):
        return self._value.endswith('!')

    def count_sentences(self):
        # Use regex to split the string by one or more sentence-ending punctuation marks
        sentences = re.split(r'[.?!]+', self._value)
        # Filter out any empty strings that might result from the split
        return len([s.strip() for s in sentences if s.strip()])

# Example Usage:
complex_string = MyString("This, well, is a sentence. This is too!! And so is this, I think? Woo...")
print(f"'{complex_string.value}' has {complex_string.count_sentences()} sentences.")