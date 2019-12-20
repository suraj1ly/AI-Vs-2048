
import random
import copy
def costfind(matrix,n):
    qw=0
    for i in range (0,n):
        for j in range (0,n):
            if matrix[i][j]!=0:
                if matrix[i][j]%n ==0:
                    k=int(matrix[i][j]/n)-1
                    l=n-1
                else:
                    k=int(matrix[i][j]/(n))
                    l=int(matrix[i][j]%(n))-1
                qw=qw+abs(k-i)+abs(l-j)
    return qw
def compare(s,t,n):
    d=0
    s1=s2=0
    for i in range (0,n):
        for j in range (0,n):
            if s[i][j]!=0:
                if s[i][j]==t[i][j]:
                    d=d+1
    s1=costfind(s,n)
    s2=costfind(t,n)
    
    if d==(n*n-2) and abs(s1-s2)==1:
        return 1
    return 0

def dfs():
    
    n = int(input('Enter  n : '))
    matrix = []; 
    stack =[]
    visited=[]
    temp=[]
    temp1=[]
    # initialize the number of rows
    for i in range(0,n):
        matrix += [0]
    # initialize the matrix
    for i in range (0,n):
        matrix[i] = [0]*n
    for i in range (0,n):
        for j in range (0,n):
            matrix[i][j] = int(input())
    #Main Logic
    stack.append(matrix)
    steps=0
    serial=0
    flag=0
    print("WAIT ..............IT WILL GIVE SOLUTION")
    while 1:
        serial=serial+1
        if serial % 500==0 :
            print("Number of Visited nodes = ",serial)
        c=0
        d=1
        temp=stack.pop()
        if (temp in visited) == False:
            visited.append(temp)
            
            #print(visited)
        else:
            continue
        for i in range (0,n):
            for j in range (0,n):
                if temp[i][j]==d:
                    c=c+1
                    d=d+1
        if c== (n*n-1):
            if temp[n-1][n-1]==0:
                
                flag=1
                
                break   
        for i in range (0,n):
            for j in range (0,n):
                if temp[i][j]==0:
                    if (i-1) >=0:
                        temp1=copy.deepcopy(temp)
                        f=temp1[i][j]
                        temp1[i][j]=temp1[i-1][j]
                        temp1[i-1][j]=f
                        stack.append(temp1)
                    
                    if (j-1) >=0:
                        temp1=copy.deepcopy(temp)
                        f=temp1[i][j]
                        temp1[i][j]=temp1[i][j-1]
                        temp1[i][j-1]=f
                        stack.append(temp1)
                    
                    
                    if (j+1) <n:
                        temp1=copy.deepcopy(temp)
                        f=temp1[i][j]
                        temp1[i][j]=temp1[i][j+1]
                        temp1[i][j+1]=f
                        stack.append(temp1)
                    
                    if (i+1) <n:
                        temp1=copy.deepcopy(temp)
                        f=temp1[i][j]
                        temp1[i][j]=temp1[i+1][j]
                        temp1[i+1][j]=f
                        stack.append(temp1)
    if flag==1:
            mainlist=[]
            visit=visited[::-1]
            q=visit[0]
            mainlist.append(q)
            for i in range(len(visit)):
                if compare(visit[i],q,n) == 1:
                    mainlist.append(visit[i])
                    q=visit[i]
            print("Steps are as follows :")
            mainlist=mainlist[::-1]
            for i in range(len(mainlist)):
                steps=steps+1
                print(mainlist[i])
            print("In DFS : It will give solutions in steps :")
            print(steps)

def nothing():
    print("Error in choosing choice ")
def bfs():
    n = int(input('Enter  n : '))
    matrix = []
    stack =[]
    visited=[]
    temp=[]
    temp1=[]
    # initialize the number of rows
    for i in range(0,n):
        matrix += [0]
    # initialize the matrix
    for i in range (0,n):
        matrix[i] = [0]*n
    for i in range (0,n):
        for j in range (0,n):
            matrix[i][j] = int(input())
    #Main Logic
    stack.append(matrix)
    steps=0
    serial=0
    flag=0
    print("WAIT ..............IT WILL GIVE SOLUTION")
    while 1:
        serial=serial+1
        if serial % 500==0 :
            print("Number of Visited nodes = ",serial)
        c=0
        d=1
        temp=stack.pop(0)
        if (temp in visited) == False:
            visited.append(temp)
    
            #print(visited)
        else:
            continue
        for i in range (0,n):
            for j in range (0,n):
                if temp[i][j]==d:
                    c=c+1
                    d=d+1
        if c== (n*n-1):
            if temp[n-1][n-1]==0:
                
                
                flag=1
                break   
        
        for i in range (0,n):
            for j in range (0,n):
                if temp[i][j]==0:
                    if (i-1) >=0:
                        temp1=copy.deepcopy(temp)
                        f=temp1[i][j]
                        temp1[i][j]=temp1[i-1][j]
                        temp1[i-1][j]=f
                        if temp1 not in visited:
                            stack.append(temp1)
                            
                    
                    if (j-1) >=0:
                        temp1=copy.deepcopy(temp)
                        f=temp1[i][j]
                        temp1[i][j]=temp1[i][j-1]
                        temp1[i][j-1]=f
                        if temp1 not in visited:
                            stack.append(temp1)
                         
                    
                    
                    if (j+1) <n:
                        temp1=copy.deepcopy(temp)
                        f=temp1[i][j]
                        temp1[i][j]=temp1[i][j+1]
                        temp1[i][j+1]=f
                        if temp1 not in visited:
                            stack.append(temp1)
                            
                    
                    if (i+1) <n:
                        temp1=copy.deepcopy(temp)
                        f=temp1[i][j]
                        temp1[i][j]=temp1[i+1][j]
                        temp1[i+1][j]=f
                        if temp1 not in visited:
                            stack.append(temp1)
    if flag==1:
            mainlist=[]
            visit=copy.deepcopy(visited)
            q=visit[len(visited)-1]
            mainlist.append(q)
            print(visited)
            i=len(visit)
            i=int(i/2)
            while i>0:
                print("i",i)
                if compare(visit[i],q,n) == 1:
                    mainlist.append(visit[i])
                    q=visit[i]
                    i=int(i/2)

                else:
                    i=i-1  
            print("final",i)
            if visited[0] not in mainlist:
                mainlist.append(visited[0])
            print("Steps are as follows :")
            mainlist=mainlist[::-1]
            for i in range(len(mainlist)):
                print(mainlist[i])
                steps=steps+1
            print("In BFS : It will give solutions in steps :")
            print(steps)
                

def idastar():
    n = int(input('Enter  n : '))
    matrix = []
    stack =[]
    visited=[]
    h=[]
    g=[]
    total=[]
    temp=[]
    temp1=[]
    # initialize the number of rows
    for i in range(0,n):
        matrix += [0]
    # initialize the matrix
    for i in range (0,n):
        matrix[i] = [0]*n
    for i in range (0,n):
        for j in range (0,n):
            matrix[i][j] = int(input())
    #Main Logic

    flag=0
    #print("WAIT ..............IT WILL GIVE SOLUTION")
    hue=int((n*n*n-n)/6)
    limit=0
    counting=0
    while 1:
        counting=counting+1
        stack =[]
        s=0
        visited=[]
        h=[]
        g=[]
        total=[]
        temp=[]
        temp1=[]
        limit =limit+hue
        print("Iteration ",counting," is with cost  ",limit)
        stack.append(matrix)
        h.append(0)
        g.append(0)
        total.append(h[0]+g[0])
        serial=0
        while 1:
            serial=serial+1
            if serial % 500==0 :
                print("Number of Visited nodes in interation ",counting," = ",serial)
        
            c=0
            
            d=1
            l=0
            l=total.index(min(total))
            s=h[l]
            #print(s)
            temp=stack.pop(l)
            if (temp in visited) == False:
                visited.append(temp)
                #print(visited)
            else:
                h.pop(l)
                g.pop(l)
                total.pop(l)
                continue
            for i in range (0,n):
                for j in range (0,n):
                    if temp[i][j]==d:
                        c=c+1
                        d=d+1
            if c== (n*n-1):
                if temp[n-1][n-1]==0:
                    print("In IDA* : It will give solutions in steps :")
                    print("Total Cost : ",s)
                    print("Number of steps taken : ",s/0.5)
                    flag=1
                    break   
            
            for i in range (0,n):
                for j in range (0,n):
                    if temp[i][j]==0:
                        if (i-1) >=0:
                            temp1=copy.deepcopy(temp)
                            f=temp1[i][j]
                            temp1[i][j]=temp1[i-1][j]
                            temp1[i-1][j]=f
                            
                            if costfind(temp1,n)>limit:
                                pass
                            else:
                                stack.append(temp1)
                                h.append(s+0.5)
                                g.append(costfind(temp1,n))
                                total.append(s+0.5+costfind(temp1,n))
                        
                        if (j-1) >=0:
                            temp1=copy.deepcopy(temp)
                            f=temp1[i][j]
                            temp1[i][j]=temp1[i][j-1]
                            temp1[i][j-1]=f
                            
                            if costfind(temp1,n)>limit:
                                pass
                            else:
                                stack.append(temp1)
                                h.append(s+0.5)
                                g.append(costfind(temp1,n))
                                total.append(s+0.5+costfind(temp1,n))
                        
                        
                        if (j+1) <n:
                            temp1=copy.deepcopy(temp)
                            f=temp1[i][j]
                            temp1[i][j]=temp1[i][j+1]
                            temp1[i][j+1]=f
                            if costfind(temp1,n)>limit:
                                pass
                            else:

                                stack.append(temp1)
                                
                                h.append(s+0.5)
                                g.append(costfind(temp1,n))
                                total.append(s+0.5+costfind(temp1,n))
                        
                        if (i+1) <n:
                            temp1=copy.deepcopy(temp)
                            f=temp1[i][j]
                            temp1[i][j]=temp1[i+1][j]
                            temp1[i+1][j]=f
                            if costfind(temp1,n)>limit:
                                pass
                            else:

                                stack.append(temp1)
                            
                                h.append(s+0.5)
                                g.append(costfind(temp1,n))
                                total.append(s+0.5+costfind(temp1,n))
        
            h.pop(l)
            g.pop(l)
            total.pop(l)
            if len(h)==0:
                del stack
                del s
                del visited
                del h
                del g
                del total
                del temp
                del temp1
                print("For cost ",limit," in iteration ",counting," ,it can not find the solution. ")
                break    
        
        if flag==1:
            mainlist=[]
            visit=visited[::-1]
            q=visit[0]
            mainlist.append(q)
            for i in range(len(visit)):
                if compare(visit[i],q,n) == 1:
                    mainlist.append(visit[i])
                    q=visit[i]
                    continue    
            print("Steps are calculated in ",counting," iteration of cost = ",limit," .It is as follows :")
            mainlist=mainlist[::-1]
            for i in range(len(mainlist)):
                print(mainlist[i])
            break    
       

 
def astar():
    n = int(input('Enter  n : '))
    matrix = []
    stack =[]
    visited=[]
    h=[]
    g=[]
    total=[]
    temp=[]
    temp1=[]
    mainlist=[]
    # initialize the number of rows
    for i in range(0,n):
        matrix += [0]
    # initialize the matrix
    for i in range (0,n):
        matrix[i] = [0]*n
    for i in range (0,n):
        for j in range (0,n):
            matrix[i][j] = int(input())
    #Main Logic

    stack.append(matrix)
    h.append(0)
    g.append(0)
    total.append(h[0]+g[0])
    print("WAIT ..............IT WILL GIVE SOLUTION")
    serial=0
    while 1:
        serial=serial+1
        if serial % 500==0 :
            print("Number of Visited nodes = ",serial)
        c=0
        d=1
        l=0
        l=total.index(min(total))
        s=h[l]
        #print(s)
        temp=stack.pop(l)
        if (temp in visited) == False:
            visited.append(temp)
            #print(visited)
        else:
            h.pop(l)
            g.pop(l)
            total.pop(l)
            continue
        for i in range (0,n):
            for j in range (0,n):
                if temp[i][j]==d:
                    c=c+1
                    d=d+1
        if c== (n*n-1):
            if temp[n-1][n-1]==0:
                print("In A* : It will give solutions in steps :")
                print("Total Cost : ",s)
                print("Number of steps taken : ",s/0.5)
                break   
        
        for i in range (0,n):
            for j in range (0,n):
                if temp[i][j]==0:
                    if (i-1) >=0:
                        temp1=copy.deepcopy(temp)
                        f=temp1[i][j]
                        temp1[i][j]=temp1[i-1][j]
                        temp1[i-1][j]=f
                        stack.append(temp1)
                        h.append(s+0.5)
                        g.append(costfind(temp1,n))
                        total.append(s+0.5+costfind(temp1,n))
                    
                    if (j-1) >=0:
                        temp1=copy.deepcopy(temp)
                        f=temp1[i][j]
                        temp1[i][j]=temp1[i][j-1]
                        temp1[i][j-1]=f
                        stack.append(temp1)
                        h.append(s+0.5)
                        g.append(costfind(temp1,n))
                        total.append(s+0.5+costfind(temp1,n))
                    
                    
                    if (j+1) <n:
                        temp1=copy.deepcopy(temp)
                        f=temp1[i][j]
                        temp1[i][j]=temp1[i][j+1]
                        temp1[i][j+1]=f
                        stack.append(temp1)
                        
                        h.append(s+0.5)
                        g.append(costfind(temp1,n))
                        total.append(s+0.5+costfind(temp1,n))
                    
                    if (i+1) <n:
                        temp1=copy.deepcopy(temp)
                        f=temp1[i][j]
                        temp1[i][j]=temp1[i+1][j]
                        temp1[i+1][j]=f
                        stack.append(temp1)
                      
                        h.append(s+0.5)
                        g.append(costfind(temp1,n))
                        total.append(s+0.5+costfind(temp1,n))
        h.pop(l)
        g.pop(l)
        total.pop(l)  
        
    visit=visited[::-1]
    q=visit[0]
    mainlist.append(q)
    
    for i in range(len(visit)):
        if compare(visit[i],q,n) == 1:
            mainlist.append(visit[i])
            q=visit[i]
            continue    
    print("Steps are as follows :")
    mainlist=mainlist[::-1]
    for i in range(len(mainlist)):
        print(mainlist[i])

 
# Driver program
if __name__ == "__main__":
    print("To search solution of n puzzle problem ")
    print("Use 1. BFS")
    print("Use 2. DFS")
    print("Use 3. A*")
    print("Use 4. IDA*")
    argument=int(input())
    
    if argument==1:
        bfs()
    elif argument==2:
        dfs()
    elif argument==3:
        astar()
    elif argument==4:
        idastar()
    else:
        nothing()
    
    #print("Solution does not exist")

        

            