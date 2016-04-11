import re

# 1.1 - Determine if a string has all unique characters
def is_unique(strng):
  chars = {}
  for c in strng:
    if c in chars.keys():
      return False
    else:
      chars[c] = 1
  return True

def test_is_unique():
  print is_unique("try")
  print is_unique("call")
  print is_unique("beauty")
  print is_unique("computer")
  print is_unique("free")
  print is_unique("")

# test_is_unique()

# 1.1 - Without using another data structure
def is_unique_wo_other_data_structure(strng):
  for i1 in range(len(strng)):
    for i2 in range(i1+1, len(strng)):
      if strng[i1] == strng[i2]:
        return False
  return True

def test_is_unique_wo_other_data_structure():
  print is_unique_wo_other_data_structure("try")
  print is_unique_wo_other_data_structure("call")
  print is_unique_wo_other_data_structure("beauty")
  print is_unique_wo_other_data_structure("computer")
  print is_unique_wo_other_data_structure("free")
  print is_unique_wo_other_data_structure("")

# test_is_unique_wo_other_data_structure()

# 1.2 - Given two strings, decide if one is a permutation of the other
def check_permutation(str1, str2):
  if str1 == "" and str2 == "":
    return True
  if (str1 == "" and str2 != "") or (str1 !="" and str2 == ""):
    return False

  all_perms = perm(str1)

  if str2 in all_perms:
    return True

  return False

def perm(strng):
  if len(strng) == 0:
    return [""]
  else:
    prev_s = perm(strng[1:])
    res_s = []
    for i in range(0, len(prev_s)):
      for j in range (0, len(strng)):
        new_s = prev_s[i][0:j] + strng[0] + prev_s[i][j:len(strng) - 1]
        if new_s not in res_s:
          res_s.append(new_s)
  return res_s

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

  rx = re.compile('[^a-z][0-9]')
  strng = rx.sub('', strng)
  print strng

  if len(strng) == 0:
    raise Exception("Empty string")

  index = 0
  while index < len(strng)/2:
    if strng[index] != strng[len(strng) - index - 1]:
      return False
    index += 1

  return True

def palindrome_permutation(strng):
  return False

def test_is_palindrome():
  # print is_palindrome("Hanah")                            # True
  # print is_palindrome("Sara")                             # False
  print is_palindrome("A dog, a plan, a canal: pagoda.")  # True
  # print is_palindrome("")                                 # Exception
  # print is_palindrome("a")                                # True
  # print is_palindrome("ab")                               # False
  # print is_palindrome("aa")                               # True
  # print is_palindrome("Otto sees Otto.")                  # True
  print is_palindrome("Otto 3.sees Otto.")                 # True


def test_palindrome_permutation():
  print palindrome_permutation("Tact Coa")  # True
  print palindrome_permutation("booger")    # False
  print palindrome_permutation("bear ear")  # True
  print palindrome_permutation("")          # False

test_is_palindrome()
# test_palindrome_permutation()

