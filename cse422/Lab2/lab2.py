import math
import random


def leafGenaration(id):
    for i in id:
        id=id.replace('0','8')
    
    numberofSuffle=int(id[3])        #shuffle range
    mini=int(id[4])                 
    maxi=id[-2:]
    maxiREV=int(maxi[::-1])         #reverse last two digit
    maxi=int(maxiREV*1.5)           #maximum value
    leaf=[]                         #leaf nodes
    for i in range(len(id)):
        leaf.append(random.randint(mini,maxi))
    return leaf,maxiREV,numberofSuffle, len(id)

def maximizer(depth, node,leaf,alpha,beta):
    maxeval= -math.inf
    if depth==3:
        return leaf[node]           #node is for index number, so that we can return that index value from leaf list
    else:
        for i in range (0,2):
            v = minimizer(depth + 1, node * 2 + i, leaf, alpha, beta)
            maxeval=max(maxeval,v)
            alpha = max(alpha, v)
            if alpha>=beta:
                break
        return maxeval

def minimizer(depth, node,leaf,alpha,beta):
    mineval= math.inf
    if depth==3:
        return leaf[node]          #node is for index number, so that we can return that index value from leaf list
    else:
        for i in range (0,2):
            v = maximizer(depth + 1, node * 2 + i, leaf, alpha, beta)
            mineval=min(mineval,v)
            beta = min(beta, v)
            if alpha>=beta:
                break
        return mineval

# shuffle 
def shuffle(leaf,Shufflenum):
    maxShuffle=[]
    count=0
    for i in range(0,Shufflenum):
        random.shuffle(leaf)
        ShufflePrun=maximizer(0,0,leaf,alpha,beta)
        maxShuffle.append(ShufflePrun)
        TotalMAx=max(maxShuffle)
        if ShufflePrun>=maxim:
            count+=1
    return maxShuffle, TotalMAx, count


alpha=-math.inf
beta= math.inf

id=input('Enter your student ID:')
leaf,maxim,Shufflenum,points=leafGenaration(id)
prunedPoint=maximizer(0,0,leaf,alpha,beta)
maxShuffle, TotalMAx, count=shuffle(leaf, Shufflenum)



print('Generated', points, 'random points between the minimum and maximum point limits:', leaf)
print('Total points to win:',maxim)
print("Achieved point by applying alpha-beta pruning=",prunedPoint)
if prunedPoint>=maxim:
    print('The winner is Optimus Prime')
else:
    print('The Winner is Megatron')
print('After the shuffle:')
#shuffle printing
print('List of all points values from each shuffle:',maxShuffle)
print('The maximum value of all shuffles:', TotalMAx)
print('Won',count, 'times out of',Shufflenum ,'number of shuffles')


