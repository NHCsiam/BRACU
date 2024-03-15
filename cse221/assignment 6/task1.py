filei=open (" ","r")
fileo=open (" ","w")
z= int(filei.readline())
x=''
y=''
line=filei.readlines()
x+=line[0].strip('\n')
y+=line[1].strip('\n')
dis={"Y":"Yasnaya","P":"Pochinki","S":"School","R":"Rozhok","F":"Farm","M":'Mylta',"H":"Shelter","I":"Prison"}


#LCS

m=len(x)+1 #r
n=len(y)+1 #c
c = [[0 for i in range(m)] for j in range(n)]
t=  [[0 for i in range(m)] for j in range(n)]

for i in range(0,m):
	c[i][0]=0
	t[i][0]=None
for j in range(0,n):
	c[0][j]=0
	t[0][j]=None
for i in range(1,m):
	for j in range(1,n):
		if (x[i-1]==y[j-1]):
			c[i][j]=c[i-1][j-1]+1
			t[i][j]='diagonal'
		elif c[i-1][j] >= c[i][j-1]:
				c[i][j] = c[i-1][j]
				t[i][j] = 'up'
		else: 
			c[i][j] = c[i][j-1]
			t[i][j] = 'left'
maxx = max(c[i][j], c[i][j])
Correctness = int((maxx*100) / 8)

center=[]
i=m-1
j=n-1
o=''
while (i>0 and j>0):
	if t[i][j]=="diagonal":
		center.append(dis[y[i-1]])
		i-=1
		j-=1
	elif t[i][j]=="left":
		j-=1
	else:
		i-=1
center.reverse()
for i in center:
	fileo.write("{} ".format(i))
fileo.write("\n{} {} {}".format("Correctness of prediction:",Correctness,"%"))