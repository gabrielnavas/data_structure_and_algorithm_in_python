class StackWithArray:
  def __init__(self):
    self.__stack = []
  
  def push(self, element: any):
    self.__stack.append(element)
  
  def pop(self) -> any:
    return self.__stack.pop()
  
  def isEmpty(self) -> bool:
    return len(self.__stack)
  
  def peek(self) -> any:
    theLast = len(self.__stack)-1
    return self.__stack[theLast]

  def size(self) -> int:
    return len(self.__stack)