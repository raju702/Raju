
# #find min value without using builtin functions?

#Logic 1
# numList=list(map(input().split()))
# a=[1,2,3,4,5,6,67]
# min =a[0]

# for i in range(len(a)):
#     if min >a[i]:
#         min=a
# print(min)

# Logic 2
# min =numList[0]
# for i in numList:
#     if min > i:
#         min=i
# print("Logic 2:",min)

'''
# implementing linked list
class Node:
    
    def __init__(self,data):
        self.data=data
        self.next=None
    
class LinkedList:
    count=0
    def __init__(self):
        self.head=None

    def display(self,count):
        current=self.head
        while(current !=None):
            print(current.data,end=" -> ")
            current=current.next
        print("END")


SLL1=LinkedList()
SLL1.head=Node(20)
n2=Node(60)
n3=Node(80)
n4=Node(13)
SLL1.head.next=n2
SLL1.head.next.next=n3
n3.next=n4
SLL1.display()  
'''
# LinkedList Operations
# 1) Insertion
# 2) Append
# 3) Delete a node with given key value
# 4) Search a node with the given key value

'''    
class LinkedList:
    def __init__(self):
        self.head=None

    def isEmpty(self):
        return self.head is None

    def append(self,data):
        new_node = Node(data)
        
        if self.isEmpty():
            self.head = new_node
            return
        current=self.head

    def display(self,):
        current=self.head
        while(current !=None):
            print(current.data,end=" -> ")
            current=current.next
        print("END")
        '''


# SLL1=LinkedList()
# SLL1.head=Node(12)
# n2=Node(50)
# n3=Node(89)
# SLL1.head.next=n2
# SLL1.head.next.next=n3
# SLL1.display()

#insert in middle
# def insertAtIndex(self,data,index):
#     new_node=Node(data)
#     current_node=self.head
#     position=0
#     if position==index:
#         self.insertAtBegin



#print the LinkedList in Reverse Order

#wrirte a program to find the count of nodes present in the linkedlist?

#how to delete the last nodes from LinkedList

# current=self.head
# while(current.next !=None):
#     current=current.next
# current.next=None

# #how to delete the first nodes from LinkedList

# first_node=head
# head=first_node.next
# first_node.next=None
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        def push(self, data):
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

        # Printing elements of Linked List
        def print_ll(self):
            temp = self.head
            while (temp):
                print(temp.data),
                temp = temp.next

        # Insertion at beginning of LL
        def insert_at_beggining(self, item):
            new_node = Node(item)
            new_node.next = self.head
            self.head = new_node

        # Count number of nodes in Linked List
        def count_nodes(self):
            count = 0
            currNode = self.head
            while currNode is not None: count += 1; currNode = currNode.next
            return count
        '''

''''
        Delete the first n nodes from a linked list. If there are less than n nodes in the linked list, delete all of them.
        Delete the first n nodes from a linked list. If there are less than n nodes in the list, delete all of them.
        Delete the first node from linked list and return head pointer after deletion.
        If no node is present then it should return None.
        
        global first_node
        if self.count_nodes() == 0 : return None
        else:                       return self.delete_node(first_node).data

        # Delete a node from the Linked List
        @staticmethod
        def delete_node(node):
            global first_node
            if first_node is None or node is None: return None
            if node.next is None: first_node = None
            else: first_node = node.next
            node.next = None
            return first_node

# Test code
if __name__ == "__main__":
    ll = LinkedList()
    
    # Inserting elements to the Linked List

'''
'''
# print the linkedlist in reverse
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("END")

    def printrev(self, temp):
        if temp is None:
            return
        self.printrev(temp.next)
        print(temp.data, end=" -> ")

SLL1 = LinkedList()
SLL1.head = Node(20)
n2 = Node(60)
n3 = Node(80)
n4 = Node(13)
SLL1.head.next = n2
n2.next = n3
n3.next = n4
SLL1.display()
print("\nReverse of SLL is :\n")
SLL1.printrev(SLL1.head)'''

# Head recurssion and tail recurssion 

'''
# Double LinkedList
def addNode(self,data):
    newNode=Node(data);
    if (self.head==None):
        self.head=self.tail=newNode;
        self.head.previous=None;
        self.tail.next=None;
    else:
        self.tail.next=newNode;
        newNode.previous=self.tail;
        self.tail=newNode;
        self.tail.next=None;
def display(self):
    current=self.head;
    if (self.head==None):
        print("List is Empty")
        return;
    print("Nodes od double linked list :")
    while(current!=None):
        print(current.data)
        current=current.next

a1=addNode(5)
a2=addNode(15)
a3=addNode(51)
display()'''
'''
#search a node in circular linked list
# flag
def find(self,key):
    temp=self.head
    f=0
    if self.head is None:
        print("List is empty")
    else:
        while True:
            if temp.data==key:
                print(key,"found")
                f=1
                break
            temp = temp.next
            if temp == self.head:   #checking for the last node
                break 
        if f==0:                     #if key not found in the list
            print(key,"Element Not Found")
'''

#python program to substract smaller valued list from linkedlist?

# create a 2 linked lists, list1 input :1,0,0,end and list2 input :1,end and the output values should be concatenate of both lists and 
# convert into integers, select the a small value from lists substract the smaller value from lists andconvert the out put into linkedlist 
# and return the output?
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self,data):
        new_node = Node(data)        
        if self.head is None:
            self.head = new_node
            return 
        
        current = self.head
        while(current.next!=None):
            current = current.next
            
        current.next = new_node
    
    def display(self):
        current = self.head
        while current != None:
            print(current.data,end=" -> ")
            current = current.next
        print("NULL")
    
    
def LLtoNum(lList):
    #lList = 1 -> 0 -> 0
    num = ""
    temp = lList.head
    while(temp != None):
        num += str(temp.data)
        temp = temp.next
    return int(num)
        
def numToLL(num):
    resLL = LinkedList()
    for i in str(num):
        resLL.append(i)
    
    return resLL    

num1List = list(map(int,input().split()))
num2List = list(map(int,input().split()))
LL1 = LinkedList()
LL2 = LinkedList()

for i in num1List:
    LL1.append(i)
    
LL1.display()    
    
for i in num2List:
    LL2.append(i)
LL1.display()

num1 = LLtoNum(LL1)
num2 = LLtoNum(LL2)
if num1 > num2:
    result = num1 - num2
else:
    result = num2 - num1
    
resLinkedList = numToLL(result)

resLinkedList.display() '''

'''
#Example
class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("END")
    
    def count_nodes(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

SLL1 = LinkedList()
SLL1.head = Node(20)
n2 = Node(60)
n3 = Node(80)
n4 = Node(13)
SLL1.head.next = n2
n2.next = n3
n3.next = n4

print("Number of nodes in the list:", SLL1.count_nodes()) '''
'''
# stack using python using linked list
class stack:
    def __init__(self):
        self.stack=[]
    def add(self,datavalue):
    #use list append method to add element
        if datavalue not in self.stack:
            self.stack.append(datavalue)
            return True
        else:
            return False
    #use peek to look at the top of the stack
    def peek(self):
        return self.stack[-1]
AStack=stack()
AStack.add("mon")
AStack.add("tue")
AStack.peek()
print(AStack.peek())
AStack.add("wed")
AStack.add("thu")
print(AStack.peek()) '''

'''
#POP stack
class stack:
    def __init__(self):
        self.stack=[]
    def add(self,datavalue):
    #use list append method to add element
        if datavalue not in self.stack:
            self.stack.append(datavalue)
            return True
        else:
            return False
    #use peek to look at the top of the stack
    def peek(self):
        return self.stack[-1]
    
    def pop(self):
        #if self.stack[-1]:
        if len(self.stack)==0:
            print("stack is empty")
            return
        self.stack.remove(self.stack[-1])
        #self.stack.remove(self.stack.index(self.stack[-1]))
        #self.stack.pop()

    def display(self):
        if self.stack==[]:
            print("The Stack is Empty.")
            return
        print("The Stack elements are: ")
        for i in range(len(self.stack)-1,-1,-1):
            print(self.stack[i])

AStack=stack()
AStack.add("mon")
AStack.add("tue")
AStack.peek()
print(AStack.peek())
AStack.add("wed")
AStack.add("thu")
print(AStack.peek())
print("poping AN element now: ")
AStack.pop()
print(AStack.peek())
AStack.display() '''

#"Reverse a string using stack"

class stack:
    def __init__(self):
        self.stack=[]
    def push(self,datavalue):
    #use list append method to add element
        self.stack.append(datavalue)
        
    #use peek to look at the top of the stack
    def peek(self):
        return self.stack[-1]
    def pop(self):
        if len(self.stack) == 0 :
            print("stack is empty")
            return
        topElement=self.peek()
        self.peek()
        self.stack.remove(self.stack[-1])
        return topElement
    def display(self):
        if  len(self.stack)==[]:
            print("stack is empty")
            return
        for i in range(len(self.stack)-1,-1,-1):
            print(self.stack[i],end='')
        print()
    def reverse(self):
        resData=''
        length=len(self.stack)
        for i in range(length):
            resData+=Stack.pop()
        return resData

data=input()
Stack=stack()
for i in data:
    Stack.push(i)
Stack.display()
Stack.reverse() 
Stack.display()
#Application of Queue Data structure
'''
class  Queue:
    def __init__(self):
        self.queue=list()
    def addtoq(self,dataval):
        #insert method to add element to queue
        if dataval not in self.queue:
            self.queue.insert(0,dataval)
            return True
        return False
    def size(self):
        return len(self.queue)
thequeue=Queue()
thequeue.addtoq("mon")
thequeue.addtoq("tue")
thequeue.addtoq("wed")
print(thequeue.size()) '''

'''
#enqueue
class  Queue:
    def __init__(self):
        self.queue=list()
    def enqueue(self,data):
        self.queue.append(data)
    def size(self):
        return len(self.queue)
Q1=Queue()
n=int(input("enter the size of the queue"))
for i in range(n):
    Q1.enqueue(input())
print("The elements are inserted into the queue",Q1.queue)
print("Size of the queue is ",Q1.size()) '''

'''
#Dequeue
class  Queue:
    def __init__(self):
        self.queue=list()
    def enqueue(self,data):
        self.queue.append(data)
    def size(self):
        return len(self.queue)
    def dequeue(self):
        if self.queue is None:
            print("queue is empty")
            return
        return self.queue.pop(0)


Q1=Queue()
n=int(input("enter the size of the queue"))
for i in range(n):
    Q1.enqueue(input())
print("The elements are inserted into the queue",Q1.queue)
print("Size of the queue is: ",Q1.size())
Q1.dequeue()
# print("The elements are inserted into the queue",Q1.queue)
# print("Size of the queue is: ",Q1.size()) '''

'''
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def size(self):
        return len(self.queue)

    def dequeue(self):
        if self.size() == 0:
            print("Queue is empty")
            return None
        return self.queue.pop(0)


if __name__ == "__main__":
    Q1 = Queue()
    n = int(input("Enter the size of the queue: "))
    for i in range(n):
        data = input("Enter data for queue: ")
        Q1.enqueue(data)

    print("The elements inserted into the queue:", Q1.queue)
    print("Size of the queue is:", Q1.size())

    Q1.dequeue()
    print("The elements are inserted into the queue",Q1.queue)
    print("Size of the queue is: ",Q1.size()) '''

#check the given expersion is balanced or not

'''
#Priority Queue
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.front=None
        self.rare=None
    def enqueue(self,data):
        new_node=Node(data)
        if self.front is None and self.rare is None:
            self.front=new_node
            self.rare=new_node
            return
        self.rare.next=new_node
        new_node.next=new_node
    def dequeue(self):
        if self.front is None and self.rare is None:
            print("Queue is empty")
            return
        first_node=self.front
        self.front=self.front.next
        first_node.next=None
        return first_node  '''