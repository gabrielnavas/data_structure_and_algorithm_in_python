class Node:
  def __init__(self, data):
    self.next = None
    self.data = data

class StackNode:
  def __init__(self):
    self.__head = None
    self.__size = 0

  def push(self, data: any):
    if(self.__head == None):
      self.__head = Node(data)
    else:
      newNode = Node(data)
      newNode.next = self.__head
      self.__head = newNode
    self.__size += 1
  
  def pop(self) -> any:
    node = self.__head
    self.__head = self.__head.next
    self.__size -= 1
    return node.data
  
  def isEmpty(self) -> bool:
    return self.__head == None
  
  def peek(self) -> any:
    return self.__head.data
    
  def size(self) -> int:
    return self.__size