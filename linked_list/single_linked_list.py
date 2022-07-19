"Big O  for linked list"

"Appending = O(1)"

"moving element = O(n)"
"Adding from the front of the list = O(1)"
"Romving front of list = O(1)"
"Adding in the middle of the list = O(n)"
"Removing from the middle of the list = O(n)"
"Look up = O(n)"

"linked list as a dictionery "

head = {
    "value":11,
    "next": {
        "value": 3, 
        "next": {
            "value": 23,
            "next": {
                "value": 7,
                "next": None
            }
        }
    }
}

# print(head['next']['next']['value'])

class Node: 
    def __init__(self,value): 
        self.value = value
        self.next = None 


class LinkedList: 
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1  
    
    def append(self,value): 
        new_node = Node(value)
        if self.head == 0: 
            self.head = new_node
            self.tail = new_node 
        
        else: 
            self.tail.next = new_node
            self.tail = new_node
        
        self.length += 1 
        return True 

    def prepend(self, value):
        new_node = Node(value)

        if self.length == 0: 
            self.head = new_node
            self.tail = new_node
        else: 
            new_node.next =self.head
            self.head = new_node 
        self.length += 1
        return True


    
        
    

    def pop_first(self): 
        if self.length == 0:
            return None  
        temp = self.head
        self.head = self.head.next
        temp.next = None 
        self.length -= 1
        if self.length == 0: 
            self.tail = None

        return temp  


    def pop(self): 
        if self.length == 0: 
            return None
        temp = self.head
        pre = self.head

        while temp.next: 
            pre = temp
            temp = temp.next
        
        self.tail = pre
        self.tail.next = None
        self.length -= 1 
        if self.length == 0:
            self.head = None 
            self.tail = None 
        
        return temp 

    def get(self, index):
        if index < 0 or index >= self.length: 
            return None 
        
        temp = self.head 
        for _ in range(index): 
            temp = temp.next 
        return temp 
    

    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return False
        if index == 0: 
            return self.prepend(value)
        if index  == self.length:
            return self.append(value)

        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next  = new_node
        self.length += 1 
        return True

    def remove(self,index,):
        if index < 0 or index >= self.length:
            return None 

        if index == 0:
            return self.pop_first()
        
        if index == self.length-1: 
            return self.pop()
        
        prev = self.get(index-1)
        temp = prev.next
        temp.next = None 
        self.length -= 1 
        return temp  


    def set_value(self, index, value):
        temp = self.get(index)
        if temp: 
            temp.value = value 
            return True 
        return False 
        # if index < 0 or index >= self.length:
        #     return None 
        # temp = self.head
        # for i in range(index):
        #     temp = temp.next
        #     if  i == index-1: 
        #         temp.value = value
        # return True 

    def reverse(self): 
        temp = self.head
        self.head = self.tail
        self.tail = temp 
        after = temp.next
        before = None 

        for _ in range(self.length): 
            after = temp.next
            temp.next = before 
            before = temp 
            temp = after 


    def print_list(self): 
        temp = self.head
        while temp is not None: 
            print(temp.value)
            temp = temp.next


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
# my_linked_list.print_list()
my_linked_list.append(4)
my_linked_list.print_list() 

print(my_linked_list.reverse())  
my_linked_list.print_list() 

# print(my_linked_list.pop())

# print(my_linked_list.pop())



# print(my_linked_list.tail.value)

# print(my_linked_list.pop_first())

# print(my_linked_list.pop_first())

# print(my_linked_list.pop_first())
# print(my_linked_list.pop_first())