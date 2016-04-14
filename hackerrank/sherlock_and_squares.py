# Watson gives two integers (A and B) to Sherlock and asks if he can count
# the number of square integers between A and B (both inclusive).

# Note: A square integer is an integer which is the square of any integer.
# For example, 1, 4, 9 and 16 are some of the square integers as they are
# squares of 1, 2, 3 and 4, respectively.

# Input Format 
# The first line contains T, the number of test cases. T test cases follow,
# each in a new line. Each test case contains two space-separated integers
# denoting A and B.

# Output Format 
# For each test case, print the required answer in a new line.

# Constraints 
# 1 ≤ T ≤ 100
# 1 ≤ A ≤ B ≤ 10^9

import sys
import math

def num_squares(lower, upper):
  if upper < lower:
    return 0

  if lower < 0:
    lower = 0
  if upper < 0:
    return 0

  lower_sq = int(math.ceil(math.sqrt(lower)))
  upper_sq = int(math.floor(math.sqrt(upper)))

  return upper_sq - lower_sq + 1

t = int(raw_input().strip())
for a0 in xrange(t):
  bounds = raw_input().split()
  lower = int(bounds[0])
  upper = int(bounds[1])
  print num_squares(lower, upper)