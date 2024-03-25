import random

def filing(file):
    filei=open(file,"r")
    firstLine=filei.readline().split()
    number_of_batsman=int(firstLine[0])
    goal_set=int(firstLine[1])
    player_details=dict()
    lines=filei.readlines()
    return lines, player_details, goal_set,number_of_batsman

def graph(lines,player_details):
    for i in lines:
        k = i.split()
        player_details[k[0]] = int(k[1])
    keys=list(player_details)
    values=list(player_details.values())
    return player_details,keys,values

def population(number_of_batsman):
    population=[]
    for i in range(4):
        temp=[]
        for j in range(number_of_batsman):
            temp.append(random.randint(0,1))
        population.append(temp)
    # print(population)
    return population

def fitnessSelection(population,values):
    fit=[]
    for i in population:
        summ=0
        for j in range(len(i)):
            if i[j]==1:
                summ+=values[j]
        fit.append(summ)
    # print(fit)
    minfit=fit.index(min(fit))
    population.pop(minfit)
    fit.pop(minfit)
    # print(population)
    return population, fit

def crossOver(fit,player_details):
    offspring=[]
    point=random.randint(1,len(player_details)-2)
    # print(point)
    for i in range (0,len(fit)-1):
        offspring.append(fit[0][:point]+fit[1+i][point:]) 
        offspring.append(fit[i+1][:point]+fit[0][point:])
    return offspring

def mutation(offspring,player_details):
    mutate=[]
    for i in offspring:
        mutatePoint=random.randint(0,len(player_details)-1)
        if i[mutatePoint]==1:
            i[mutatePoint]=0
        elif i[mutatePoint]==0:
            i[mutatePoint]=1
        mutate.append(i)
    return mutate

def genetics(population,goal_set,values,player_details,loop):
    fittest, value=fitnessSelection(population,values)
    loop+=1
    if loop==995:
        print(-1,loop)
        return
    else:
        for i in value:
            if i==goal_set:
                print(goal_set)
                print(fittest[value.index(i)], loop)
                return 
    off=crossOver(fittest,player_details)
    mutate=mutation(off,player_details)
    genetics(mutate,goal_set,values,player_details,loop)










lines, player_details, goal_set,number_of_batsman= filing('input.txt')
playerD,keys,values=graph(lines,player_details)
population=population(number_of_batsman)
loop=0
# genetics(population,goal_set,values,playerD,loop)

fittest, value=fitnessSelection(population,values)
for i in range(5000):
    loop+=1
    for i in value:
        if i==goal_set:
            print(goal_set)
            print(fittest[value.index(i)], loop)
            exit()
    off=crossOver(fittest,player_details)
    mutate=mutation(off,player_details)
    fittest, value=fitnessSelection(mutate,values)
print(-1)