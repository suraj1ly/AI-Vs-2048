
from collections import Counter
import time
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random
import copy
import math
# threshold=2
#start time of program
start_time = time.time()
#Define function to make euclidean distance
def euclidean_function(a,b):
    result=math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)
    return int(result)
#return the result in integer format

#function to generate the random coordinates
def generate_coordinate(n):
    coordinates = []
    for i in range(n):
        a = random.randint(0, 10 * n)
        b = random.randint(0, 10* n)
        if ((a, b)) not in coordinates:
            coordinates.append((a, b))
    return coordinates
#returning the coordinates 

#number of cities
no_of_cities = 25
#no of ants
no_of_ants = 40
#evaporation rate
pheromone_evaporation_level = 0.9
alpha = 4
beta = 6
#alpha and beta to regulate the distance and pheremone priority
#distnace matrix for random coordinates 
distance_matrix = []
# threshold=int(no_of_cities/1.5)
# threshold=random.randint(5,threshold)
#coordinates
coordinates = generate_coordinate(no_of_cities)
#Print Coordinates
print("\nCoordinates:", coordinates, "\n")

empt=[]
for i in range(no_of_cities):
    empt = []
    for j in range(no_of_cities):
        # print(i, k, coordinates[i], coordinates[k], distance.euclidean(coordinates[i], coordinates[k]))
        empt.append(euclidean_function(coordinates[i], coordinates[j]))
    distance_matrix.append(empt)

print("Distance Matrix")
print(distance_matrix)

G = nx.Graph()
for p in range(len(coordinates)):
    G.add_node(p, pos=[coordinates[p][0], coordinates[p][1]])
pos = nx.get_node_attributes(G, 'pos')
pher_level=[]
for i in range(no_of_cities):
    pher_level.append([])

#Initialising phenerome level as 0 for each edge
for i in range(no_of_cities):
    for j in range(no_of_cities):
        pher_level[i].append(0)
print()
# print("Phenerome Level : ")
# print(pher_level)
edges=G.edges
#give edges to graph


counter=0
count6=0
#iteration counter for program
while True:
    flag=False
    #printing the iteration
    print("Iteration : ",counter+1)
    # G_temp=copy.deepcopy(G)
    history=[]
    history1=[]
    for i in range(no_of_ants):
        history.append([])
        history1.append([])
    for i in range(no_of_ants):
        allowed=[]
        for j in range(no_of_cities):
            allowed.append(j)
        

        s=random.randint(0,len(allowed)-1)
        r=allowed[s]
        start=r
        history[i].append(r)
        history1[i].append(r)
        r1=r
     
        
        while (len(allowed)-1)!=0:
            allowed.remove(r1)
            
           
            p=[]
            sum=0
            for j in allowed:
                sum=sum+((pher_level[r1][j]**alpha)*((1/distance_matrix[r1][j])**beta))
            for j in allowed:
                g=((pher_level[r1][j]**alpha)*((1/distance_matrix[r1][j])**beta))
                if sum==0:
                    p.append(0)
                else:

                    p.append(g/sum)
            count=0
            for j in range(len(p)):
                if p[j]==0:
                    count=count+1
            if count==len(p) and len(p)>1:
                r2=random.randint(0,len(allowed)-1)
                r1=allowed[r2]
            else:
                h4=0
                rand=random.randint(0,100)
                f=rand/100
                s=0
                for m in range(len(p)):
                    s=s+p[m]
                    if s>f:
                        h4=m
                        break
                r2=h4
                
                r1=allowed[r2]

            
            history[i].append(r1)
            history1[i].append(r1)
        history[i].append(start)
        
        #Printing history
        #print(history)
        #Printing history1
        # print(history1)
        
    delta_pher=[]
    mark=[]
    for k in range(no_of_cities):
        mark.append([])
    for k in range(no_of_cities):
        for l in range(no_of_cities):
            mark[k].append(0)
    for i in range(no_of_ants):
        i1=1
        lk=0
        # lk=distance_matrix[history[i][len(history[i])-1]][history[i][0]]
        while i1<len(history[i]):
            lk=lk+distance_matrix[history[i][i1]][history[i][i1-1]]
            i1=i1+1
        w=30/lk
        #printing the distances that kth ant did
        # print(lk)
        delta_pher.append(1/lk)
        i1=1
       #marking the edges if it already used such that not do evaportaion
       #again because it will evaporate the edge tow or more times
       #which we donot need
        while i1<len(history[i]):
            if mark[history[i][i1]][history[i][i1-1]]==1:
                pher_level[history[i][i1]][history[i][i1-1]]=pher_level[history[i][i1]][history[i][i1-1]]+w
                pher_level[history[i][i1-1]][history[i][i1]]=pher_level[history[i][i1-1]][history[i][i1]]+w
                
            else:
                mark[history[i][i1]][history[i][i1-1]]=1
                mark[history[i][i1-1]][history[i][i1]]=1

                pher_level[history[i][i1]][history[i][i1-1]]=(1-pheromone_evaporation_level)*pher_level[history[i][i1]][history[i][i1-1]]+w
                pher_level[history[i][i1-1]][history[i][i1]]=(1-pheromone_evaporation_level)*pher_level[history[i][i1-1]][history[i][i1]]+w

            
            
            i1=i1+1
    # print(pher_level)
    #just aise hi
    # for i in range(no_of_cities):
    #     for j in range(no_of_cities):
    #         if i!=j:
    #             pher_level[i][j]=0.8*pher_level[i][j]

    for i in range(no_of_cities):
        for j in range(no_of_cities):
            if i!=j:
                if mark[i][j]==0:
                    pher_level[i][j]=(1-pheromone_evaporation_level)*pher_level[i][j]
                
    for i in range(no_of_cities):
        for j in range(no_of_cities):
            if i!=j and pher_level[i][j]>0.1:
                G.add_edge(i,j,weight=pher_level[i][j])
        #ploting the graph as nodes and edges
    weights = [G[u][v]['weight'] for u, v in edges]
    nx.draw_networkx(G, pos, node_size=100, edges=edges, width=weights)
    # print(history)
    #printing phenerome level
    # print(pher_level)
    counter=counter+1
    g=1
    h=history1[0]
    
    k2=0
    k3=len(h)-1

    h1=[]
    while k2<len(h):
        h1.append(h[k3])
        k3=k3-1
        k2=k2+1
    count1=0
    count3=0
    for l in range(no_of_cities):
        for m in range(no_of_cities):
            if l!=m:
                if (pher_level[l][m])>0.1:
                    count3=count3+1
    if count3==no_of_cities:
        flag=True
        # print(pher_level)
        


    while g<no_of_ants:
        c=0
        c1=0
        len1=0
        k=history1[g].index(h[0])
       
        k4=history1[g].index(h1[0])
        k1=k
        k5=k4 # new
        
        while k<len(history1[g]):
            
            if h[c]==history1[g][k]:
      
                len1=len1+1
            
            
            c=c+1
            k=k+1
        while c1<k1:
          
            if h[c]==history1[g][c1]:
    
                len1=len1+1
         
            
            c=c+1
            c1=c1+1
        
        c=0
        c1=0

        while k4<len(history1[g]):
            
            if h1[c]==history1[g][k4]:
           
                len1=len1+1
           
            
            c=c+1
            k4=k4+1
        while c1<k5:
          
            if h1[c]==history1[g][c1]:
               
                len1=len1+1
        
            
            c=c+1
            c1=c1+1
        # print("Length : " ,len1)

        if len1>int(len(history1[g])/1.5):
            count1=count1+1
            

        
        g=g+1
    if count1>=int((no_of_ants-1)/1.5):
        
    
        plt.show()
        
        break
    else:
        plt.pause(1)
        plt.close()

print("Time :" , (time.time() - start_time))
print("Iterations : ",counter)