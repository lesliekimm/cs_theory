# Angry Professor
# A Discrete Mathematics professor has a class of N students.
# Frustrated with their lack of discipline, he decides to
# cancel class if fewer than K students are present when
# class starts.

# Given the arrival time of each student, determine if the
# class is canceled.

# Input Format
# The first line of input contains T, the number of test cases.

# Each test case consists of two lines.
# The first line has two space-separated integers, N
# (students in the class and K (the cancelation threshold).
# The second line contains N space-separated integers
# (a1,a2,…,aNa1,a2,…,aN) describing the arrival times for
# each student.

# Note: Non-positive arrival times (ai≤0ai≤0) indicate the
# student arrived early or on time; positive arrival times 
# (ai>0ai>0) indicate the student arrived ai, 0ai minutes 
# late.

# Output Format
# For each test case, print the word YES if the class is
# canceled or NO if it is not.

# Constraints
# 1≤T≤10
# 1≤N≤1000
# 1≤K≤N
# −100≤ai≤100,where i∈[1,N]−100≤ai≤100,where i∈[1,N]

# Note 
# If a student arrives exactly on time (ai=0)(ai=0),
# the student is considered to have entered before the
# class started.

import sys

def cancel_class(enrolled, threshold, arrival_times):
  on_time = 0

  for x in range(0, enrolled):
    if arrival_times[x] <= 0:
      on_time += 1

  if on_time >= threshold:
    print "NO"  
  else:
    print "YES"

t = int(raw_input().strip())

if (t < 1 or t > 10):
  raise Exception("Invalid number of classes.")

for a0 in xrange(t):
  n,k = raw_input().strip().split(' ')
  n,k = [int(n),int(k)]
  a = map(int,raw_input().strip().split(' '))

  if (n < 1 or n > 1000):
    raise Exception("Invalid number of students.")

  if (k < 1 or k > n):
    raise Excpetion("Invalid threshold.")

  for x in range(0, len(a)):
    if (a[x] < -100 or a[x] > 100):
      raise Exception("Invalid arrival time.")

  cancel_class(n, k, a)


