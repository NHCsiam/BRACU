def selectionsort(arr):
    for i in range (len(arr)):
        minV=i
        for j in range (i,len(arr)):
            if arr[j]<arr[minV]:
                minV=j
        temp=arr[i]
        arr[i]=arr[minV]
        arr[minV]=temp


fileI=open (" ","r")
fileO= open(" ","w")
inn=fileI.readline()
num=inn.split(" ")
n=int(num[0])
m=int(num[1])
arr=[0]*n
arr2=[0]*m
fread=fileI.readlines()
for i in fread:
    num1=i.strip().split()
    for j in range(0,len(num1)):
        arr[j]=int(num1[j])
selectionsort(arr)
for i in range(m):
    arr2[i]=arr[i]
fileO.write("{}".format(arr2))

print(arr2)