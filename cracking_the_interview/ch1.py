import re
import pytest

# 1.1 - Determine if a string has all unique characters
def is_unique(strng):
  chars = {}
  for c in strng:
    if c in chars.keys():
      return False
    else:
      chars[c] = 1
  return True

def is_unique_set(string):
  chars = set()
  for c in string:
    if c in chars:
      return False
    else:
      chars.add(c)
  return True

# 1.1 - Without using another data structure
def is_unique_brute_force(strng):
  for i1 in range(len(strng)):
    for i2 in range(i1+1, len(strng)):
      if strng[i1] == strng[i2]:
        return False
  return True

# insertion, bubble, selection - n^2 running time
# merge(recursive), quick sort(recursive), heap sort - n log n

def is_unique_sort(strng):
  # strng.sort()                # mutative - will change var outside function
  str2 = sorted(strng)        # nonmutative
  for index in range(len(str2) - 1):
    if str2[index] == str2[index + 1]:
      return False
  return True

# abstracted test
def _test_is_unique(is_unique_function):
  assert is_unique_function("try")
  assert not is_unique_function("call")
  assert is_unique_function("beauty")
  assert is_unique_function("computer")
  assert not is_unique_function("free")
  assert is_unique_function("")

# passing test into abstracted test
def test_is_unique():
  _test_is_unique(is_unique)

def test_is_unique_set():
  _test_is_unique(is_unique_set)

def test_is_unique_brute_force(): 
  _test_is_unique(is_unique_brute_force)

def test_is_unique_sort():
  _test_is_unique(is_unique_sort)





# 1.2 - Given two strings, decide if one is a permutation of the other
def check_permutation(str1, str2):
  if str1 == "" and str2 == "":
    return True
  # if (str1 == "" and str2 != "") or (str1 !="" and str2 == ""):
  if len(str1) != len(str2):
    return False

  all_perms = all_permutations(str1)

  if str2 in all_perms:
    return True

  return False

def all_permutations(strng):
  if len(strng) == 0:
    return [""]
  else:
    first_char = strng[0]
    prev_s = all_permutations(strng[1:])  # recursive call generates (n-1)! strings
    # res_s = []
    res_s = set()  # list will grow to eventually have n! strings
    # for i in range(0, len(prev_s)):  # (n-1)! iterations
    #   substr_perm = prev_s[i]
    for substr_perm in prev_s:  # (n-1)! iterations
      for j in range(0, len(strng)):  # n iterations
        # put first character into every possible position in the substring permutation
        # new_s = prev_s[i][0:j] + strng[0] + prev_s[i][j:len(strng) - 1]
        new_s = substr_perm[:j] + first_char + substr_perm[j:]  # 2*n running time
        # if new_s not in res_s:  # 'in' takes up to n! running time to linear search
        #   res_s.append(new_s)   # constant time
        if new_s not in res_s:  # 'in' takes constant time to check set membership
          res_s.add(new_s)
    # overall running time:  (n-1)! * n * [2*n + n!]    ==>   O((n!)^2)    OMG
  return res_s  # n! strings

# all_permutations("fun") => ["fun", "fnu", "ufn", "unf", "nfu", "nuf"]

# strng = "fun"
# prev_s = all_permutations("un") => ["un", "nu"]
# res_s = []
# i in [0, 1]
# j in [0, 1, 2]
# j = 0: new_s = "" + "f" + "un"
# j = 1: new_s = "u" + "f" + "n"

# strng[0:-1] => "fu"
# prev_s[i] => "un"
# j = 1
# "un"[0:j] + "un"[j:2 - 1] => "u" + "n"

def test_check_perm():
  print check_permutation("thump", "humpt")
  print check_permutation("book", "okbo")
  print check_permutation("", "okbo")
  print check_permutation("", "")
  print check_permutation("code", "dope")

# test_check_perm()

# 1.3 - Write a method to replace all spaces in a string with '%20'
def urlify(strng):
  strng_arr = strng.split(" ")
  strng_arr = strng_arr[:-1]
  res = ""
  for string in strng_arr:
    res += string + "%20"
  return res

def test_urlify():
  print urlify(" Hello World")
  print urlify("NoSpacesHere")
  print urlify("FindTheSpaceAtTheEnd ")
  print urlify("This is a normal sentence with spaces.")
  print urlify("This has [] punctuation; in the middle")

# test_urlify()

# 1.4 - Given a string, check if it is a permutation of a palindrome.
# Palindrome is a word or phrase that is the same forward & backwards.
def is_palindrome(strng):
  strng = strng.lower()
  odd_str = len(strng) % 2      # 1 means odd number of char

  rx = re.compile('[^\w]')
  strng = rx.sub('', strng)

  if len(strng) == 0:
    raise Exception("Empty string")

  index = 0
  while index < len(strng)/2:
    if strng[index] != strng[len(strng) - index - 1]:
      return False
    index += 1

  return True

def palindrome_permutation(strng):
  permutations = all_permutations(strng)

  for p in permutations:
    if is_palindrome(p):
      return True
  return False

def test_is_palindrome():
  print is_palindrome("Hanah")                            # True
  print is_palindrome("Sara")                             # False
  print is_palindrome("A dog, a plan, a canal: pagoda.")  # True
  # print is_palslindrome("")                                 # Exception
  print is_palindrome("a")                                # True
  print is_palindrome("ab")                               # False
  print is_palindrome("aa")                               # True
  print is_palindrome("Otto sees Otto.")                  # True
  print is_palindrome("Otto 3.sees Otto.")                # False

def test_palindrome_permutation():
  print palindrome_permutation("Tact Coa")                          # True
  print palindrome_permutation("booger")                            # False
  print palindrome_permutation("bear ear")                          # True
  # print palindrome_permutation("")                                 # False
  print palindrome_permutation("Sara")                              # False

# test_is_palindrome()
# test_palindrome_permutation()

# 1.5 - Given two strings, determine if they are one edit (or zero) edit
# away form matching. Edits are add char, remove char or replace char
def one_away(str1, str2):
  index1 = 0
  index2 = 0
  num_edits = 0

  str1 = str1.lower()
  str2 = str2.lower()

  if str1 == str2:    # both empty strings or equal strings
    return True
  elif abs(len(str1) - len(str2)) == 1:
    return True
  else:
    while index1 < len(str1) and index2 < len(str2):
      if index1 == len(str1) - 1 and index2 == len(str2) - 1:
        if str1[index1] != str2[index2]:
          index1 += 1
          index2 += 1
          num_edits += 1
      elif str1[index1] == str2[index2]:
        if index1 == len(str1) - 1 and index2 == len(str2) - 1:   # zero edits
          return True
        index1 += 1
        index2 += 1
      elif str1[index1 + 1:] == str2[index2 + 1:]:                # replace edit
        return True
      elif str1[index1 + 1] == str2[index2 + 1]:
        index1 += 1
        index2 += 1
        num_edits += 1
      elif str1[index1 + 1] == str2[index2]:
        index1 += 1
        num_edits += 1
      elif str1[index1] == str2[index2 + 1]:
        index2 += 1
        num_edits += 1
    else:
      return False

  if num_edits > 1:
    return True
  return False

def test_one_away():
  print one_away("", "a")           # True
  print one_away("", "")            # True
  print one_away("", "ab")          # False
  print one_away("bake", "cake")    # True
  print one_away("bale", "fall")    # False
  print one_away("dog", "Dog")      # True
  print one_away("creAm", "cram")   # True

# test_one_away()

# 1.6 - Compress a given string to it's char followed by the char count.
# i.e. 'aabbbcddaaaa' would return 'a2b3c1d2a4'
# If compressed string is longer than original string, return original string.
def string_compression(strng):
  if strng == "":
    raise Exception("Empty string")

  index = 0
  new_s = ""
  curr = strng[index]
  curr_count = 0
  while index < len(strng):
    if strng[index] == curr:
      curr_count += 1
    else:
      new_s = new_s + curr + str(curr_count)
      curr = strng[index]
      curr_count = 1
    index += 1
  new_s = new_s + curr + str(curr_count)

  if len(new_s) > len(strng):
    new_s = strng

  return new_s

def test_string_compression():
  # print string_compression("")                # raise error
  print string_compression("aabbbcddaaaa")    # 'a2b3c1d2a4'
  print string_compression("abc")             # return original
  print string_compression("aa")              # return 'a2'
  print string_compression("a")               # return original

# test_string_compression()

# 1.7 - Given an image represented by an NxN matrix, where each pixel in img
# is 4 bytes, write a method to rotate the image by 90 degrees.
# Bonus: Do it in place
def rotate_matrix(mtx):
  n = len(mtx)
  
  for item in mtx:
    if len(item) != n:
      raise ValueError("Matrix must be NxN size")

  if n == 0:
    return mtx
  else:
    print "recursion here"

  return mtx

def test_rotate_matrix():
  mtx = []                    # base case - recursion???
  mtx1 = [ [1] ]
  mtx2 = [ [1, 2],
           [3, 4] ]
  mtx3 = [ [1, 2, 3],
           [8, 9, 4],
           [7, 6, 5] ]
  mtx4 = [ [1,   2,  3, 4],
           [12, 13, 14, 5],
           [11, 16, 15, 6],
           [10,  9,  8, 7] ]
  mtx_error = [ [1], [2] ]
  print rotate_matrix(mtx)
  print rotate_matrix(mtx1)
  print rotate_matrix(mtx2)
  print rotate_matrix(mtx3)
  print rotate_matrix(mtx4)
  # print rotate_matrix(mtx_error)      # raise error

test_rotate_matrix()

if __name__ == "__main__":
  pytest.main()




