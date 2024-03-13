file = open(" ", "r")
fileO= open (" ", "w")
n= int(file.readline())
#print(n)
A=[]
B=[]
C=[]
for i in range(n):
    A.append([0]*n)
    B.append([0]*n)
    C.append([0]*n)
idx=0
g=0
r=0
for i in file:
    if idx==n:
        break
    m1=i.strip().split()
    for j in range(0, len(m1)): #converting to int
        A[g][j] = int(m1[j])
    g+=1
    idx += 1
#print(A)
for i1 in file:
    m2=i1.strip().split()
    for y in range (0,len(m2)): #converting to int
        B[r][y]=int(m2[y])
    r+=1
#print(B)

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range (len(B)):
            C[i][j]+=A[i][k]*B[k][j]

for r in C:
    #print(r)
    fileO.write("{}\n".format(r))
























