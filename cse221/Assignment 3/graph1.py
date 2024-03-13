from collections import defaultdict

graph = defaultdict(list)
def addEdge(graph, u, v):
    graph[u].append(v)

fileo=open(" ","r")
v= int(fileo.readline())
e= int(fileo.readline())
fdata=fileo.readlines()
for i in fdata:
    m=i.strip().split()
    a=int(m[0])
    b=int(m[1])
    addEdge(graph,a,b)
graphC=dict(graph)

#bfs 
visited=[0]*v
print("BFS:")
def BFS(visited,graph,start,end):
    queue=[]

    
    visited[int(start)-1]=1
    queue.append(start)
    while queue:
        m=queue.pop(0)
        print(m,end=" ")
        if m==end:
            break
        for neighbour in graph[m]:
            if visited[int(neighbour)-1]==0:
                queue.append(neighbour)
                visited[int(neighbour)-1]=1
BFS(visited,graph,1,12)
print("\n")


#DFS
visited2=[0]*v
printed=[]
print("DFS:")
def DFS_visit(graph,node):
    visited2[int(node)-1]=1
    printed.append(node)
    for i in graph[node]:
        if i not in visited2:
            DFS_visit(graph,i)
def DFS(graph,end):
    for i in graph.copy():
        if i not in visited2:
            DFS_visit(graph,i)
    for i in range(v):
        print(printed[i], end=" ")
        if printed[i]==v:
            break
DFS(graph,12)