#!/usr/bin/env python3


class MyString:
    
    def __init__(self, value = ""):
        self.value = value

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        if isinstance(value, str):
            self._value = value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        if self.value.endswith(".") == True:
            return True
        else:
            return False
        
    def is_question(self):
        if self.value.endswith("?") == True:
            return True
        else:
            return False
        
    def is_exclamation(self):
        if self.value.endswith("!") == True:
            return True
        else:
            return False
    
    def count_sentences(self):
        split_list = self.value.replace("!", ".").replace("?", ".").split(".")
        item_to_remove = split_list.count('')
        for i in range(item_to_remove):
            split_list.remove('')
        return len(split_list)
    
    