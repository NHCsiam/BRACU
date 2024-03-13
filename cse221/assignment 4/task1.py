from collections import defaultdict
import heapq
import math

def dijkstra(graph,src=1):
    dis=[0]*len(graph)
    dis[src]=0
    q=[]
    visited=[0]*m
    for i in graph:
        if i!=src:
            dis[i]=[math.inf]*len(graph)
        heapq.heappush(q,(dis[i],i))
        visited[i]=1
    while q:
        u=heapq.heappop(q)
        if visited[u[1]]:
            continue
        visited[u[1]]=1
        for j in graph[u]:
            alt=dis[u[1]]+i[0]
            if alt<alt[i[0]]:
                dist[i[1]]=alt
                heapq.heappush(q,(dis[i[0]],i[0]))
    return dis[len(graph)-1] 
graph = defaultdict(list)
print(graph)
def addEdge(graph, u, v,w):
    graph[u].append([v,w]) 


fileo=open(" ","r")
g= int(fileo.readline())
for i in fileo:
    n,m=list(map(int,i.split()))
        
    if m==0:
        print(0)
    elif m==1:
        u,v,w=(map(int,fileo.readline().split()))
        print(w)
    else:
        for k in range(m):
            u,v,w=(map(int,fileo.readline().split()))
            addEdge(graph,u,v,w)


dijkstra(graph,1)
print(graph)

