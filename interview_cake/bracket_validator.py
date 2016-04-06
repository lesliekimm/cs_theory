# You're working with an intern that keeps coming to you
# with JavaScript code that won't run because the braces,
# brackets, and parentheses are off. To save you both some
# time,you decide to write a braces/brackets/parentheses
# validator.

# Let's say:
# '(', '{', '[' are called "openers."
# ')', '}', ']' are called "closers."

# Write an efficient function that tells us whether or not
# an input string's openers and closers are properly nested.

# Examples:
# "{ [ ] ( ) }" should return True
# "{ [ ( ] ) }" should return False
# "{ [ }" should return False

class Node:
  def __init__(self, data=None, next=None):
    self.data = data
    self.next = next

  def __str__(self):
    return str(self.data)

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

def validator(string):
  if len(string) == 0:
    raise Exception("Empty string.")

  opening = ['{', '[', '(']
  closing = ['}', ']', ')']
  bracketStack = Stack()
  
  string_chars = list(string)
  for x in range (len(string_chars)):
    if string_chars[x] in opening:
      bracketStack.push(string_chars[x])
    elif string_chars[x] in closing:
      if bracketStack.peek() == '{' and string_chars[x] == '}':
        bracketStack.pop()        
      elif bracketStack.peek() == '(' and string_chars[x] == ')':
        bracketStack.pop()
      elif bracketStack.peek() == '[' and string_chars[x] == ']':
        bracketStack.pop()
      else:
        return "False"

  if bracketStack.get_size() != 0:
    return "False"

  return "True"



print validator("{ [ ] ( ) }")            # True
print validator("{ [ ( ] ) }")            # False
print validator("{ [ }")                  # False
# print validator("")                     # Exception
print validator("{")                      # False
print validator("{ (")                    # False
print validator("{ [ ] ( ) } { } (_)")    # True
print validator("{{angular syntax}} ( ) ( [ : random ] stuff ) here { } ")    # True



