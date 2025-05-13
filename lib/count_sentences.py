#!/usr/bin/env python3

class MyString:
  def __init__(self, value=''):
    self._value = ''
    self.value = value # use setter for validation

  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self, value):
    if not isinstance(value, str):
      print("The value must be a string.")
   
    self._value = value

  def is_sentence(self):
    if self._value.endswith('.'):
      return True
    else:
      return False
    
  def is_question(self):
    if self._value.endswith('?'):
      return True
    else:
      return False
    
  def is_exclamation(self):
    if self._value.endswith('!'):
      return True
    else:
      return False
    
  def count_sentences(self):
    sentences = self._value.split('.')
    return len(sentences) - 1 if sentences[-1] == '' else len(sentences)

string = MyString()
string.value = "This is a string! It has three sentences. Right?"
print(string.is_question()) # False