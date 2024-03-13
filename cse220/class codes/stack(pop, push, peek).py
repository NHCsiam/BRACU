# Task 1
class ArrayStack:
    stack=[]
    size=0

    def push(self,x):
        
        self.stack+=x
        self.size+=1
        return self.stack
    def peek(self):
        if self.size==0:
            print("stack is empty")
            return
        else:
            value=self.stack[self.size-1]
            return value
    def pop(self):
        if self.size==0:
            print("stack is empty")
            return
        else:
            value=self.stack[self.size-1]
            self.stack[self.size-1]=0
            self.size-=1
            return value

    def checkparenthesis(self,a):
        open = ["[","{","("]
        close = ["]","}",")"]
        count=0
        for i in a:
            count+=1
            if i in open:
                self.push(i)
            elif i in close:
                pos=close.index(i)
                if len(self.stack)==0:
                    print(a)
                    return f'This expression is NOT correct. \nError at charecter #{count}."{i}"- not opened'
                if ((len(self.stack)>0)and (open[pos]==self.stack[len(self.stack)-1])):
                    self.stack.pop()
                    self.size-=1
                else:
                    if i in open:
                        print(a)
                        return f'This expression is NOT correct. \nError at charecter #{a.index(self.peek())+1}. "{self.peek()}"- not opened'
                    elif i in close:
                        print(a)
                        return f'This expression is NOT correct. \nError at charecter #{a.index(self.peek())+1}. "{self.peek()}"- not closed'
        if len(self.stack)==0:
            print(a)
            return "This expression is correct."
        else:
            if i in open:
                print(a)
                return f'This expression is NOT correct. \nError at charecter #{a.index(self.peek())+1}. "{self.peek()}"- not opened'
            elif i in close:
                print(a)
                return f'This expression is NOT correct. \nError at charecter #{a.index(self.peek())+1}. "{self.peek()}"- not closed'


# Task 2
class Node:
    def __init__(self,element):
        self.element=element
        self.next=None
class LinkedStack:
    head=None
    def push(self,x):
        new=Node(x)
        if self.head==None:
            self.head=new
        else:
            new.next=self.head
            self.head=new
    def pop(self):
        temp=self.head
        self.head=self.head.next
        temp.element=None
        temp.next=None
    def peek (self):
        return(self.head.element)
    def checkparenthesis1(self,a):
        open = ["[","{","("]
        close = ["]","}",")"]
        count=0
        for i in a:            
            count+=1
            if i in open:
                self.push(i)    
            elif i in close:
                pos=close.index(i)
                if self.head==None:
                    print(a)
                    return f'This expression is NOT correct. \nError at charecter #{count}. "{i}"- not opened'
                elif open[pos]==self.peek():
                    self.pop()                    
                else:
                    if i in open:
                        print(a)
                        return f'This expression is NOT correct. \nError at charecter #{a.index(self.peek())+1}. "{self.peek()}"- not opened'
                    elif i in close:
                        print(a)
                        return f'This expression is NOT correct. \nError at charecter #{a.index(self.peek())+1}. "{self.peek()}"- not closed'
        if self.head==None:
            print(a)
            return "This expression is correct."
        else:
            print(a)
            return "This expression is NOT correct."



#Tester 

#OUTPUT 1
li=ArrayStack()
print(li.checkparenthesis('1+2*(3/4)'))
stack=LinkedStack()
print(stack.checkparenthesis1("1+2*(3/4)"))

#OUTPUT 2
#li=ArrayStack()
#print(li.checkparenthesis('1+2*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14'))
#stack=LinkedStack()
#print(stack.checkparenthesis1("1+2*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14"))

#OUTPUT 3
#li=ArrayStack()
#print(li.checkparenthesis('1+2*[3*3+{4–5(6(7/8/9)+10)}–11+(12*8)/{13+13}]+14'))
#stack=LinkedStack()
#print(stack.checkparenthesis1("1+2*[3*3+{4–5(6(7/8/9)+10)}–11+(12*8)/{13+13}]+14"))

#OUTPUT 4
#li=ArrayStack()
#print(li.checkparenthesis('1+2]*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14'))
#stack=LinkedStack()
#print(stack.checkparenthesis1("1+2]*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14"))