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