class Node: 
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList:
    def __init__(self, value):
       new_node = Node(value)
       self.head = new_node
       self.tail = new_node
       self.length = 1

num = int(input("Enter the value: "))
my_linked_list = LinkedList(num)

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)


"""
    EXPECTED OUTPUT:
    ----------------
    Head: the number you entered
    Tail: the number you entered
    Length: 1
    
"""

                                                                                                                    