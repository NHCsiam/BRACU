class KeyIndex:
    def __init__(self,A):
        self.max=A[0]
        self.min=A[0]
        for i in range(0,len(A)):
            if self.min>A[i]:
                self.min=A[i]
        for i in range(1,len(A)):
            if self.max<A[i]:
                self.max=A[i]        
        #finding min{new array for min}
        if self.min<0:
            self.min1=self.min*-1
            for i in range(0,len(A)):
                A[i]+=self.min1
            #making new array for min
            self.max=A[0]
            for i in range(1,len(A)):
                if self.max<A[i]:
                    self.max=A[i]
            self.B=[0]*(self.max+1)
            for i in range(0,len(A)):
                self.B[A[i]]+=1
            print(self.B)
        else:
            #finding max{new array for max}
            self.B=[0]*(self.max+1)
            for i in range(0,len(A)):
                self.B[A[i]]+=1
            print(self.B)

    def search(self,val):
        if self.min>0:           
            if val<0 or val>=len(self.B):
                return False
            if self.B[val]==0:
                return False
            elif self.B[val]>0:
                return True
        else:
            if val<self.min and val<0:
                return False
            val+=self.min1           
            if self.B[val]==0:
                return False
            elif self.B[val]>0:
                return True

    def sort(self):
        j=0
        if self.min<0:
            k=0
            for i in range(len(self.B)):
                if self.B[i]>0:
                    A[k]=i+self.min
                    k+=1
                    self.B[k]-=1
            for i in range(len(A)):
                print(A[i], end=' ')
        else:    
            for i in range(len(self.B)):
                if self.B[i]>0:
                    A[j]=i
                    j+=1
            for i in range(len(A)):
                print(A[i], end=' ')

def hashtable(a):
    arr=[0]*9
    for i in a:
        s=[]
        num=0
        c=0
        s+=i
        for j in i:
            if j >= '0' and j <= '9':
                num+=int(j)
            elif j!='A' and j!='E' and j!='I' and j!='O' and j!='U':
                c+=1        
        temp=0
        temp=((c*24)+num)%9      
        if arr[temp]==0:
            arr[temp]=i
        else:
            while True:
                temp=(temp+1)%len(arr)
                if(arr[temp]==0):
                    arr[temp]=i
                    break
    return arr



A=[1,3,5,-2,0]
k=KeyIndex(A)
print(k.search(-2))
k.sort()
print(hashtable(["ST1E89B8A32","kajdas54","6969kokko","abcd58","fight42","shockdart66","yoru420","then451","loki69"]))
