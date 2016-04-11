# The Utopian Tree goes through 2 cycles of growth every year. Each spring,
# it doubles in height. Each summer, its height increases by 1 meter.

# Laura plants a Utopian Tree sapling with a height of 1 meter at the onset
# of spring. How tall will her tree be after N growth cycles?

# Input Format
# The first line contains an integer, T, the number of test cases. 
# T subsequent lines each contain an integer, N, denoting the number of
# cycles for that test case.

# Constraints 
# 1 ≤ T ≤ 10
# 0 ≤ N ≤ 60

# Output Format
# For each test case, print the height of the Utopian Tree after N cycles.
# Each height must be printed on a new line.

import sys

t = int(raw_input().strip())
for a0 in xrange(t):
  n = int(raw_input().strip())
  height = 1
  if n < 0:
    raise Exception("Invalid number of cycles")
  if n % 2 == 0:
    while n > 0:
      height *= 2
      heigh += 1
      n -= 2
  elif n == 1:
    height *= 2
  else:
    while n > 1:
      height *= 2
      heigh += 1
      n -= 2
    height += 2
  print height


