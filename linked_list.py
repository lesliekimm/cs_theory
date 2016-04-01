from node import Node

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.count = 0

  # create and insert a new node at front of LL
  def insert(self, data):
    if self.is_empty():
      self.head = Node(data)
      self.tail = self.head
    else:
      self.tail.next = Node(data)
      self.tail = self.tail.next

    self.count += 1
    return

  # remove kth node from front of LL
  def remove(self, index):
    if self.is_empty():
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
    return

  # remove duplicate nodes
  def remove_dup(self):
    if self.is_empty():
      raise Exception("Cannot remove duplicates from an empty list.")
    
    current = self.head
    dups = {}

    dups[current.data] = True
    previous = current
    current = current.next

    while current is not None:
      if dups.has_key(current.data):
        previous.next = current.next
        if current.next is None:
          self.tail = previous
          current = None
        else:
          current = current.next
        self.count -= 1
      else:
        dups[current.data] = True
        previous = current
        current = current.next
    return

  # remove duplicate nodes without a buffer
  def remove_dup_no_buffer(self):
    if self.is_empty():
      raise Exception("Cannot remove duplicates from an empty list.")

    # current = self.head
    return

  # returns number of nodes in LL
  def get_count(self):
    return self.count

  # check to see if LL is empty or not
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
    return

  # create and insert new node at back of LL

  # create and insert node at position k in LL

  # remove kth node from back of LL

  # count number of elements in LL

  # find max, min, avg values of elements in LL

  # given LL, determine if it has a cycle in it. return the node where the cyle begins. return null if no cycle exists
  # can you solve it using constant extra space?

  # given an array of elements, create LL from array in same order

  # given unsorted array of elements, create a sorted LL by creating new node for each array element & inserting it into its appropriate position in list