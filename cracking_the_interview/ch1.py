# Interview Question 1.1 - Determine if a string has all unique characters
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

test_is_unique()

# Interview Question 1.1 - Without using another data structure
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

test_is_unique_wo_other_data_structure()