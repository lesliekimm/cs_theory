# You're working on a secret team solving coded transmissions. Your team is scrambling
# to decipher a recent message, worried it's a plot to break into a major European
# National Cake Vault. The message has been mostly deciphered, but all the words are
# backwards! Your colleagues have handed off the last step to you.

# Write a function reverse_words() that takes a string message and reverses the order
# of the words in-place.

# Since strings in Python are immutable, we'll first convert the string into a list of
# characters, do the in-place word reversal on that list, and re-join that list into a
# string before returning it. This isn't technically "in-place" and the list of
# characters will cost O(n) additional space, but it's a reasonable way to stay
# within the spirit of the challenge. If you're comfortable coding in a language with
# mutable strings, that'd be even better!

# When writing your function, assume the message contains only letters and spaces, and
# all words are separated by one space.

import pytest

def reverse_words(string):
  string_char = list(string)

  for index_front in xrange(len(string_char) / 2):
    index_back = -index_front - 1
    string_char[index_front], string_char[index_back] = string_char[index_back], string_char[index_front]

  front = 0
  back = 0

  while back < len(string_char):
    while string_char[back] != ' ':
      back += 1
      if back == len(string_char):
        break;

    word_front = front
    word_back = back - 1

    for word_front in xrange(((word_back - word_front) / 2) + 1):
      word_back = word_back - word_front

      string_char[word_front + front], string_char[word_back] = string_char[word_back], string_char[word_front + front]

    front = back + 1
    back += 1

  reversed = ''.join(string_char)

  return reversed

def test_reverse_words():
  message_empty = ""
  message_double_space = "find  you will"
  message_short = "find you will "
  message_short_space = " find you will "
  message = "find you will pain only go you recordings security the into if"
  
  assert reverse_words(message_empty) == ""
  assert reverse_words(message_double_space) == "will you  find"
  assert reverse_words(message_short) == " will you find"
  assert reverse_words(message_short_space) == " will you find "
  assert reverse_words(message) == "if into the security recordings you go only pain will you find"










