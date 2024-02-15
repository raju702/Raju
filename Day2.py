'''
count of nodes
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None
    def display(self):
        current=self.head
        while current !=None:
            print(current.data,end="->")
            current=current.next
        print("end")
    def count(self):
        count=0
        current=self.head
        while current!=None:
            count+=1
            current=current.next
        return count
ll=Linkedlist()
ll.head=Node(1)
n1=Node(3)
n2=Node(2)
n3=Node(6)
ll.head.next=n1
n1.next=n2
n2.next=n3
ll.display()
print(f"Number of nodes in the linked list are {ll.count()}")'''

#stack
class stack:
    def __init__(self):
        self.stack=[]
    def add(self,data):
        if data not in self.stack:
            self.stack.append(data)
            return True
        else:
            return False
    # def peek(self):
    #     return self.stack[-1]
    def pop(self):
        if len(self.stack)==0:
            print("stack is empty")
            return
        self.stack.remove(self.stack[-1])
    def display(self):
        if self.stack==[]:
            print("the stack is empty")
            return
        print("the stack elements are: ")
        for i in range(len(self.stack)-1,-1,-1):
            print(self.stack[i])


Stack=stack()
Stack.add(3)
Stack.add(4)
Stack.add("ram")
Stack.add("raju")
#print(Stack.peek())
#print(Stack.count())
#Stack.pop()
Stack .display()