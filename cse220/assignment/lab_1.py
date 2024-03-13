# Linear Arrays
# Task 1
def shiftLeft(source,k):
    i=len(source)-1
    while i>=k:
        source[i-k]=source[i]
        i-=1
    
    i=len(source)-1

    while(i>=k):
        source[i]=0 
        i=i-1
    print(source)    
    


# Task 2
def rightRotate (source,k):
    temp=[0]*k    
    i=0
    while i<k:
        temp[i]=source[i]        
        i+=1
    
    for t in range(0,len(source)-k):
        source[t]=source[t+k]
        
    i=len(source)-k
    p=0
    while(i<len(source)):
        source[i]=temp[p]
        i+=1
        p+=1
    print(source)
    


#Task 3
def remove(source,size,idx):
    i=idx
    while i<size-1:
        source[i]=source[i+1]
        i+=1
    source[size-1]=0
    print(source)
    



# Task 4
def removeAll(source,size,idx):
    i=0
    while i<len(source):
        if source[i]==idx:
            source[i]=0
        i+=1    
    for i in range(0,len(source)-1):        
            if source[i]==0 and source[i+1]!=0:
                source[i]=source[i+1]
                source[i+1]=0
    for i in range(0,len(source)-1):        
            if source[i]==0 and source[i+1]!=0:
                source[i]=source[i+1]   
                source[i+1]=0
    print(source)


# Task 5
def split(source):
    sum=0
    newAdd=0
    c=0
    for i in range(0,len(source)):
        sum+=source[i]
    for i in range(0,len(source)):
        newAdd+=source[i]
        sum-=source[i]
        if sum==newAdd:
            print('true')
            c+=1
            break
    if c==0:
        print('Flase')


# Task 6
def arraySeries (n):
    temp=[0]*(n*n)
    i=n*n-1
    while i>=0:
        j=0
        k=0
        while k<=((i+1)/n)-1:
            temp[i-j]=k+1
            k+=1
        i-=n
    print(temp)


# Task 7
def MaxBunch(source):
    c=1
    max=0
    i=0
    while i<len(source)-1:
        if (source[i]==source[i+1]):
            c+=1
        else:
            if (c>max):
                max=c
            c=1
        i+=1
    if (c>max):
        max=c
    print(max)
    

    
# Task 8
def Repetition(source):

    list1=[]
    for i in range(len(source)):
        count=1
        if(source[i]!=-1):
            for j in range(len(source)):
                if(i!=j and source[i]==source[j]):
                    count+=1
                    source[j]=-1
            list1.append(count)
    for i in range(len(list1)):
        for j in range(0,len(list1)):
            if(list1[i]>1 and list1[i]==list1[j] and i!=j):
                return True
                
                
    return False
        

#Circular Array:

# Task 1
def palindrome(source,size,start,):
    count=0
    i=size
    j=(start+size-1)%len(source)
    imple=0
    while imple<size//2:
        if source[i]!=source[j]:
            count+=1
        
        i=(i+1)%len(source)
        j-=1
        imple+=1
        if j<0:
            j=len(source)-1
            
    if count>0:
        return False
    else:
        return True
    


#Task 2
def Intersection(source1,start1,size1,source2,start2,size2):
    lin1=[]
    lin2=[]
    out=[]
    i1=start1
    i2=start2
    j=0
    while j<size1:
        lin1+=[source1[i1]]
        i1=(i1+1)%len(source1)
        j+=1
    #print(lin1)
    j=0
    while j<size2:
        lin2+=[source2[i2]]
        i2=(i2+1)%len(source2)
        j+=1
    #print(lin2)
    for i in range(len(lin1)):        
        for j in range(len(lin2)):
            if lin2[j]==lin1[i]:
                out+=[lin2[j]]
    
    print(out)
    

 

# Linear Array:
# Task 1
source=[10,20,30,40,50,60]
shiftLeft(source,3)

# Task 2
source=[10,20,30,40,50,60]
rightRotate(source, 3)

# Task 3
source=[10,20,30,40,50,0,0]
remove(source,5,2)

# Task 4
source=[10,2,30,2,50,2,2,0,0,]
removeAll(source,7,2)

# Task 5
Input=[2, 1, 1, 2, 1]  
split(Input)

#task 6
n=2
arraySeries(n)

# Task 7
Input= [1,1,2, 2, 1, 1,1,1]  
MaxBunch(Input)

# Task 8
Input= [4,5,6,6,4,3,6,4]
print(Repetition(Input))

# Circular Array:
# Task 1
Input= [10,20,0,0,0,10,20,30]
print(palindrome(Input, 5, 5))

# Task 2
Circular_array1=[40,50,0,0,0,10,20,30]
Circular_array2=[10,20,5,0,0,0,0,0,5,40,15,25]
Intersection(Circular_array1,5,5,Circular_array2,8,7)