from node import Node

class Stack:
  def __init__(self):
    self.head = None
    self.size = 0

  def push(self, data):
    if self.size == 0:
      self.head = Node(data)
    else:
      new_node = Node(data)
      new_node.next = self.head
      self.head = new_node

    self.size += 1

  def pop(self):
    if self.size == 0:
      raise Exception("Cannot pop from empty stack.")
    
    temp = self.head
    val = temp.data
    self.head = temp.next
    temp.next = None
    self.size -= 1

    return val

  def peek(self):
    if self.size == 0:
      raise Exception("Cannot peek into empty stack.")

    return self.head.data

  def get_size(self):
    return self.size

  # LK - what do you mean by avoid instantiating new data structure?
  # the original question said to mutate the existing stack. is this
  # something different?
  def fix_stack(self):
    if self.size == 0:
      raise Exception("Empty stack, nothing to fix.")
    if self.size == 1:
      raise Exception("Only one item, nothing to fix.")
    if self.size < 0:
      raise Exception("You gone fooked up.")
    if self.size >= 2:
      temp1 = self.head.next
      temp2 = self.head

      while temp1.next is not None:
        temp2 = temp1
        temp1 = temp1.next

      val1 = temp1.data
      val2 = temp2.data
      temp1.data = val2
      temp2.data = val1

# used to test
def fix_stack_test():
  myStack = Stack()
  print "size"
  print myStack.get_size()

  myStack.push(2)
  myStack.push(1)
  myStack.push(3)
  myStack.push(4)
  myStack.push(5)

  print "current stack"
  current = myStack.head
  for x in range(0, myStack.size):
    print current.data
    current = current.next

  myStack.fix_stack()

  print "fixed stack"
  current = myStack.head
  for x in range(0, myStack.size):
    print current.data
    current = current.next

  print "current stack"
  current = myStack.head
  for x in range(0, myStack.size):
    print current.data
    current = current.next

  print "popping"
  print myStack.pop()

  print "current stack"
  current = myStack.head
  for x in range(0, myStack.size):
    print current.data
    current = current.next

  print "popping"
  print myStack.pop()

  print "current stack"
  current = myStack.head
  for x in range(0, myStack.size):
    print current.data
    current = current.next

  print "peeking"
  print myStack.peek()

# fix_stack_test()

# return list of coins to return as change given paramters of array of coin denominations and amount given
# first try - assuming coins in order highest to smallest
def change(coins, amount):
  coins.sort()        # second try - coins don't need to be in order now
  coins.reverse()
  change_list = []

  index = 0
  while index < len(coins):
    while amount >= coins[index]:
      change_list.append(coins[index])
      amount -= coins[index]
    index += 1

  return change_list

print change([25, 10, 5, 1], 42)
print change([25, 5, 1], 42)
print change([25, 10, 1], 42)
print change([10, 1, 25, 5], 42)




