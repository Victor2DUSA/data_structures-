class Node: 
    def __init__(self,value):
        self.value = value 
        self.next  = None 

class Queues: 
    def __init__(self, value): 
        new_node = Node(value)
        self.first = new_node
        self.last = new_node 
        self.length = 1

    def enqueue(self, value): 
        temp = Node(value)
        if self.first is not None:
            self.last.next =temp
            self.last = temp 
        else: 
            self.first = temp
            self.last = temp
        self.length += 1 

    
    def dequeue(self): 
        if self.length == 0: 
            return None
        
        temp = self.first
        if self.first == 1:
            self.first = None 
            self.last = None
        else: 
            self.first = self.first.next  
            temp.next = None
        self.length -=1

        return temp 


    def print_queue(self): 
        temp = self.first
        while temp is not None: 
            print(temp.value)
            temp = temp.next


my_queue = Queues(1)
my_queue.enqueue(2)
my_queue.print_queue()