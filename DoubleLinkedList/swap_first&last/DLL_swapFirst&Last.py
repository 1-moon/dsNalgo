class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    # WRITE SWAP_FIRST_LAST METHOD HERE #
    def swap_first_last(self):
        # ======== change the value and structure as well =========
        # if not self.head or not self.head.next:
        #     return False 
          
        # first = self.head 
        # last = self.tail 
        
        # if self.length == 2:
        #     temp = first 
        #     temp.next = None 
        #     # swap first node with last node 
        #     first = last 
        #     first.prev = None 
        #     self.head = first 
            
        #     # allocate last to tail 
        #     last = temp 
        #     self.tail = last 
        #     # sort out pointers on both nodes
        #     first.next = last 
        #     last.prev = first 
        #     return True 
            
        # # cut off the connection between first and second nodes of list 
        # second = first.next 
        # first.next = None
        # second.prev = None 
        
        # # cut off the connection between last and second_last nodes of list 
        # second_last = last.prev 
        # last_prev = None 
        # second_last.next = None 
        
        # # swap first and last 
        # temp = first 
        # first = last 
        # last = temp 
        
        # # connect 
        # first.next = second 
        # second.prev = first 
        # last.prev = second_last
        # second_last.next = last 
        
        # # allocate head&tail to fist&tail 
        # self.head = first 
        # self.tail = last 
        # return True 
        
        # ========= only change the value ===========
        # 1. Check if the doubly linked list is empty or has only one node. 
        # If so, there's nothing to swap, hence exit the function early.
        if self.head is None or self.head == self.tail:
            return
        
        # 2. If the list has more than one node, swap the values of the 
        # head (first node) and tail (last node).
        # Note: We're only exchanging the data stored in the nodes, 
        # rather than altering the structure of the linked list itself.
        self.head.value, self.tail.value = self.tail.value, self.head.value
        
    

my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)


print('DLL before swap_first_last():')
my_doubly_linked_list.print_list()


my_doubly_linked_list.swap_first_last()


print('\nDLL after swap_first_last():')
my_doubly_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    DLL before swap_first_last():
    1
    2
    3
    4

    DLL after swap_first_last():
    4
    2
    3
    1

"""

