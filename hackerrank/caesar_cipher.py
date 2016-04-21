#!/usr/bin/python
# -*- coding: ascii -*-

# Julius Caesar protected his confidential information by encrypting it in a cipher. Caesar's cipher rotated every letter in a string by a fixed number, KK, making it unreadable by his enemies. Given a string, SS, and a number, KK, encrypt SS and print the resulting string.

# Note: The cipher only encrypts letters; symbols, such as -, remain unencrypted.

# Input Format

# The first line contains an integer, N, which is the length of the unencrypted string. 
# The second line contains the unencrypted string, S. The third line contains the integer
# encryption key, K, which is the number of letters to rotate.

# Constraints 
# 1 ≤ N ≤ 100
# 0 ≤ K ≤ 100
# S is a valid ASCII string and doesn't contain any spaces.

# Output Format
# For each test case, print the encoded string.

# Sample Input
# 11
# middle-Outz
# 2

# Sample Output
# okffng-Qwvb

# Explanation
# Each unencrypted letter is replaced with the letter occurring K spaces after it when
# listed alphabetically. Think of the alphabet as being both case-sensitive and circular; if KK rotates past the end of the alphabet, it loops back to the beginning (i.e.: the letter after zz is aa, and the letter after ZZ is AA).

# Selected Examples: 
# m (ASCII 109) becomes o (ASCII 111). 
# i (ASCII 105) becomes k (ASCII 107). 
# − remains the same, as symbols are not encoded. 
# O (ASCII 79) becomes Q (ASCII 81). 
# z (ASCII 122) becomes b (ASCII 98); because z is the last letter of the alphabet, a
# (ASCII 97) is the next letter after it in lower-case rotation.


import sys

n = int(raw_input().strip())
s = raw_input().strip()
k = int(raw_input().strip())

encoded = ""

for index in range(n):
  if s[index].isalpha():
    asc = (ord(s[index]) + k)
    if asc > 96:
      asc = asc % 122
      if asc < 97:
        asc += 96
    elif asc > 64 and asc < 91:
      asc = asc % 91
      if asc < 65:
        asc += 64
    encoded += chr(asc)
  else:
   encoded += s[index]

print encoded












