class Node:
    def __init__(self,ele):
        self.element=ele
        self.next=None
        self.prev=None

class linkedList:
    head=Node(None)
    head.next=head.prev=head
    def __init__(self):
        n=Node("hola",None,None)
        n.next=self.head.next
        n.prev=self.head
        self.head.next=n
        n.next=n
        n.prev=n
        
        #iteration
        #forward
        n=self.head.next
        while n is not self.head:
            n=n.next
        #backward
        n=self.head.prev
        while n!=self.head:
            n=n.prev
    
    def insert(self,p,elem):
        n=Node(elem,None,None)
        q=p.next
        n.next=q
        n.prev=p
        p.next=n
        q.prev=n
        return n

    def remove(self,n):
        p=n.prev
        q=n.next
        p.next=q
        q.prev=p
        n.next=None
        n.prev=None
        n.element=None

li1=[1,2,3,4,5]
li2=linkedList(li1)
li2.insert()





