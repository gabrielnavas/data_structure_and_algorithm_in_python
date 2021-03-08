class Node:
  def __init__(self, data):
    self.left = None
    self.right = None
    self.data = data

class BinarySearchTree:
  def __init__(self):
    self._root = None
  
  def add(self, data):
    if(self._root == None):
      self._root = Node(data)
    else:
      node = self._root
      end = False
      while(end == False): 
        if(data < node.data):
          if(node.left == None):
            node.left = Node(data)
            end = True
          else:
            node = node.left
        else:
          if(node.right == None):
            node.right = Node(data)
            end = True
          else:
            node = node.right
    
  def inOrder(self): 
    def recInOrder(node: Node):
      if(node == None): return
      recInOrder(node.left)
      print(node.data)
      recInOrder(node.right)
    recInOrder(self._root)


t = BinarySearchTree()
t.add(10)
t.add(9)
t.add(5)
t.add(12)
t.add(11)
t.add(15)
t.inOrder()