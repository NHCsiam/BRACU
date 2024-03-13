#Task 1
def selection_sort(a,i,j):
    l=len(a)
    if i==l and j==l:
        return -1
    if i<l-1:
        min=i
        for j in range(i+2,l):
            if a[j]<a[min]:
                min=j
        if min!=i:
            temp=a[i]
            a[i]=a[min]
            a[min]=temp
        selection_sort(a,i+1,i+2)        
#task 1
A=[13,25,0,-4,7,-1,18,9,-6,21]
i=0
j=i+1
selection_sort(A,i,j)
print(A)


#Task 2
def insertion_sort(a,i):
    l=len(a)
    if i==l:
        return -1
    if i<l:     
        for j in range (i-1,-1,-1):
            if a[j]>a[j+1]:
                t=a[j+1]
                a[j+1]=a[j]
                a[j]=t
            else:
                break
        insertion_sort(a, i+1)
#task 2
p=[22,5,14,2,7,1]
i=1
insertion_sort(p,i)
print(p)


#linked list
class Node:
    
    def __init__(self,element,next):
        self.element=element
        self.next=next
        
    def printNode(self):
        print(self.element, end=',')
        
class LinkedList:
    
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
    
    def printlist(self):
        n=self.head
        while n!=None:
            n.printNode()
            n=n.next
#Task 3    
    def bubble_sort(self):
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



#Task 4    
    def selection_sort(self):

        n=self.head
        while n!=None:
            min=n.element
            min_id=n
            j=n
            while j!=None:
                if (j.element<min):
                    min=j.element
                    min_id=j
                j=j.next
            temp=min_id.element
            min_id.element=n.element
            n.element=temp
            n=n.next

#task3
list1=[13,25,0,-4,7,-1,18,9,-6,21]
list2=LinkedList(list1)
list2.bubble_sort()
list2.printlist()

#task 4
list3=[13,25,0,-4,7,-1,18,9,-6,21]
list4=LinkedList(list3)
list4.selection_sort()
list4.printlist()

#Doubly list
class Node1:
    def __init__(self,elem):
        self.element=elem
        self.next=None
        self.prev=None
    def printNode1(self):
        print(self.element, end=',')


class DoublyList:
    

    def __init__(self,a):
        self.head=None
        self.tail=None
        if a==None:
            print("Array cannot be empty")
        else:
            for i in a:
                temp=Node1(i)
                if self.head==None:
                    self.head=temp
                    self.tail=temp
                else:
                    self.tail.next=temp
                    temp.prev=self.tail
                    self.tail = temp
    
    def printlist(self):
        n=self.head
        while n!=None:
            n.printNode1()
            n=n.next

#Task 5
    def insertion_sort(self):
        n=self.head        
        while n!=None:
            pre=self.tail
            while pre!=self.head:
                if pre.prev.element>pre.element:
                    temp=pre.element
                    pre.element=pre.prev.element
                    pre.prev.element=temp                
                else:
                    pre=pre.prev
            n=n.next

#task 5
list5=[13,25,0,-4,7,-1,18,9,-6,21]
list6=DoublyList(list5)
list6.insertion_sort()
list6.printlist()

#Task 6
def binarySearch (A,val,L,R):
    if L>R:
        return -1
    else:
        mid=(L+R)//2
        if val==A[mid]:
            return mid+1
        elif val>A[mid]:
            return binarySearch(A,val,mid+1,R)
        else:
            return binarySearch(A,val,L,mid-1)

#task 6
A=[15, 21,47,84,96]
L=0
R=len(A)-1
search=binarySearch(A,96,L,R)
print("\n",search)

#Task 7
A = {}
def fibonacci(n):
    if n in A:
        return A[n]
    if (n==1 or n==2):
        return 1
    else:
        val=fibonacci(n-1)+fibonacci(n-2)
        A[n] = val
        return val


# task 7
n=5
print(fibonacci(n))