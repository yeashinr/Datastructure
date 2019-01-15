class Node:

    def __init__(self,value = None):
        self.value = value
        self.next = None

class Linkedlist:

    def __init__(self):
        self.head = Node()
        

    def display_list(self):

        if self.head == None:
            print("List is empty")
        else:
            pointer = self.head
            while pointer.next != None:
                print(pointer.value,"->")
                pointer = pointer.next

    
    def count_nodes(self):
        count = 0
        pointer = self.head
        while pointer.next != None:
            count +=1
            pointer = pointer.next
       # print("Number of nodes:", count)
        
    
    def search(self,x):
        pointer = self.head
        position = 1

        while pointer is not None:
            if pointer.value == x:
                print(x , "is found at: ", position)
                return True
            pointer = pointer.next
            position +=1
        else:
            print(x, "is not found")
            return False

    def insert_at_head(self,data):
        if self.head != None:
            node = Node(data)
            node.next = self.head
            self.head = node
        

    def insert_at_tail(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            node = Node(data)
            pointer = self.head
            while pointer.next != None:
                pointer = pointer.next
            pointer.next = node
           
    
    def creat_list(self):
        n = input("Please enter the number of list wanted to create: ")

        for x in range(n):
            data = input("Please enter the data to be inserted: ")
            self.insert_at_tail(data)
    
    def insert_after(self,data,position):
        pos = 1
        pointer = self.head

        while pointer is not None:
            if pos == position:
                node = Node(data)
                node.next = pointer.next
                pointer.next = node
                break
            pos +=1
        self.head = Node(data)

    
    def insert_before(self,data,position):
        pos = 2
        pointer = self.head
        previous = pointer


        if 0 < position <= self.count_nodes:

            if position == 1:
                self.insert_at_head(data)
            else:
                while pos != position:
                    previous = pointer
                    pointer = pointer.next
                    pos += 1
                else:
                    node = Node(data)
                    previous.next = node
                    node.next = pointer

                
                    
    
    def insert_at_position(self,data,position):
        
        if position == 1:
            node = Node(data)
            node.next = self.head
            self.head = node
            return
        pointer = self.head
        pos = 1

        while pos < position - 1 and pointer.next is not None:
            pointer = pointer.next
            pos +=1
        
        if pointer is None:
            print("You can only insert upto position ",pos)
        else:
            node = Node(data)
            node.next = pointer.next
            pointer.next = node
 


    def delete_node(self, position):
        pass
        
    
    def delete_first_node(self):
        if self.head != None:
            self.head = self.head.next

    def delete_last_node(self):
    
        if self.head != None:
            pointer = self.head
            while pointer.next != None:
                pointer = pointer.next
            pointer = None
    
    def reverse_list(self):
        pass 

    def bubble_sort_exdata(self):
        pass

    def bubble_sort_exlinks(self):
        pass

    def has_cycle(self):
        pass

    def find_cycle(self):
        pass
    
    def remove_cycle(self):
        pass
    
    def insert_cycle(self):
        pass
    
    def merge2 (self,list):
        pass
    
    def _merge2(self,p1,p2):
        pass
    
    def merge_sort(self):
        pass
    
    def _merge_sort_rec(self,listStart):
        pass
    
    def _divide_list(self,p):
        pass

    
lst = Linkedlist()