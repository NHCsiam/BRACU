def mergeSort(A,p,q,r):
    n1 = q - p + 1
    n2 = r- q

    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(0 , n1):
        L[i] = arr[p + i]
    for j in range(0 , n2):
        R[j] = arr[q + 1 + j]
    i = 0     
    j = 0     
    g = p     
    while i < n1 and j < n2 :
        if L[i] <= R[j]:
            A[g] = L[i]
            i += 1
        else:
            A[g] = R[j]
            j += 1
        g += 1
    while i < n1:
        A[g] = L[i]
        i += 1
        g += 1
    while j < n2:
        A[g] = R[j]
        j += 1
        g += 1
def merge(arr,p,r):
    if p < r:
        q = (p+(r-1))//2
        merge(arr,p,q)
        merge(arr,q+1, r)
        mergeSort(arr,p,q, r)

file1=open(" ","r")
file2=open(" ","w")
n= int(file1.readline())
arr=[0]*n
fread=file1.readlines()
for i in fread:
    num=i.strip().split()
    for j in range(0,len(num)):
        arr[j]=int(num[j])

n=len(arr)
merge(arr,0,n-1)
file2.write("{}".format(arr))