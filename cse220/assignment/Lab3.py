# task 1

class Node:
    def __init__(self,elem):
        self.element=elem
        self.next=None
        self.prev=None


class DoublyList:
    head=Node(None)
#task2{1}
    def __init__(self,a):
        if a==None:
            print("Array cannot be empty")
        else:
            tail = DoublyList.head
            for i in a:
                temp=Node(i)
                tail.next=temp
                temp.prev=tail
                tail = tail.next
#task2
    def showList(self):
        n=self.head
        if self.head is None:
            print('Empty list')
        else:
            while n!=None:
                print(n.element," -> ",end='')
                n=n.next
#task 3
    def insert(self,newElement):
        n=self.head.next
        new=Node(newElement)
        if self.head.next==None:
            self.head.next=new
        else:
            temp=self.head.next
            while temp.next!=self.head:
                temp=temp.next
            temp.next=new
            new.next=self.head
            new.prev=temp
            self.head.prev=new
#task 4
    def insert2(self,newElement,index):
        n=self.head.next
        new=Node(newElement)
        if self.head.next==None:
            self.head.next=new
        else:
            pos=0
            temp1=self.head.next
            while temp1.next!=self.head:
                if pos==index-1:
                    break
                temp1=temp1.next
                pos+=1
            temp=temp1.next
            new.next=temp1.next
            new.prev=temp1
            temp1.next=new
            temp.prev=new
#Task 5
    def remove(self,index):
        n=self.head.next
        if self.head==None:
            print("Empty")
        else:
            pos=0
            while n!=self.head:
                if pos==index:
                    n.prev.next=n.next
                    n.next.prev=n.prev
                    n.next=None
                    n.prev=None
                    break 
                pos+=1
                n=n.next
# task 6
    def removekey(self, deletekey):
        n=self.head.next 
        while n!=self.head:
            if n.element==deletekey:
                n.prev.next=n.next
                n.next.prev=n.prev
                n.next=None
                n.prev=None
                return            
            n=n.next
    
    





        

list1=[1,3,2,5,4]
list2=DoublyList(list1)
list2.removekey(2)
list2.showList()
list2.insert2(9,2)
list2.showList()
list2.remove(2)
list2.showList()
#list2.insert(90)
list2.showList()
