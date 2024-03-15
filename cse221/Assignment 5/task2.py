def insertionSort(f,s):
    for i in range(0,len(f)):
        temp=f[i]
        temp2=s[i]
        j=i-1
        while j>=0 and temp<f[j]:
            f[j+1]=f[j]
            s[j+1]=s[j]
            j-=1
        f[j+1]=temp
        s[j+1]=temp2

filei=open (" ","r")
fileo=open (" ","w")
n= filei.readline()
n=n.strip().split()
N=int(n[0])
M=int(n[1])
s=[]
f=[]
line=filei.readlines()
for i in line:
    num1=i.strip().split()
    s.append(int(num1[0]))
    f.append(int(num1[1]))

insertionSort(f,s)

worker=[0]*M
count=0
c=0
select={}
for i in range (len(s)):
    if c<M:
        worker[i]=f[i]
        count+=1
        select[s[i]]=f[i]
    else:
        for j in range(M):
            if worker[j]<=s[i]:
                count+=1
                worker[j]=f[i]
                select[s[i]]=f[i]
                break
    c+=1
print(count,file=fileo)