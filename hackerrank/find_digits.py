# Given an integer, N, traverse its digits (d1,d2,...,dn) and determine how many
# digits evenly divide N (i.e.: count the number of times N divided by each
# digit di has a remainder of 0). Print the number of evenly divisible digits.

# Note: Each digit is considered to be unique, so each occurrence of the same
# evenly divisible digit should be counted (i.e.: for N=111, the answer is 33).

# Input Format
# The first line is an integer, T, indicating the number of test cases. 
# The T subsequent lines each contain an integer, N.

# Constraints 
# 1 ≤ T ≤ 15
# 0 < N < 109

# Output Format
# For every test case, count and print (on a new line) the number of digits in N 
# that are able to evenly divide N.

import sys

t = int(raw_input().strip())
for a0 in xrange(t):
  n = int(raw_input().strip())
  n_str = str(n)

  count = 0

  for i in range(len(n_str)):
    if n_str[i] == "0":
      continue
    elif n % int(n_str[i]) == 0:
      count += 1

  print count