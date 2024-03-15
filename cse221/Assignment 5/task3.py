def insertionSort(f):
    for i in range(0,len(f)):
        temp=f[i]
        j=i-1
        while j>=0 and temp<f[j]:
            f[j+1]=f[j]
            j-=1
        f[j+1]=temp

filei=open (" ","r")
fileo=open (" ","w")
n= int(filei.readline())
f=[]
st=""
line=filei.readline().strip().split()
line2=filei.readline().strip().split()
for i in line:
    f.append(int(i))
for i in line2:
    st+=i

insertionSort(f)
Jacc=0
jilc=0
a=0
s=''
stack=[]
num=0
for i in st:
    if i=="J":
        s+=str(f[a])
        Jacc+=f[a]
        stack.append(f[a])
        a+=1
    else:
        num=stack.pop()
        s+=str(num)
        jilc+=num

print(s,file=fileo)
print("Jack will work for",Jacc,"hours",file=fileo)
print("Jill will work for",jilc,"hours",file=fileo)
