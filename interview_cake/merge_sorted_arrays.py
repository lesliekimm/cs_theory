# In order to win the prize for most cookies sold, my friend Alice and I
# are going to merge our Girl Scout Cookies orders and enter as one unit.
# Each order is represented by an "order id" (an integer).

# We have our lists of orders sorted numerically already, in lists. Write
# a function to merge our lists of orders into one sorted list.

# For example:
# my_list     = [3, 4, 6, 10, 11, 15]
# alices_list = [1, 5, 8, 12, 14, 19]

def merge_lists(list1, list2):
  merged = []

  index1 = 0
  index2 = 0

  while index1 < len(list1) or index2 < len(list2):
    if index1 != len(list1) and index2 != len(list2):
      if list1[index1] < list2[index2]:
        merged.append(list1[index1])
        index1 += 1
      elif list1[index1] == list2[index2]:
        merged.append(list1[index1])
        merged.append(list2[index2])
        index1 += 1
        index2 += 1
      else:
        merged.append(list2[index2])
        index2 += 1
    elif index1 == len(list1) and index2 != len(list2):
      while index2 != len(list2):
        merged.append(list2[index2])
        index2 += 1
    else:
      while index1 != len(list1):
        merged.append(list1[index1])
        index1 += 1

  return merged


my_list = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]
# prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
# print merge_lists(my_list, alices_list)

def merge_lists_constant_space(list1, list2):
  merged = list1


  return merged



my_list = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]
# prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
print merge_lists_constant_space(my_list, alices_list)
