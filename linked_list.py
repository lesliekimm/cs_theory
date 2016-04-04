from node import Node

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.count = 0

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

    current = self.head
    while current is not None:
      previous = current
      if current.next is not None:
        temp = current.next
        while temp is not None:
          if (temp.data == current.data):
            previous.next = temp.next
            if (temp is not self.tail):
              temp = temp.next
            else:
              self.tail = previous
              temp = temp.next
              previous = previous.next
            self.count -= 1
          else:
            temp = temp.next
            previous = previous.next
      current = current.next
    return

  # returns data of kth node from the end of the LL
  def kth_to_last(self, k):
    if self.is_empty():
      raise Exception("Nothing to return from an empty list.")
    if (k <= 0 or k > self.count):
      raise TypeError("Position k is out of bounds.")

    position_from_front = self.count - k + 1

    current = self.head
    
    for x in range(0, position_from_front - 1):
      current = current.next
    return current.data

  # delete the middle node given access only to that node
  def delete_middle_node(self, ptr):
    first_half = LinkedList()
    current = self.head

    while current is not ptr:
      first_half.insert(current.data)
      current = current.next

    second_half = LinkedList()
    second_half.head = ptr.next

    first_half.tail.next = second_half.head
    first_half.count = self.count - 1
    return first_half

  # returns data of kth node from the end of the LL using recursion
  # def kth_to_last_recursive(self, current, k):
  #   if self.is_empty():
  #     raise Exception("Nothing to return from an empty list.")
  #   if (k <= 0 or k > self.count):
  #     raise TypeError("Position k is out of bounds.")

  #   if current is None:
  #     raise TypeError("Position k is out of bounds.")

  #   if (k == 0):
  #     return current.data
  #   return self.kth_to_last_recusive(current.next, k - 1)      




  # create and insert new node at back of LL

  # create and insert node at position k in LL

  # remove kth node from back of LL

  # count number of elements in LL

  # find max, min, avg values of elements in LL

  # given LL, determine if it has a cycle in it. return the node where the cyle begins. return null if no cycle exists
  # can you solve it using constant extra space?

  # given an array of elements, create LL from array in same order

  # given unsorted array of elements, create a sorted LL by creating new node for each array element & inserting it into its appropriate position in list