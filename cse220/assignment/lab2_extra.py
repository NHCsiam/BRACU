class Node:
    
    def __init__(self,element,next):
        self.element=element
        self.next=None
        
    def printNode(self):
        print(self.element, end=',')
        
class Mylist:
    
    def __init__(self,a):
        self.head=None
        self.tail=None
        for i in a:
            n=Node(i,None)
            if self.head is None:
                self.head=n
                self.tail=n
            else:
                self.tail.next=n
                self.tail=n
# Task 2-(1a)
        self.a=[]
# Task 2-(1b)
        if isinstance(a, Mylist):
            self.head=None
            self.tail=None
            for i in a:
                n=Node(i,None)
                if self.head is None:
                    self.head=n
                    self.tail=n
                else:
                    self.tail.next=n
                    self.tail=n
# Task 2-(1c)                    
        elif isinstance(a, Mylist):
            self.head=None
            self.tail=None
            temp=a.head
            while temp is not None:
                node1=Node(temp.element,None)
                if self.head is None:
                    self.head=node1
                    self.tail=node1
                else:
                    self.tail.next=node1
                    self.tail=node1
                temp=temp.next
    def showList(self):
        n=self.head
        if self.head is None:
            print('Empty list')
        else:
            while n!=None:
                print(n.element)
                n=n.next
#Task 2-(5)
    def insert(self,val):
        n=self.head
        new=Node(val,None)
        if self.head==None:
            self.head=new
        else:
            temp=self.head
            while temp!=self.tail:
                temp=temp.next
            temp.next=new
#Task 2-(6)
    def insert2(self,val,idx):
        n=self.head
        new=Node(val,None)
        if self.head==None:
            self.head=new
        else:
            pos=0
            temp=self.head
            while temp!=self.tail:
                if pos==idx:
                    break
                elif pos==idx-1:
                    break
                temp=temp.next
                pos+=1
            if pos==idx:
                self.head=new
                new.next=temp
            else:
                store=temp.next
                temp.next=new
                new.next=store
#Task 3-(6)
    def rotate(self,term,k):
        n=self.head
        c=1
        if term=="right":
            while c<k and n!=self.tail:
                n=n.next
                c+=1
            knode=n
            while n.next!=self.tail:
                n=n.next        
            n.next.next=self.head
            self.head=n
            knode.next.next=None
    
            


#tester
list1=[3,2,5,1,8]
list2=Mylist(list1)
list2.insert2(99,5)
list2.showList()
