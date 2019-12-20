import copy
import random
import numpy as np
from random import shuffle
import matplotlib.pyplot as plt
#Note: I haveto make only professor course present not others in sets
dump=[]

def fitness2(chromosomes, course1, professors1, slot, profcourse1, lec):
    value = 0
    # w1=4 is weight/penalty when professor are assigned to different Lecture Halls at same time slot
    # w2=4 is weight/penalty when Courses are assigned to different rooms at same time slot
    # w3=3 is weight/penalty when timetable does not include all the Courses
    # w4=3 is weight/penalty when number of lectures for each course is not satisfied
    # w5=3 is weight/penalty for two lectures on one day for Course
    # w10=4 is penalty when professor teach unalloted course (It is solved by making sets as according to professor to course relation) 
    w1 = 1 
    w2 = 1 
    w3 = 1 
    w4 = 1 
    w5 = 1  
    # 1
    i = 0
    l = 0
    l = len(chromosomes)
    loop = int(l/40)
    while i < int(l/lec):
        f = []
        count1 = 0
        count2 = 0
        for j in range(loop):
            if (chromosomes[(i*lec)+j][1] == 0) or (chromosomes[(i*lec)+j][1] ==-1):
                pass
            else:
                f.append(chromosomes[(i*lec)+j][1])
        g = copy.deepcopy(f)
        for j in range(len(f)):
            if f[j] in g[(j+1):]:
                count1 = count1+1
        if count1 > 0:
            count2 = count2+1
        
        i = i+1
    value = value-w1*count2
    # 2
    i = 0
    while i < (l/lec):
        f = []
        count1 = 0
        count2 = 0
        for j in range(loop):
            if (chromosomes[(i*lec)+j][0] == 0) or (chromosomes[(i*lec)+j][0] == -1):
                pass
            else:
                f.append(chromosomes[(i*lec)+j][0])
        g = copy.deepcopy(f)
        for j in range(len(f)):
            if f[j] in g[(j+1):]:
                count1 = count1+1
        if count1 > 0:
            count2 = count2+1
        value = value-w2*count2
        i = i+1
    
        
    # 3
    f = []
    count1 = 0
    count2 = 0
    for i in range(l):
        f.append(chromosomes[i][0])
    for i in range(len(course1)):
        if course1[i] in f:
            count1 = count1+1
    h = len(course1)-count1
    if h > 0:
        count2 = 1
    if count2==1:
        value = value-w3*count2

    # 4
    f = []
    count1 = 0
    count2 = 0

    for i in range(l):
        if (chromosomes[i][0]==0) or (chromosomes[i][0]==-1):
            pass
        else:

            f.append(chromosomes[i][0])
    for i in range(len(course1)):
        count1 = 0
        for j in range(slot):
            if course1[i] in f:
                k = f.index(course1[i])
                f.pop(k)
                count1 = count1+1
        if count1 != slot or course1[i] in f:
            count2 = count2+1
    
    value = value-w4*count2

    # 5 for Course
    loop = int(l/5)
    l1 = 5
    i = 0
    count2 = 0
    while i < l1:
        f = []
        count1 = 0
        for j in range(loop):
            if (chromosomes[i*loop+j][0] == 0) or (chromosomes[i*loop+j][0] == -1):
                pass
            else:
                f.append(chromosomes[i*loop+j][0])
        g = copy.deepcopy(f)
        for j in range(len(f)):
            if f[j] in g[(j+1):]:
                count1 = count1+1
        if count1 > 0:
            count2 = count2+1
        i = i+1

    value = value-w5*count2
    # 5 for Professor
    # loop=int(l/5)
    # i=0
    # l1=5
    # count2=0
    # while i<l1:
    #     f=[]
    #     count1=0
    #     for j in range(loop):
    #         if chromosomes[i*loop+j][1]==0:
    #             pass
    #         else:
    #             f.append(chromosomes[i*loop+j][1])
    #     g=copy.deepcopy(f)
    #     for j in range(len(f)):
    #         if f[j] in g[(j+1):]:
    #             count1=count1+1
    #     if count1>0:
    #         count2=count2+1
    #     i=i+1
    # value=value-w5*count2
    # 6
    # f=[]
    # p=[]

    # count1=0
    # for i in range(len(professors1)):
    #   f.append([])
    # for i in range(l):
    #   if chromosomes[i][1] in p:
    #      t=p.index(chromosomes[i][1])
    #     if chromosomes[i][0] in f[t]:
    #        pass
    #   else:
    #      f[t].append(chromosomes[i][0])
    # else:
    #   if chromosomes[i][1]==0:
    #      pass
    # else:
    #    p.append(chromosomes[i][1])
    #   f[len(p)-1].append(chromosomes[i][0])
    # for i in range(len(p)):

    #   count1=count1+len(f[i])-2

    # value=value-w6*count1

    #7
    # f=[]
    # count1=0
    # count2=0
    # for i in range(l):
    #     if chromosomes[i][1]==0:
    #         pass
    #     else:
    #         f.append(chromosomes[i][1])
    # for i in range(len(professors1)):
    #     if professors1[i] in f:
    #         count1=count1+1
    # h=len(professors1)-count1
    # if h>0:
    #     count2=1
    # value=value-w7*count2
    # 8

    # 10
    # f = []

    # count1 = 0
    # w10 = 1
    # count2=0
    # for i in range(l):
    #     if chromosomes[i][1] == 0:
    #         pass
    #     else:
    #         t = professors1.index(chromosomes[i][1])
    #         s = profcourse1[t]
    #         if chromosomes[i][0] not in s:
    #             count2 = count2+1
    # value = value-w10*count2
    return value
def fitness(chromosomes, course1, professors1, slot, profcourse1, lec):
    value = 0
    # w1=4 is weight/penalty when professor are assigned to different Lecture Halls at same time slot
    # w2=4 is weight/penalty when Courses are assigned to different rooms at same time slot
    # w3=3 is weight/penalty when timetable does not include all the Courses
    # w4=3 is weight/penalty when number of lectures for each course is not satisfied
    # w5=3 is weight/penalty for two lectures on one day for Course
    # w10=4 is penalty when professor teach unalloted course (It is solved by making sets as according to professor to course relation) 
    w1 = 1 
    w2 = 1 
    w3 = 1 
    w4 = 1 
    w5 = 1  
    # 1
    i = 0
    l = 0
    l = len(chromosomes)
    loop = int(l/40)
    while i < int(l/lec):
        f = []
        count1 = 0
        count2 = 0
        for j in range(loop):
            if chromosomes[(i*lec)+j][1] == 0:
                pass
            else:
                f.append(chromosomes[(i*lec)+j][1])
        g = copy.deepcopy(f)
        for j in range(len(f)):
            if f[j] in g[(j+1):]:
                count1 = count1+1
        if count1 > 0:
            count2 = count2+1
        
        i = i+1
    value = value-w1*count2
    # 2
    i = 0
    while i < (l/lec):
        f = []
        count1 = 0
        count2 = 0
        for j in range(loop):
            if chromosomes[(i*lec)+j][0] == 0:
                pass
            else:
                f.append(chromosomes[(i*lec)+j][0])
        g = copy.deepcopy(f)
        for j in range(len(f)):
            if f[j] in g[(j+1):]:
                count1 = count1+1
        if count1 > 0:
            count2 = count2+1
        value = value-w2*count2
        i = i+1
    
        
    # 3
    f = []
    count1 = 0
    count2 = 0
    for i in range(l):
        f.append(chromosomes[i][0])
    for i in range(len(course1)):
        if course1[i] in f:
            count1 = count1+1
    h = len(course1)-count1
    if h > 0:
        count2 = 1
    if count2==1:
        value = value-w3*count2

    # 4
    f = []
    count1 = 0
    count2 = 0

    for i in range(l):
        if chromosomes[i][0]==0:
            pass
        else:

            f.append(chromosomes[i][0])
    for i in range(len(course1)):
        count1 = 0
        for j in range(slot):
            if course1[i] in f:
                k = f.index(course1[i])
                f.pop(k)
                count1 = count1+1
        if count1 != slot or course1[i] in f:
            count2 = count2+1
    
    value = value-w4*count2

    # 5 for Course
    loop = int(l/5)
    l1 = 5
    i = 0
    count2 = 0
    while i < l1:
        f = []
        count1 = 0
        for j in range(loop):
            if chromosomes[i*loop+j][0] == 0:
                pass
            else:
                f.append(chromosomes[i*loop+j][0])
        g = copy.deepcopy(f)
        for j in range(len(f)):
            if f[j] in g[(j+1):]:
                count1 = count1+1
        if count1 > 0:
            count2 = count2+1
        i = i+1

    value = value-w5*count2
    # 5 for Professor
    # loop=int(l/5)
    # i=0
    # l1=5
    # count2=0
    # while i<l1:
    #     f=[]
    #     count1=0
    #     for j in range(loop):
    #         if chromosomes[i*loop+j][1]==0:
    #             pass
    #         else:
    #             f.append(chromosomes[i*loop+j][1])
    #     g=copy.deepcopy(f)
    #     for j in range(len(f)):
    #         if f[j] in g[(j+1):]:
    #             count1=count1+1
    #     if count1>0:
    #         count2=count2+1
    #     i=i+1
    # value=value-w5*count2
    # 6
    # f=[]
    # p=[]

    # count1=0
    # for i in range(len(professors1)):
    #   f.append([])
    # for i in range(l):
    #   if chromosomes[i][1] in p:
    #      t=p.index(chromosomes[i][1])
    #     if chromosomes[i][0] in f[t]:
    #        pass
    #   else:
    #      f[t].append(chromosomes[i][0])
    # else:
    #   if chromosomes[i][1]==0:
    #      pass
    # else:
    #    p.append(chromosomes[i][1])
    #   f[len(p)-1].append(chromosomes[i][0])
    # for i in range(len(p)):

    #   count1=count1+len(f[i])-2

    # value=value-w6*count1

    #7
    # f=[]
    # count1=0
    # count2=0
    # for i in range(l):
    #     if chromosomes[i][1]==0:
    #         pass
    #     else:
    #         f.append(chromosomes[i][1])
    # for i in range(len(professors1)):
    #     if professors1[i] in f:
    #         count1=count1+1
    # h=len(professors1)-count1
    # if h>0:
    #     count2=1
    # value=value-w7*count2
    # 8

    # 10
    # f = []

    # count1 = 0
    # w10 = 1
    # count2=0
    # for i in range(l):
    #     if chromosomes[i][1] == 0:
    #         pass
    #     else:
    #         t = professors1.index(chromosomes[i][1])
    #         s = profcourse1[t]
    #         if chromosomes[i][0] not in s:
    #             count2 = count2+1
    # value = value-w10*count2
    return value


def cross(c1, c2, l1):
    size1 = 40*l1
    t = random.randint(0, (size1-1))
    c3 = []
    c4 = []
    c6=[]
    c7=[]
    c3 = c1[0:t]
    c4 = c2[0:t]

    i = t
    while i < size1:
        c3.append(c2[i])
        i = i+1
    i = t
    while i < size1:
        c4.append(c1[i])
        i = i+1
    q=random.randint(0,100)
    #For Double Point CrossOver
    if q<80:
        c6,c7=cross(copy.deepcopy(c3),copy.deepcopy(c4),l1)
    

    if len(c6)>0:
        return c6,c7
    return c3, c4


def crossover(chromosomes1, l1):
    population2 = copy.deepcopy(chromosomes1)
    d1 = []
    d2 = []
    for i in range(len(chromosomes1)):
        j = i+1
        while (j < len(chromosomes1)):
            d1, d2 = cross(copy.deepcopy(
                chromosomes1[i]), copy.deepcopy(chromosomes1[j]), l1)
            population2.append(d1)
            population2.append(d2)
            j = j+1

    return population2


def mutation(p, l1, set1):
    pop1 = copy.deepcopy(p)
    p = 0
    for i in range(len(pop1)):
        p = random.randint(0, 100)/100
        if p <= 0.92:
            j = 0
            while j < len(pop1[i]):

                q = random.randint(0, 100)/100
                if q <= 0.95:
                    r = random.randint(0, (len(set1)-1))

                    pop1[i][j] = set1[r]
                else:
                    pass
                j = j+1
        else:
            pass
    return pop1
# def collision(chromosomes,l1,profcourse1,course1,professor1,courseslot1,sets1):

#     pass
def localsearch(population1,l1,profcourse1,course1,professor1,courseslot1,sets1):
    pop2=copy.deepcopy(population1)
    i=0
    size=40*l1
    
    #Step 1 Reccombining two Chromosomes and select the best one in neighbour 
    while i<(len(pop2)-1):
        d=[]
        
        e=[]
        f=[]
        g=[]
        q=[]
        r=[]
        d,e=cross(copy.deepcopy(pop2[i]),copy.deepcopy(pop2[i+1]),l1)
        d1=fitness(copy.deepcopy(d), copy.deepcopy(course1), copy.deepcopy(professor1), courseslot1, copy.deepcopy(profcourse1), l1)
        d2=fitness(copy.deepcopy(e), copy.deepcopy(course1), copy.deepcopy(professor1), courseslot1, copy.deepcopy(profcourse1), l1)
        d3=fitness(copy.deepcopy(pop2[i]), copy.deepcopy(course1), copy.deepcopy(professor1), courseslot1, copy.deepcopy(profcourse1), l1)
        d4=fitness(copy.deepcopy(pop2[i+1]), copy.deepcopy(course1), copy.deepcopy(professor1), courseslot1, copy.deepcopy(profcourse1), l1)
        f.append(d1)
        f.append(d2)
        f.append(d3)
        f.append(d4)
        g.append(d)
        g.append(e)
        g.append(pop2[i])
        g.append(pop2[i+1])
        q=g[f.index(max(f))]
        u=f.index(max(f))
        f.pop(u)
        g.pop(u)
        r=g[f.index(max(f))]
        pop2[i]=q
        pop2[i+1]=r

        i=i+2
    #Step 2 For Selecting Locally Best Chromosome in neighbourhood of given Chromosomes
    
    for i in range(len(pop2)):
        #listing=[]
        #listing=collision(copy.deepcopy(pop2[i]),l1,copy.deepcopy(profcourse1),copy.deepcopy(course1),copy.deepcopy(professor1),courseslot1,copy.deepcopy(sets1))
        e=int(size*30/100)
        for j in range(e):
            poptemp=[]
            poptemp=copy.deepcopy(pop2[i])
            k=random.randint(0,(size-1))

            w=random.randint(0,100)
            if w<80:
                x=random.randint(0,(len(sets1)-1))
                poptemp[k]=sets1[x]
           
            d5=fitness(copy.deepcopy(poptemp), copy.deepcopy(course1), copy.deepcopy(professor1), courseslot1, copy.deepcopy(profcourse1), l1)
            d6=fitness(copy.deepcopy(pop2[i]), copy.deepcopy(course1), copy.deepcopy(professor1), courseslot1, copy.deepcopy(profcourse1), l1)
            if d6<d5:
                pop2[i]=poptemp

    return pop2
def representation1(chromosomes,l1):
    print()
    print()
    print("................ Time Table .................")
    days=0
    p=[[-1,-1]]
    for i in range(len(chromosomes)):
        if chromosomes[i] in p:
            chromosomes[i]=[0,0]

    size=int(len(chromosomes)/5)
    while days<5:
        i=0
        s=[]
        while i<size:
            
            s.append(chromosomes[days*size+i])
            i=i+2
        i=1
        t=[]
        while i<size:
            t.append(chromosomes[days*size+i])
            i=i+2
        print("Day ",(days+1))
        print(s)
        print(t)
        print()
        days=days+1
def representation(chromosomes,l1):
    print()
    print()
    print("................ Time Table .................")
    days=0
    size=int(len(chromosomes)/5)
    while days<5:
        i=0
        s=[]
        while i<size:
            s.append(chromosomes[days*size+i])
            i=i+2
        i=1
        t=[]
        while i<size:
            t.append(chromosomes[days*size+i])
            i=i+2
        print("Day ",(days+1))
        print(s)
        print(t)
        print()
        days=days+1
    pass
def nothing():
    print("Error in choosing choice ")

#GENETIC ALGORITHM
def ga():
    global dump
    course = []
    lecture = []
    professor = []
    profcourse = []
    c = int(input("Enter Number of Courses : "))
    l = int(input("Enter Number of Lecture Hall : "))
    p = int(input("Enter Number of Professors : "))
    print("Enter the Courses")
    for i in range(c):
        course.append(int(input()))
    print("Enter the Lecture Halls")
    for i in range(l):
        lecture.append(int(input()))
    print("Enter the Professors ")
    for i in range(p):
        professor.append(int(input()))
    courseslot = int(input("Enter the number of lectures for each Course : "))
    print("Course : ", course)
    print("Lecture : ", lecture)
    print("Profesor", professor)

    for i in range(p):
        profcourse.append([])
    print("Enter the alloted Courses for each Professor .Give not more than two courses ")
    for i in range(p):
        for j in range(2):
            print("Do You want to add Course for ", (i+1), " Professor")
            print("1. Yes")
            print("2. No")
            choice = int(input())
            if choice == 1:
                print("Enter Course to allot to ", (i+1), " Professor ")
                profcourse[i].append(int(input()))
                continue
            else:
                break

    print("Alloted Courses to professors", profcourse)
    # allot 0 for each course and professor list to identify for no lecture alloted .

    chromosome = []
    size = 40*l

    population = []
    sets = []
    sum=0
    for i in range(len(profcourse)):
        sum=sum+len(profcourse[i])
    for i in range(sum):
        sets.append([])
    count=0
    for i in range(p):
        for j in range(len(profcourse[i])):
          
            sets[count+j].append(profcourse[i][j])
            sets[count+j].append(professor[i])
        count=count+len(profcourse[i])
            
            

    # for i in range(len(course)):
    #     for j in range(len(professor)):
    #         sets[i*len(professor)+j].append(course[i])
    #         sets[i*len(professor)+j].append(professor[j])
    sets.append([0, 0])
    print("Sets : ",sets)

    for i in range(100):
        chromosome = []

        for k in range(size):
            s1 = random.randint(0, sum)
            chromosome.append(sets[s1])
        population.append(chromosome)
  
    # for i in range(len(population)):
    #     print(population[i])
    #     print()
   
    values = []
    for i in population:
        data = fitness(copy.deepcopy(i), copy.deepcopy(course), copy.deepcopy(
            professor), courseslot, copy.deepcopy(profcourse), l)
        values.append(data)
    bestchromosomes = []

    for i in range(10):
        t = values.index(max(values))
        bestchromosomes.append(population[t])
        population.pop(t)
        values.pop(t)
    # for i in range(len(bestchromosomes)):
    #     print(bestchromosomes[i])
    #     print()
    v = 0
   
    while True:
        print("Iteration .......... : ",v+1)
        population = []

        population1 = []
        population = crossover(copy.deepcopy(bestchromosomes), l)

        population1 = mutation(copy.deepcopy(
            population), l, copy.deepcopy(sets))
        r = random.randint(0, (len(sets)-1))
        q = random.randint(0, 100)
        if q<65:
            sets.append([0,0])
        else:
            sets.append(sets[r])
            m = random.randint(0, (len(sets)-1))
            sets.append(sets[m])
        values = []
        for i in population1:
            k = fitness(copy.deepcopy(i), copy.deepcopy(course), copy.deepcopy(
                professor), courseslot, copy.deepcopy(profcourse), l)
            values.append(k)
        del bestchromosomes
        bestchromosomes = []
        for i in range(10):
    
            t = values.index(max(values))
            bestchromosomes.append(population1[t])
            population1.pop(t)
            values.pop(t)

        for i in range(len(bestchromosomes)):
            
            h = fitness(copy.deepcopy(bestchromosomes[i]), copy.deepcopy(course), copy.deepcopy(
                professor), courseslot, copy.deepcopy(profcourse), len(lecture))
           
            dump.append(h)
        
            if h == 0:
                plt.plot(dump)
                plt.title('Genetic Algorithm :Programming Assignment 3')
                plt.xlabel('Iterations')
                plt.ylabel('Fitness Function')
                plt.show()
                
                representation(bestchromosomes[i],l)
                exit(0)
            
            print()
            break
        v = v+1
    

    pass

#MEMETIC ALGORITHM
def ma():
    global dump
    course = []
    lecture = []
    professor = []
    profcourse = []
    c = int(input("Enter Number of Courses : "))
    l = int(input("Enter Number of Lecture Hall : "))
    p = int(input("Enter Number of Professors : "))
    print("Enter the Courses")
    for i in range(c):
        course.append(int(input()))
    print("Enter the Lecture Halls")
    for i in range(l):
        lecture.append(int(input()))
    print("Enter the Professors ")
    for i in range(p):
        professor.append(int(input()))
    courseslot = int(input("Enter the number of lectures for each Course : "))
    print("Course : ", course)
    print("Lecture : ", lecture)
    print("Profesor", professor)

    for i in range(p):
        profcourse.append([])
    print("Enter the alloted Courses for each Professor .Give not more than two courses ")
    for i in range(p):
        for j in range(2):
            print("Do You want to add Course for ", (i+1), " Professor")
            print("1. Yes")
            print("2. No")
            choice = int(input())
            if choice == 1:
                print("Enter Course to allot to ", (i+1), " Professor ")
                profcourse[i].append(int(input()))
                continue
            else:
                break

    print("Alloted Courses to professors", profcourse)
    # allot 0 for each course and professor list to identify for no lecture alloted .

    chromosome = []
    size = 40*l

    population = []
    sets = []
    sum=0
    for i in range(len(profcourse)):
        sum=sum+len(profcourse[i])
    for i in range(sum):
        sets.append([])
    count=0
    for i in range(p):
        for j in range(len(profcourse[i])):
        
            sets[count+j].append(profcourse[i][j])
            sets[count+j].append(professor[i])
        count=count+len(profcourse[i])
    # for i in range(len(course)):
    #     for j in range(len(professor)):
    #         sets[i*len(professor)+j].append(course[i])
    #         sets[i*len(professor)+j].append(professor[j])
    sets.append([0, 0])
    print(sets)

    for i in range(100):
        chromosome = []

        for k in range(size):
            s1 = random.randint(0, sum)
            chromosome.append(sets[s1])
        population.append(chromosome)
  
    # for i in range(len(population)):
    #     print(population[i])
    #     print()
    pop1=[]
    pop1=localsearch(copy.deepcopy(population),l,copy.deepcopy(profcourse),copy.deepcopy(course),copy.deepcopy(professor),courseslot,copy.deepcopy(sets))
 
    population=[]
    population=copy.deepcopy(pop1)


   
    values = []
    for i in population:
        data = fitness(copy.deepcopy(i), copy.deepcopy(course), copy.deepcopy(
            professor), courseslot, copy.deepcopy(profcourse), l)
        values.append(data)
    bestchromosomes = []

    for i in range(10):
        t = values.index(max(values))
        bestchromosomes.append(population[t])
        population.pop(t)
        values.pop(t)
    # for i in range(len(bestchromosomes)):
    #     print(bestchromosomes[i])
    #     print()
    v = 0
   
    while True:
        print("Iteration .......... : ",v+1)
        population = []

        population1 = []
        population = crossover(copy.deepcopy(bestchromosomes), l)

        population1 = mutation(copy.deepcopy(
            population), l, copy.deepcopy(sets))
        r = random.randint(0, (len(sets)-1))
        q = random.randint(0, 100)
        if q<65:
            sets.append([0,0])
        else:
            sets.append(sets[r])
            m = random.randint(0, (len(sets)-1))
            sets.append(sets[m])
        pop1=localsearch(copy.deepcopy(population1),l,copy.deepcopy(profcourse),copy.deepcopy(course),copy.deepcopy(professor),courseslot,copy.deepcopy(sets))
       
        population1=[]
        population1=copy.deepcopy(pop1)
        
        
        values = []
        for i in population1:
            k = fitness(copy.deepcopy(i), copy.deepcopy(course), copy.deepcopy(
                professor), courseslot, copy.deepcopy(profcourse), l)
            values.append(k)
        del bestchromosomes
        bestchromosomes = []
        for i in range(10):
    
            t = values.index(max(values))
            bestchromosomes.append(population1[t])
            population1.pop(t)
            values.pop(t)

        for i in range(len(bestchromosomes)):
            
            h = fitness(copy.deepcopy(bestchromosomes[i]), copy.deepcopy(course), copy.deepcopy(
                professor), courseslot, copy.deepcopy(profcourse), len(lecture))
           
            dump.append(h)
        
            if h == 0:
                plt.plot(dump)
                plt.title('Memetic Algorithm :Programming Assignment 3')
                plt.xlabel('Iterations')
                plt.ylabel('Fitness Function')
                plt.show()
                representation(bestchromosomes[i],l)
                exit(0)
            
            print()
            break
        v = v+1
def satisfy(chromosomes,lec,course1,slot):
    # 1
    i = 0
    l = 0
    l = len(chromosomes)
    loop = int(l/40)
    count3=True
    count2 = 0
 
    while i < int(l/lec):
        f = []
        count1 = 0
        count2 = 0

        for j in range(loop):
            if (chromosomes[(i*lec)+j][1] == 0) or (chromosomes[(i*lec)+j][1]==-1):
           
                pass
            else:
                f.append(chromosomes[(i*lec)+j][1])
        g = copy.deepcopy(f)
        for j in range(len(f)):
            if f[j] in g[(j+1):]:
                count1 = count1+1
        if count1 > 0:
            count2 = count2+1
      
        
        i = i+1
    if count2>0:
        count3=False
    
    # 2
    i = 0
    count4=True
    count2=0
    while i < (l/lec):
        f = []
        count1 = 0
  
        for j in range(loop):
            if (chromosomes[(i*lec)+j][0] == 0) or (chromosomes[(i*lec)+j][0]==-1):
                if chromosomes[(i*lec)+j][0]==-1:
                    pass
            else:
                f.append(chromosomes[(i*lec)+j][0])
        g = copy.deepcopy(f)
        for j in range(len(f)):
            if f[j] in g[(j+1):]:
                count1 = count1+1
        if count1 > 0:
            count2 = count2+1
        
        i = i+1
    if count2>0:
        count4=False
    #5
    loop = int(l/5)
    l1 = 5
    i = 0
    count2 = 0

    count5=True
    while i < l1:
        f = []
        count1 = 0
        for j in range(loop):
            if (chromosomes[i*loop+j][0] == 0)or (chromosomes[i*loop+j][0]==-1):
                pass
            else:
                f.append(chromosomes[i*loop+j][0])
        g = copy.deepcopy(f)
        for j in range(len(f)):
            if f[j] in g[(j+1):]:
                count1 = count1+1
        if count1 > 0:
            count2 = count2+1
        i = i+1
    
    if count2>0:
        count5=False

    #4
    f = []
    count1 = 0
    count2 = 0
    count6=True
    for i in range(len(chromosomes)):
        if (chromosomes[i][0]==0) or (chromosomes[i][0]==-1):
            pass
        else:

            f.append(chromosomes[i][0])
    for i in range(len(course1)):
        count1 = 0
        for j in range(slot):
            if course1[i] in f:
                k = f.index(course1[i])
                f.pop(k)
                count1 = count1+1
        if (course1[i] in f):#Changed
            count2 = count2+1
    if count2>0:
        count6=False


        
    return (count3 and count4 and count5 and count6)


def recurcsp(sets1,node1,l1,profcourse1,course1,professor1,courseslot1):
    d=[]

    s="hello"
 
    if satisfy(copy.deepcopy(node1),l1,copy.deepcopy(course1),courseslot1)==False:
        
        return s,node1 #I have to check it
    if fitness2(copy.deepcopy(node1), copy.deepcopy(course1),copy.deepcopy(professor1), courseslot1, copy.deepcopy(profcourse1), l1)==0:
      
        return "satisfy",node1
    
    for i in range(40*l1):
        
           
        if node1[i][0]!=-1 or node1[i][1]!=-1:
        
            pass
        else:
            for j in range(len(sets1)):
             
            
                
                node1[i]=sets1[j]
                
              
                
                t,d=recurcsp(copy.deepcopy(sets1),copy.deepcopy(node1),l1,copy.deepcopy(profcourse1),copy.deepcopy(course1),copy.deepcopy(professor1),courseslot1)  

                if  t=="hello":
                    continue
                
                if t=="satisfy":
             
                    return "satisfy",d

                # if satisfy(copy.deepcopy(d),l1)==False:
                #     print("satisfy")
                #     return s,node1 #I have to check
                # if fitness(copy.deepcopy(d), copy.deepcopy(course1),copy.deepcopy(professor1), courseslot1, copy.deepcopy(profcourse1), l1)==0:
                #     print("Fitness 1")
                #     return "satisfy",d  
    return s,node1   #Only for Assumptions


def csp():
    global dump
    course = []
    lecture = []
    professor = []
    profcourse = []
    c = int(input("Enter Number of Courses : "))
    l = int(input("Enter Number of Lecture Hall : "))
    p = int(input("Enter Number of Professors : "))
    print("Enter the Courses")
    for i in range(c):
        course.append(int(input()))
    print("Enter the Lecture Halls")
    for i in range(l):
        lecture.append(int(input()))
    print("Enter the Professors ")
    for i in range(p):
        professor.append(int(input()))
    courseslot = int(input("Enter the number of lectures for each Course : "))
    print("Course : ", course)
    print("Lecture : ", lecture)
    print("Profesor", professor)

    for i in range(p):
        profcourse.append([])
    print("Enter the alloted Courses for each Professor .Give not more than two courses ")
    for i in range(p):
        for j in range(2):
            print("Do You want to add Course for ", (i+1), " Professor")
            print("1. Yes")
            print("2. No")
            choice = int(input())
            if choice == 1:
                print("Enter Course to allot to ", (i+1), " Professor ")
                profcourse[i].append(int(input()))
                continue
            else:
                break

    print("Alloted Courses to professors", profcourse)
    # allot 0 for each course and professor list to identify for no lecture alloted .


    size = 40*l

    node=[]
    sets=[]
    sum=0
    for i in range(size):
        node.append([])
    for i in range(len(profcourse)):
        sum=sum+len(profcourse[i])
    for i in range(sum):
        sets.append([])
    count=0
    
    datanode=[]
    for i in range(p):
        for j in range(len(profcourse[i])):
          
            sets[count+j].append(profcourse[i][j])
            sets[count+j].append(professor[i])
        count=count+len(profcourse[i])
    for i in range(size):
        node[i].append(-1)
        node[i].append(-1)
    datanode=[]
    sets.append([0,0])

    print("Sets",sets)
    qw,datanode=recurcsp(copy.deepcopy(sets),copy.deepcopy(node),
    l,copy.deepcopy(profcourse),copy.deepcopy(course),copy.deepcopy(professor),courseslot)
    if qw=="satisfy":
        representation1(datanode,l)
        pass




 


if __name__ == "__main__":
    print("...........Time Table Optimisation..........")
    print("Enter Choice ")
    print("1. Genetic Algorithm")
    print("2. Memetic Algorithm")
    print("3. Constraint Satisfaction Problem")
    choice = int(input())
    if choice == 1:
        ga()
       
        
    elif choice == 2:
        ma()
    elif choice == 3:
        csp()
    else:
        nothing()
