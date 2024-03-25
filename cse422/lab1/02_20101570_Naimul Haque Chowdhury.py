filei=open("G:\BRACU\Semester 9\CSE422\Labs\lab1\Input file.txt","r")
lines=filei.readlines()
# print(lines)
heuristic={}
for i in lines:
    val=i.split()
    heuristic[val[0]]=val[1]


def childs(lines):
    parenchild={}
    for i in lines:
        val=i.split()
        val.pop(1)
        neigh=[]
        for j in range(1,len(val),2):
            child=[]
            child.append(val[j])
            child.append(int(val[j+1]))
            neigh.append(child)
        parenchild[val[0]]=neigh        
    return parenchild


def aster(parenchild,start,stop):
    open=[start]    #to save the nodes that needs to be iterated
    close=[]        #to save iterated nodes
    g = {}          # to save all node's values
    parents = {}    # for backtracking
    g[start] = 0
    parents[start] = start


    while len(open)>0:
        currentN=None                                   #for current node check
        for i in open:
            if currentN==None or (g[i]+int(heuristic[i]))<(g[currentN]+int(heuristic[currentN])):   #calculate min val
                currentN=i
        if currentN==None:
            print("NO PATH FOUND")
            return None
        if currentN==stop:                                                 
            totalpath=[]                                                             #final path
            while parents[currentN]!=currentN:                                       #start backtracking
                totalpath.append(currentN)
                currentN=parents[currentN]
            totalpath.append(start)
            totalpath.reverse()
            print("Path:", totalpath)
            print("Total cost:",g[totalpath[-1]],"km")
            return totalpath

        for neighN,neigh_cost in parenchild[currentN]:                        #inner loop for iterate childs
            if neighN not in open and neighN not in close:
                open.append(neighN)
                parents[neighN]=currentN                                      #saving parent as it's childs value so that we can backtrack later
                g[neighN]=g[currentN]+neigh_cost                              #calculating child's cost
            else:
                if g[neighN] > g[currentN] + neigh_cost:                     #again calculating to find minimum val of a known child
                    g[neighN] = g[currentN] + neigh_cost
                    parents[neighN] = currentN                               #saving parent as it's childs value so that we can backtrack later
                    if neighN in close:
                        close.remove(neighN)
                        open.append(neighN)
        open.remove(currentN)
        close.append(currentN)






test=childs(lines)
start=input('Start node:')
stop=input('Destination:')
aster(test,start,stop)
# print(start, stop)




