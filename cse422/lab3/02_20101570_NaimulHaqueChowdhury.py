import random

# this function will give 3 values all lines as string in a list, target, number of batsman
def filing(file):
    filei=open(file,"r")
    firstLine=filei.readline().split()
    number_of_batsman=int(firstLine[0])                 #setting the number of batsman
    goal_set=int(firstLine[1])                          #setting Target score
    lines=filei.readlines()
    return lines, goal_set,number_of_batsman

#this will give a dictionary of players and their runs, list of keys as their name and list of values as their runs
def graph(lines):
    player_details={}
    for i in lines:
        perline = i.split()                             #splitting per line 
        player_details[perline[0]] = int(perline[1])    #after split adding them in dictionay as key and value
    keys=list(player_details)                           #spliting keys 
    values=list(player_details.values())                #spliting value
    return player_details,keys,values

#this will give a population list which will have 4 chromosomes and each chromosome will have 8 genes
def population(number_of_batsman):
    population=[]
    for i in range(4):
        temp=[]
        for j in range(number_of_batsman):
            temp.append(random.randint(0,1))            #genereting binary list chromosome 
        population.append(temp)
    return population

#this will give fittest list from our population and their added values
def fitnessSelection(population,values):
    fit=[]
    for i in population:
        summ=0
        for j in range(len(i)):
            if i[j]==1:
                summ+=values[j]                        #before this line "if" condition will check in which index of chromosome list matchs to 1, when it matchs it will the value of that index in value list which we got from dictionary. this is how it will find those values and will add it in sum variable. finally we will get the fitness value
        fit.append(summ)
    minfit=fit.index(min(fit))                         #get the index number from fit list 
    population.pop(minfit)                             #delete that index from population list 
    fit.pop(minfit)                                    #delete that index from fit list 
    return population, fit

#will generate a new population (offspring) using fittest list
def crossOver(fit,player_details):
    offspring=[]
    point=random.randint(1,len(player_details)-2)           # we will get a random number to do slice from
    for i in range (0,len(fit)-1):
        offspring.append(fit[0][:point]+fit[1+i][point:])   #slice first chromosome and add the sliced numbers from 2nd chromosome
        offspring.append(fit[i+1][:point]+fit[0][point:])   #slice 2nd chromosome and add the sliced numbers from first chromosome
    return offspring                                        #will get four offsprings from this crossover

#will generate a mutated population using the offsprings
def mutation(offspring,player_details):
    mutate=[]
    for i in offspring:
        mutatePoint=random.randint(0,len(player_details)-1)  #it will generate a random point which we will use as index to do mutation. it give a random index point for every offspring
        if i[mutatePoint]==1:
            i[mutatePoint]=0
        elif i[mutatePoint]==0:
            i[mutatePoint]=1
        mutate.append(i)
    return mutate






lines, goal_set,number_of_batsman= filing('input.txt')
playerDetails,keys,values=graph(lines)
population=population(number_of_batsman)
# loop=0

fittest, fit_value=fitnessSelection(population,values)
for i in range(5000):                                      #this loop will try to find the combination which will return goal satet value if cant it will break and print '-1' 
    # loop+=1
    for value in fit_value:
        if value==goal_set:
            print(keys)
            print(fittest[fit_value.index(value)] )
            exit()
    offspring=crossOver(fittest,playerDetails)
    mutate=mutation(offspring,playerDetails)
    fittest, fit_value=fitnessSelection(mutate,values)
print(keys)
print(-1)