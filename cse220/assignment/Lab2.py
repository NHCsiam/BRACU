#Task 1
class Node:
    
    def __init__(self,element,next):
        self.element=element
        self.next=next
        
    def printNode(self):
        print(self.element, end=',')
        
class Mylist:
    
    def __init__(self,a):
        self.head=None
        tail=None
        for i in a:
            n=Node(i,None)
            if self.head is None:
                self.head=n
                tail=n
            else:
                tail.next=n
                tail=n
# Task 2-(1a)
        self.a=[]
# Task 2-(1b)
        if isinstance(a, Mylist):
            self.head=None
            tail=None
            for i in a:
                n=Node(i,None)
                if self.head is None:
                    self.head=n
                    tail=n
                else:
                    tail.next=n
                    tail=n
# Task 2-(1c)                    
        elif isinstance(a, Mylist):
            self.head=None
            tail=None
            temp=a.head
            while temp is not None:
                node1=Node(temp.element,None)
                if self.head is None:
                    self.head=node1
                    tail=node1
                else:
                    tail.next=node1
                    tail=node1
                temp=temp.next
# Task 2-(2)     
    def showList(self):
        n=self.head
        if self.head is None:
            print('Empty list')
        else:
            while n!=None:
                print(n.element)
                n=n.next    
# Task 2-(3)     
    def isempty(self):
        if self.a is None:
            print("True")
        else:
            print("False")
# Task 2-(4)            
    def clear(self):
        if self.a is not None:
            self.a=None
        else:
            print("The list is empty")

#print mathod        
    def printlist(self):
        n=self.head
        while n!=None:
            n.printNode()
            n=n.next

#Task 2-(7)
    def remove(self, deletekey):
        n=self.head        
        while n!=None:
            if n.element==deletekey:
                print(n.element)               
                break
            prev=n
            n=n.next
        prev.next = n.next


#Advanced operations
# Task 3-(1)
    def Even(self):
        newList=[]
        n=self.head
        while n!=None:
            if n.element%2==0:
                newNode=Node(n.element,None)
                newList.append(newNode.element)
            
            n=n.next
        print(newList)

#Task 3-(2)
    def elementcheck(self,value):
        n=self.head
        while n!=None:
            if n.element==value:
                return True
            n=n.next
        return False

# Task 3-(3)            
    def reverseList1(self):    
        n =self.head
        polo=None        
        while(n is not None):    
            nextNode = n.next    
            n.next =polo    
            polo = n    
            n = nextNode    
        self.head=polo

#Task 3-(4)    
    def sort(self):
        n=self.head
        j=self.head
        while n!=None:
            while j!=None:
                if n.element<j.element:
                    temp=n.element
                    n.element=j.element
                    j.element=temp
                j=j.next
            j=self.head
            n=n.next
# Task 3-(5)    
    def sum1(self):
        n=self.head
        total=0
        while n!=None:
            total=total+n.element
            n=n.next
        print(total)



#test
list1=[1,3,2,5,4]
list2=Mylist(list1)

list2.sort()
#list2.printlist()
#list2.sort()
#list2.sum1()
#list2.printlist()
list2.showList()
