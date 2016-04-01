from node import Node

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.count = 0

  # create and insert a new node at front of LL
  def insert(self, data):
    if (self.count == 0):
      self.head = Node(data)
      self.tail = self.head
    else:
      self.tail.next = Node(data)
      self.tail = self.tail.next

    self.count += 1

  # remove kth node from front of LL
  def remove(self, index):
    if (self.count == 0):
      raise Exception("Cannot remove element from empty list.")
    if (index < 0 or index >= self.count):
      raise TypeError("Index is out of bounds.")

    if (self.count == 1 and index == 0):
      self.head = None
      self.tail = None
    elif (index == 0):
      self.head = self.head.next
    else:
      current = self.head
      for x in range (0, index - 1):
        current = current.next

      if (current.next.next is None):
        self.tail = current
        current.next = None
      else:
        current.next = current.next.next

    self.count -= 1

  def remove_dup(self):
    if (self.count == 0):
      raise Exception("Cannot remove duplicates from an empty list.")
    



  # chekcs to see if LL is empty or not
  def is_empty(self):
    if (self.count == 0):
      return True
    return False

  # print list
  def print_list(self):
    current = self.head
    while current is not None:
      print current
      current = current.next

  # create and insert new node at back of LL

  # create and insert node at position k in LL

  # remove kth node from back of LL

  # count number of elements in LL

  # find max, min, avg values of elements in LL

  # given LL, determine if it has a cycle in it. return the node where the cyle begins. return null if no cycle exists
  # can you solve it using constant extra space?

  # given an array of elements, create LL from array in same order

  # given unsorted array of elements, create a sorted LL by creating new node for each array element & inserting it into its appropriate position in list