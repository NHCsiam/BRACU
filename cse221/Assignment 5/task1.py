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
n= int(filei.readline())
s=[]
f=[]
line=filei.readlines()
for i in line:
    num1=i.strip().split()
    s.append(int(num1[0]))
    f.append(int(num1[1]))

insertionSort(f,s)
count=0
select={}
for i in range (len(s)):
    if count==0:
        fin=f[i]
        count+=1
        select[s[i]]=f[i]
    else:
        if s[i]>=fin:
            count+=1
            fin=f[i]
            select[s[i]]=f[i]

print(count,file=fileo)
for x, y in select.items():
    print(x, y,file=fileo)


































'''fileo=open("G:/BRACU/semester 5/CSE 221/labs/Assignment 5/input1.txt","r")
n= int(fileo.readline())
fread=fileo.readlines()
start=[]
end=[]
dic={}
selected_d={}

for i in fread:
    num=i.strip().split()
    s=int(num[0])
    f=int(num[1])
    dic[s]=f
dic1 = sorted(dic.items(), key=lambda x: x[1])
print(dic1)
count=0
for i in dic1:
    if count==0:
        f=i
        count+=1
        selected_d[i]=dic[i]
    else:
        if dic[i]>f:
            count+=1
            f=i
            selected_d[i]=dic[i]
print(count)
print(selected_d)
#for i in sort_orders:
#	print(i[0], i[1])'''
