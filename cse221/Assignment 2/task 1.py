def bubbleSort(arr):
    i=0
    while i<len(arr)-1:
        if arr[i]>arr[i+1]:
            temp=arr[i]
            arr[i]=arr[i+1]
            arr[i+1]=temp
            i=-1
        i+=1

fdata=open(" ","r")
fdataO=open(" ","w")
n= int(fdata.readline())
arr=[0]*n
fread=fdata.readlines()
for i in fread:
    num=i.strip().split()
    for j in range(0,len(num)):
        arr[j]=int(num[j])
bubbleSort(arr)
fdataO.write("{}".format(arr))
print(arr)

