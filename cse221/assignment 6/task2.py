filei=open (" ","r")
fileo=open (" ","w")
x=''
y=''
z=''
line=filei.readlines()
x+=line[0].strip('\n')
y+=line[1].strip('\n')
z+=line[2].strip('\n')

m=len(x)
n=len(y)
o=len(z)

c = [[[0 for i in range(o+1)] for j in range(n+1)]for k in range(m+1)]
t= [[[0 for i in range(o+1)] for j in range(n+1)]for k in range(m+1)]

for i in range(1,m+1):
	for j in range(1,n+1):
		for k in range(1,o+1):
			if i == 0 or j == 0 or k == 0:
				c[i][j][k] = 0
				t[i][j][k] = None
			elif x[i-1]==y[j-1] and x[i-1]==z[k-1]:
					c[i][j][k]=c[i-1][j-1][k-1]+1
					t[i][j][k]="diagonal"
			else:
				if c[i-1][j][k]>=c[i][j-1][k]:
					max=c[i-1][j][k]
					if max>=c[i][j][k-1]:
						c[i][j][k]=max
						t[i][j][k]="up-up-left"
					else:
						max=c[i][j][k-1]
						c[i][j][k]=max
						t[i][j][k]="left-up-left"
				else:
					max=c[i][j-1][k]
					if max>=c[i][j][k-1]:
						c[i][j][k]=max
						t[i][j][k]="up-left-up"
					else:
						max=c[i][j][k-1]
						c[i][j][k]=max
						t[i][j][k]="left-up-up"


fileo.write("{}".format(c[i][j][k]))



















