def insertionSort(arr,arr1):
    for i in range(0,len(arr)):
        temp=arr[i]
        j=i-1
        for j in range(i-1,-1,-1): 
            if j<=0 and temp>arr[j]:
                arr[j+1]=arr[j]
                arr1[j+1]=arr1[j]
                j-=1
            else:
                return
        arr[j+1]=temp

filei=open (" ","r")
fileo=open (" ","w")
n= int(filei.readline())
arr=[0]*n
arr1=[0]*n
line=filei.readlines()
for i in range(len(arr)):
    num1=line[0].strip().split()
    for j in range(0,len(num1)):
        arr[j]=int(num1[j])
for i in range(len(arr1)):
    num=line[1].strip().split()
    for j in range(0,len(num)):
        arr1[j]=int(num[j])

insertionSort(arr,arr1)
fileo.write("{}".format(arr))
print(arr)