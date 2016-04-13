import re
import pytest

# 1.1 - determine if a string has all unique characters
# use dictionary to store chars as keys
def is_unique(strng):
  chars = {}
  for c in strng:
    if c in chars.keys():
      return False
    else:
      chars[c] = 1
  return True

# use set to store chars because we don't need key, value pairs
def is_unique_set(strng):
  chars = set()
  for c in strng:
    if c in chars:
      return False
    else:
      chars.add(c)
  return True

# without using another data structure - brute force method
def is_unique_brute_force(strng):
  for i1 in range(len(strng)):
    for i2 in range(i1+1, len(strng)):
      if strng[i1] == strng[i2]:
        return False
  return True

# different types of sorts
# insertion, bubble, selection - n^2 runtime
# merge(recursive), quick sort(recursive), heap sort - nlog(n) runtime

# sort char in strng first to compare one value and the next
def is_unique_sort(strng):
  # strng.sort()                # mutative - will change var outside function
  str2 = sorted(strng)        # nonmutative - requires 2n space bc str2 is copy
  for index in range(len(str2) - 1):
    if str2[index] == str2[index + 1]:
      return False
  return True

# abstracted test
def _test_is_unique(is_unique_function):
  assert is_unique_function("try")          # True
  assert not is_unique_function("call")     # False
  assert is_unique_function("beauty")       # True
  assert is_unique_function("computer")     # True
  assert not is_unique_function("free")     # False
  assert is_unique_function("")             # True

# passing function into abstracted test
def test_is_unique():
  _test_is_unique(is_unique)

def test_is_unique_set():
  _test_is_unique(is_unique_set)

def test_is_unique_brute_force(): 
  _test_is_unique(is_unique_brute_force)

def test_is_unique_sort():
  _test_is_unique(is_unique_sort)





# 1.2 - given two strings, decide if one is a permutation of the other
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

# original function
def perm(strng):
  if len(strng) == 0:
    return [""]
  else:
    prev_s = perm(strng[1:])              # recursive call generates (n-1)! strings
    res_s = []                            # list will grow to have n! strings
    for i in range(0, len(prev_s)):       # (n-1)! iterations
      for j in range (0, len(strng)):     # n iterations
        new_s = prev_s[i][0:j] + strng[0] + prev_s[i][j:len(strng) - 1] # 2n runtime
        if new_s not in res_s:            # 'in' takes up to n! runtime for linear search
          res_s.append(new_s)             # constant time
  return res_s                            # overall runtime: (n-1)! * n * [2n + n!] ==> O((n!)^2) OMG

# function worked out with alan improves runtime by n! by using set for search
# instead of appendng strings to a new list
def all_permutations(strng):
  if len(strng) == 0:
    return [""]
  else:
    first_char = strng[0]
    prev_s = all_permutations(strng[1:])  # recursive call generates (n-1)! strings
    res_s = set()                         # list will grow to eventually have n! strings
    for substr_perm in prev_s:            # (n-1)! iterations
      for j in range(0, len(strng)):      # n iterations
        # put first character into every possible position in the substring permutation
        new_s = substr_perm[:j] + first_char + substr_perm[j:]  # 2*n running time
        if new_s not in res_s:            # 'in' takes constant time to check set membership
          res_s.add(new_s)                # constant time
  return res_s                            # overall runtime: n!

# all_permutations("fun") => ["fun", "fnu", "ufn", "unf", "nfu", "nuf"]

# strng = "fun"
# prev_s = all_permutations("un") => ["un", "nu"]
# res_s = []
# i in [0, 1]
# j in [0, 1, 2]
# j = 0: new_s = "" + "f" + "un"
# j = 1: new_s = "u" + "f" + "n"

def test_check_perm():
  assert check_permutation("thump", "humpt")    # True
  assert check_permutation("book", "okbo")      # True
  assert not check_permutation("", "okbo")      # False
  assert check_permutation("", "")              # True
  assert not check_permutation("code", "dope")  # False





# 1.3 - write a method to replace all spaces in a string with '%20'
def urlify(strng):
  strng_arr = strng.split(" ")
  strng_arr2 = strng_arr[:-1]
  res = ""
  for string in strng_arr2:
    res += string + "%20"
  res += strng_arr[-1]
  return res

def test_urlify():
  assert urlify(" Hello World") == "%20Hello%20World"
  assert urlify("NoSpacesHere") == "NoSpacesHere"
  assert urlify("FindTheSpaceAtTheEnd ") == "FindTheSpaceAtTheEnd%20"
  assert urlify("This is a normal sentence with spaces.") == "This%20is%20a%20normal%20sentence%20with%20spaces."
  assert urlify("This has [] punctuation; in the middle") == "This%20has%20[]%20punctuation;%20in%20the%20middle"





# 1.4 - given a string, check if it is a permutation of a palindrome
# palindrome is a word or phrase that is the same forward & backwards
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
  assert is_palindrome("Hanah")                            # True
  assert not is_palindrome("Sara")                         # False
  assert is_palindrome("A dog, a plan, a canal: pagoda.")  # True
  # print is_palslindrome("")                                 # Exception
  assert is_palindrome("a")                                # True
  assert not is_palindrome("ab")                           # False
  assert is_palindrome("aa")                               # True
  assert is_palindrome("Otto sees Otto.")                  # True
  assert not is_palindrome("Otto 3.sees Otto.")            # False

def test_palindrome_permutation():
  assert palindrome_permutation("Tact Coa")                # True
  assert not palindrome_permutation("booger")              # False
  assert palindrome_permutation("bear ear")                # True
  # print palindrome_permutation("")                       # False
  assert not palindrome_permutation("Sara")                # False





# 1.5 - given two strings, determine if they are one edit (or zero) edit
# away from matching
# edits are add char, remove char or replace char
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
  assert one_away("", "a")              # True
  assert one_away("", "")               # True
  assert not one_away("", "ab")         # False
  assert one_away("bake", "cake")       # True
  assert not one_away("bale", "fall")   # False
  assert one_away("dog", "Dog")         # True
  assert one_away("creAm", "cram")      # True





# 1.6 - compress a given string to it's char followed by the char count
# i.e. 'aabbbcddaaaa' would return 'a2b3c1d2a4'
# if compressed string is longer than original string, return original string
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
  assert string_compression("aabbbcddaaaa") == "a2b3c1d2a4"
  assert string_compression("abc") == "abc"
  assert string_compression("aa") == "a2"
  assert string_compression("a") == "a"





# 1.7 - given an image represented by an NxN matrix, where each pixel in img
# is 4 bytes, write a method to rotate the image by 90 degrees.
# bonus: do it in place
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




