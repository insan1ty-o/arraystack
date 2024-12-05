# Your Code & Heading go Here!
# Matthew Fahnestock
# U4 L1
# Creating a Stack Class

class ArrayStack():
  def __init__(self):
    self.__stack = []
    self.__size = 0


  def __is_empty(self):
    "Checks if the stack is empty, and returns true if so."
    if self.__size > 0:
      return True
    else:
      return False

  def push(self, element):
    "Pushes new element to stack"
    self.__stack.append(element)
    self.__size += 1

  def pop(self):
    "Removes top element in stack"
    check = self.__is_empty()
    if check != False:
      ele = self.__stack[-1]
      del self.__stack[-1]
      self.__size -= 1
      return ele
    else:
      raise IndexError("no element to delete in stack")

  def top(self):
    "Returns the current top element in stack"
    check = self.__is_empty()
    if check != False:
      return self.__stack[-1]
    else:
      raise IndexError("no top element available in stack")
   


  def __len__(self):
    "Returns size of stack"
    return self.__size
  def __str__(self):
    """Display contents of stack"""
    out = ""
    for ele in self.__stack:
        out += str(ele) + ' '

    out += "<TOP"
    return out