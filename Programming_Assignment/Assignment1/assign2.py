import matplotlib.pyplot as p
import matplotlib.pyplot as r
from matplotlib import colors
import numpy as np
import random
import copy
def validation(matrix,n):
    c1=0
    c2=0
    c3=0
    c4=0
    for i in range(0,n):
        for j in range(0,n):
            if matrix[i][j]==10:
                c1=c1+1
            if matrix[i][j]==20:
                c2=c2+1
            if matrix[i][j]==40:
                c3=c3+1
            if matrix[i][j]==60:
                c4=c4+1
    if (n*n)%2==0:
        if c1>int((n*n)/2) or c2>int((n*n)/2) or c3>int((n*n)/2) or c4>int((n*n)/2):
            return 1
        else:
            return 0
    else:
        if c1>(int((n*n)/2)+1) or c2>(int((n*n)/2)+1) or c3>(int((n*n)/2)+1) or c4>(int((n*n)/2)+1):
            return 1
        else: 
            return 0 
def dfs():
    n = int(input('Enter  n : '))
    data = np.random.rand(n, n) * 20
    # create discrete colormap
    cmap = colors.ListedColormap(['red', 'blue','green','yellow'])
    limit = [0,5,10,15,20]
    norm = colors.BoundaryNorm(limit, cmap.N)
    fig,a = p.subplots()
    a.imshow(data, cmap, norm)

    # draw gridlines
    p.axis('off')

    a.grid(False)
    p.title("Before Search , n*n board ")
    p.show()
    matrix = []
    stack =[]
    visited=[]
    temp=[]
    temp1=[]
    flag3=0
    # initialize the number of rows
    for i in range(0,n):
        matrix += [0]
    # initialize the matrix
    for i in range (0,n):
        matrix[i] = [0]*n
    for i in range (0,n):
        for j in range (0,n):
            if data[i][j]>=0 and data[i][j]<5:
                matrix[i][j]=10
            if data[i][j]>=5 and data[i][j]<10:
                matrix[i][j]=20
            if data[i][j]>=10 and data[i][j]<15:
                matrix[i][j]=40
            if data[i][j]>=15 and data[i][j]<=20:
                matrix[i][j]=60
    #Main Logic
    if validation(matrix,n)==1:
        print("Does not have solution ")
        flag3=1
    stack.append(matrix)
    steps=0
    if flag3==0:
        print("WAIT ..............IT WILL GIVE SOLUTION")
    while 1:
        if flag3==1:
            break
        c=0
        flag6=0
        temp=stack.pop()
        if (temp in visited) == False:
            visited.append(temp)
            steps=steps+1
            print(visited)
        else:
            continue
        g=0
        for i in range (0,n):
            for j in range (0,n):
                if (i-1)>0:
                    if temp[i][j]==temp[i-1][j]:
                        g=g+1
                if (i+1)<n:
                    if temp[i][j]==temp[i+1][j]:
                        g=g+1
                if (j-1)>0:
                    if temp[i][j]==temp[i][j-1]:
                        g=g+1
                if (j+1)<n:
                    if temp[i][j]==temp[i][j+1]:
                        g=g+1
                c=c+1
                if g>=1:
                    break

        if c== n*n and validation(temp,n)==0:
            print("In DFS : It will give solutions in steps :")
            print(steps)
            cmap = colors.ListedColormap(['red', 'blue','green','yellow'])
            limit = [0,15,25,45,65]
            norm = colors.BoundaryNorm(limit, cmap.N)
            fig,a = r.subplots()
            a.imshow(temp, cmap, norm)
            # draw gridlines
            r.axis('off')

            a.grid(False)
            r.title("After Search in DFS ,resultant n*n board ")
            r.show()
            break   
        temp1=copy.deepcopy(temp)
        logic=0
        for i in range (0,n):
            
            for j in range (0,n):
                y=0
                m=[]
                m.append(temp1[i][j])
                if (i-1)>=0:
                    if temp1[i][j]==temp1[i-1][j]:
                        y=y+1
                    else: 
                        if temp1[i-1][j] not in m:
                            m.append(temp1[i-1][j])

                if (i+1)<n:
                    if temp1[i][j]==temp1[i+1][j]:
                        y=y+1
                    else: 
                        if temp1[i+1][j] not in m:
                            m.append(temp1[i+1][j])
                if (j-1)>=0:
                    if temp1[i][j]==temp1[i][j-1]:
                        y=y+1
                    else: 
                        if temp1[i][j-1] not in m:
                            m.append(temp1[i][j-1])
                if (j+1)<n:
                    if temp1[i][j]==temp1[i][j+1]:
                        y=y+1
                    else: 
                        if temp1[i-1][j] not in m:
                            m.append(temp1[i-1][j])
                if y>0:
                    if len(m)==4:
                        logic=temp1[i+1][j]
                    else:
                        if 10 not in m:
                            logic=10
                        elif 20 not in m:
                            logic=20
                        elif 40 not in m:
                            logic=40
                        else:
                            logic=60
                h=random.randint(0,n-1)
                k=random.randint(0,n-1)
        
                flag1=0
                flag2=0
                c5=0
                for w in range(h,n):
                    if flag1==1:
                        break
                    for v in range(k,n):
                        c5=c5+1
                        if temp1[w][v]==logic:
                            t=temp1[i][j]
                            temp1[i][j]=temp1[w][v]
                            temp1[w][v]=t
                            flag1=1
                if flag1==0:
                    for w in range(0,h):
                        if flag2 ==1:
                            break
                        for v in range(0,k):
                            c5=c5+1
                            if temp1[w][v]==logic:
                                t=temp1[i][j]
                                temp1[i][j]=temp1[w][v]
                                temp1[w][v]=t
                                flag2=1
                if c5>=n*n:
                    ###
                    flag6=1
                    temp1=copy.deepcopy(temp)
                    logic=0
                    for i in range (0,n):
                        for j in range (0,n):
                        
                            m.append(temp1[i][j])
                            if (i-1)>=0:
                                if temp1[i][j]!=temp1[i-1][j]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i-1][j]
                                    temp1[i-1][j]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)


                            if (i+1)<n:
                                if temp1[i][j]!=temp1[i+1][j]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i+1][j]
                                    temp1[i+1][j]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)
                                  
                            if (j-1)>=0:
                                if temp1[i][j]!=temp1[i][j-1]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i][j-1]
                                    temp1[i][j-1]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)
                                  
                            if (j+1)<n:
                                if temp1[i][j]!=temp1[i][j+1]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i][j+1]
                                    temp1[i][j+1]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)

        if temp1 not in visited and flag6==0:
            stack.append(temp1)
        logic=0
        temp1=copy.deepcopy(temp)
        for i in range (0,n):
            
            for j in range (0,n):
                y=0
                m=[]
                m.append(temp1[i][j])
                if (i-1)>=0:
                    if temp1[i][j]==temp1[i-1][j]:
                        y=y+1
                    else: 
                        if temp1[i-1][j] not in m:
                            m.append(temp1[i-1][j])

                if (i+1)<n:
                    if temp1[i][j]==temp1[i+1][j]:
                        y=y+1
                    else: 
                        if temp1[i+1][j] not in m:
                            m.append(temp1[i+1][j])
                if (j-1)>=0:
                    if temp1[i][j]==temp1[i][j-1]:
                        y=y+1
                    else: 
                        if temp1[i][j-1] not in m:
                            m.append(temp1[i][j-1])
                if (j+1)<n:
                    if temp1[i][j]==temp1[i][j+1]:
                        y=y+1
                    else: 
                        if temp1[i-1][j] not in m:
                            m.append(temp1[i-1][j])
                if y>0:
                    if len(m)==4:
                        logic=temp1[i+1][j]
                    else:
                        if 60 not in m:
                            logic=60
                        elif 40 not in m:
                            logic=40
                        elif 20 not in m:
                            logic=20
                        else:
                            logic=10
                h=random.randint(0,n-1)
                k=random.randint(0,n-1)
            
                flag1=0
                flag2=0
                c5=0
                for w in range(h,n):
                    if flag1==1:
                        break
                    for v in range(k,n):
                        c5=c5+1
                        if temp1[w][v]==logic:
                            t=temp1[i][j]
                            temp1[i][j]=temp1[w][v]
                            temp1[w][v]=t
                            flag1=1
                if flag1==0:
                    for w in range(0,h):
                        if flag2 ==1:
                            break
                        for v in range(0,k):
                            c5=c5+1
                            if temp1[w][v]==logic:
                                t=temp1[i][j]
                                temp1[i][j]=temp1[w][v]
                                temp1[w][v]=t
                                flag2=1
                if c5>=n*n:
                    ###
                    flag6=1
                    temp1=copy.deepcopy(temp)
                    logic=0
                    for i in range (0,n):
                        for j in range (0,n):
                        
                            m.append(temp1[i][j])
                            if (i-1)>=0:
                                if temp1[i][j]!=temp1[i-1][j]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i-1][j]
                                    temp1[i-1][j]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)


                            if (i+1)<n:
                                if temp1[i][j]!=temp1[i+1][j]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i+1][j]
                                    temp1[i+1][j]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)
                                  
                            if (j-1)>=0:
                                if temp1[i][j]!=temp1[i][j-1]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i][j-1]
                                    temp1[i][j-1]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)
                                  
                            if (j+1)<n:
                                if temp1[i][j]!=temp1[i][j+1]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i][j+1]
                                    temp1[i][j+1]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)

        if temp1 not in visited and flag6==0:
            stack.append(temp1)
        temp1=copy.deepcopy(temp)
        logic=0
        for i in range (0,n):
            
            for j in range (0,n):
                y=0
                m=[]
                m.append(temp1[i][j])
                if (i-1)>=0:
                    if temp1[i][j]==temp1[i-1][j]:
                        y=y+1
                    else: 
                        if temp1[i-1][j] not in m:
                            m.append(temp1[i-1][j])

                if (i+1)<n:
                    if temp1[i][j]==temp1[i+1][j]:
                        y=y+1
                    else: 
                        if temp1[i+1][j] not in m:
                            m.append(temp1[i+1][j])
                if (j-1)>=0:
                    if temp1[i][j]==temp1[i][j-1]:
                        y=y+1
                    else: 
                        if temp1[i][j-1] not in m:
                            m.append(temp1[i][j-1])
                if (j+1)<n:
                    if temp1[i][j]==temp1[i][j+1]:
                        y=y+1
                    else: 
                        if temp1[i-1][j] not in m:
                            m.append(temp1[i-1][j])
                if y>0:
                    if len(m)==4:
                        logic=temp1[i+1][j]
                    else:
                        if 20 not in m:
                            logic=20
                        elif 60 not in m:
                            logic=60
                        elif 10 not in m:
                            logic=10
                        else:
                            logic=40
                h=random.randint(0,n-1)
                k=random.randint(0,n-1)
             
                flag1=0
                flag2=0
                c5=0
                for w in range(h,n):
                    if flag1==1:
                        break
                    for v in range(k,n):
                        c5=c5+1
                        if temp1[w][v]==logic:
                            t=temp1[i][j]
                            temp1[i][j]=temp1[w][v]
                            temp1[w][v]=t
                            flag1=1
                if flag1==0:
                    for w in range(0,h):
                        if flag2 ==1:
                            break
                        for v in range(0,k):
                            c5=c5+1
                            if temp1[w][v]==logic:
                                t=temp1[i][j]
                                temp1[i][j]=temp1[w][v]
                                temp1[w][v]=t
                                flag2=1
                if c5>=n*n:
                    ###
                    flag6=1
                    temp1=copy.deepcopy(temp)
                    logic=0
                    for i in range (0,n):
                        for j in range (0,n):
                        
                            m.append(temp1[i][j])
                            if (i-1)>=0:
                                if temp1[i][j]!=temp1[i-1][j]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i-1][j]
                                    temp1[i-1][j]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)


                            if (i+1)<n:
                                if temp1[i][j]!=temp1[i+1][j]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i+1][j]
                                    temp1[i+1][j]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)
                                  
                            if (j-1)>=0:
                                if temp1[i][j]!=temp1[i][j-1]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i][j-1]
                                    temp1[i][j-1]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)
                                  
                            if (j+1)<n:
                                if temp1[i][j]!=temp1[i][j+1]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i][j+1]
                                    temp1[i][j+1]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)

        if temp1 not in visited and flag6==0:
            stack.append(temp1)
        temp1=copy.deepcopy(temp)
        logic=0
        for i in range (0,n):
            
            for j in range (0,n):
                y=0
                m=[]
                m.append(temp1[i][j])
                if (i-1)>=0:
                    if temp1[i][j]==temp1[i-1][j]:
                        y=y+1
                    else: 
                        if temp1[i-1][j] not in m:
                            m.append(temp1[i-1][j])

                if (i+1)<n:
                    if temp1[i][j]==temp1[i+1][j]:
                        y=y+1
                    else: 
                        if temp1[i+1][j] not in m:
                            m.append(temp1[i+1][j])
                if (j-1)>=0:
                    if temp1[i][j]==temp1[i][j-1]:
                        y=y+1
                    else: 
                        if temp1[i][j-1] not in m:
                            m.append(temp1[i][j-1])
                if (j+1)<n:
                    if temp1[i][j]==temp1[i][j+1]:
                        y=y+1
                    else: 
                        if temp1[i-1][j] not in m:
                            m.append(temp1[i-1][j])
                if y>0:
                    if len(m)==4:
                        logic=temp1[i+1][j]
                    else:
                        if 40 not in m:
                            logic=40
                        elif 10 not in m:
                            logic=10
                        elif 60 not in m:
                            logic=60
                        else:
                            logic=20
                h=random.randint(0,n-1)
                k=random.randint(0,n-1)
     
                flag1=0
                flag2=0
                c5=0
                for w in range(h,n):
                    if flag1==1:
                        break
                    for v in range(k,n):
                        c5=c5+1
                        if temp1[w][v]==logic:
                            t=temp1[i][j]
                            temp1[i][j]=temp1[w][v]
                            temp1[w][v]=t
                            flag1=1
                if flag1==0:
                    for w in range(0,h):
                        if flag2 ==1:
                            break
                        for v in range(0,k):
                            c5=c5+1
                            if temp1[w][v]==logic:
                                t=temp1[i][j]
                                temp1[i][j]=temp1[w][v]
                                temp1[w][v]=t
                                flag2=1
                if c5>=n*n:
                    ###
                    flag6=1
                    temp1=copy.deepcopy(temp)
                    logic=0
                    for i in range (0,n):
                        for j in range (0,n):
                        
                            m.append(temp1[i][j])
                            if (i-1)>=0:
                                if temp1[i][j]!=temp1[i-1][j]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i-1][j]
                                    temp1[i-1][j]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)


                            if (i+1)<n:
                                if temp1[i][j]!=temp1[i+1][j]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i+1][j]
                                    temp1[i+1][j]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)
                                  
                            if (j-1)>=0:
                                if temp1[i][j]!=temp1[i][j-1]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i][j-1]
                                    temp1[i][j-1]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)
                                  
                            if (j+1)<n:
                                if temp1[i][j]!=temp1[i][j+1]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i][j+1]
                                    temp1[i][j+1]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)

        if temp1 not in visited and flag6==0:
            stack.append(temp1)
        ###
        temp1=copy.deepcopy(temp)
        logic=0
        for i in range (0,n):
            
            for j in range (0,n):
                y=0
                m=[]
                m.append(temp1[i][j])
                if (i-1)>=0:
                    if temp1[i][j]==temp1[i-1][j]:
                        y=y+1
                    else: 
                        if temp1[i-1][j] not in m:
                            m.append(temp1[i-1][j])

                if (i+1)<n:
                    if temp1[i][j]==temp1[i+1][j]:
                        y=y+1
                    else: 
                        if temp1[i+1][j] not in m:
                            m.append(temp1[i+1][j])
                if (j-1)>=0:
                    if temp1[i][j]==temp1[i][j-1]:
                        y=y+1
                    else: 
                        if temp1[i][j-1] not in m:
                            m.append(temp1[i][j-1])
                if (j+1)<n:
                    if temp1[i][j]==temp1[i][j+1]:
                        y=y+1
                    else: 
                        if temp1[i-1][j] not in m:
                            m.append(temp1[i-1][j])
                if y>0:
                    if len(m)==4:
                        logic=temp1[i+1][j]
                    else:
                        if 60 not in m:
                            logic=60
                        elif 40 not in m:
                            logic=40
                        elif 20 not in m:
                            logic=20
                        else:
                            logic=10
                h=random.randint(0,n-1)
                k=random.randint(0,n-1)
                flag1=0
                flag2=0
                c5=0
                for w in range(h,n):
                    if flag1==1:
                        break
                    for v in range(k,n):
                        c5=c5+1
                        if temp1[w][v]==logic:
                            t=temp1[i][j]
                            temp1[i][j]=temp1[w][v]
                            temp1[w][v]=t
                            flag1=1
                if flag1==0:
                    for w in range(0,h):
                        if flag2 ==1:
                            break
                        for v in range(0,k):
                            c5=c5+1
                            if temp1[w][v]==logic:
                                t=temp1[i][j]
                                temp1[i][j]=temp1[w][v]
                                temp1[w][v]=t
                                flag2=1
                if c5>=n*n:
                    ###
                    flag6=1
                    temp1=copy.deepcopy(temp)
                    logic=0
                    for i in range (0,n):
                        for j in range (0,n):
                        
                            m.append(temp1[i][j])
                            if (i-1)>=0:
                                if temp1[i][j]!=temp1[i-1][j]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i-1][j]
                                    temp1[i-1][j]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)


                            if (i+1)<n:
                                if temp1[i][j]!=temp1[i+1][j]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i+1][j]
                                    temp1[i+1][j]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)
                                  
                            if (j-1)>=0:
                                if temp1[i][j]!=temp1[i][j-1]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i][j-1]
                                    temp1[i][j-1]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)
                                  
                            if (j+1)<n:
                                if temp1[i][j]!=temp1[i][j+1]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i][j+1]
                                    temp1[i][j+1]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)

        if temp1 not in visited and flag6==0:
            stack.append(temp1)
        temp1=copy.deepcopy(temp)
        logic=0
        for i in range (0,n):
            
            for j in range (0,n):
                y=0
                m=[]
                m.append(temp1[i][j])
                if (i-1)>=0:
                    if temp1[i][j]==temp1[i-1][j]:
                        y=y+1
                    else: 
                        if temp1[i-1][j] not in m:
                            m.append(temp1[i-1][j])

                if (i+1)<n:
                    if temp1[i][j]==temp1[i+1][j]:
                        y=y+1
                    else: 
                        if temp1[i+1][j] not in m:
                            m.append(temp1[i+1][j])
                if (j-1)>=0:
                    if temp1[i][j]==temp1[i][j-1]:
                        y=y+1
                    else: 
                        if temp1[i][j-1] not in m:
                            m.append(temp1[i][j-1])
                if (j+1)<n:
                    if temp1[i][j]==temp1[i][j+1]:
                        y=y+1
                    else: 
                        if temp1[i-1][j] not in m:
                            m.append(temp1[i-1][j])
                if y>0:
                    if len(m)==4:
                        logic=temp1[i+1][j]
                    else:
                        if 10 not in m:
                            logic=10
                        elif 60 not in m:
                            logic=60
                        elif 20 not in m:
                            logic=20
                        else:
                            logic=40
                        
                h=random.randint(0,n-1)
                k=random.randint(0,n-1)
             
                flag1=0
                flag2=0
                c5=0
                for w in range(h,n):
                    if flag1==1:
                        break
                    for v in range(k,n):
                        c5=c5+1
                        if temp1[w][v]==logic:
                            t=temp1[i][j]
                            temp1[i][j]=temp1[w][v]
                            temp1[w][v]=t
                            flag1=1
                if flag1==0:
                    for w in range(0,h):
                        if flag2 ==1:
                            break
                        for v in range(0,k):
                            c5=c5+1
                            if temp1[w][v]==logic:
                                t=temp1[i][j]
                                temp1[i][j]=temp1[w][v]
                                temp1[w][v]=t
                                flag2=1
                if c5>=n*n:
                    ###
                    flag6=1
                    temp1=copy.deepcopy(temp)
                    logic=0
                    for i in range (0,n):
                        for j in range (0,n):
                        
                            m.append(temp1[i][j])
                            if (i-1)>=0:
                                if temp1[i][j]!=temp1[i-1][j]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i-1][j]
                                    temp1[i-1][j]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)


                            if (i+1)<n:
                                if temp1[i][j]!=temp1[i+1][j]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i+1][j]
                                    temp1[i+1][j]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)
                                  
                            if (j-1)>=0:
                                if temp1[i][j]!=temp1[i][j-1]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i][j-1]
                                    temp1[i][j-1]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)
                                  
                            if (j+1)<n:
                                if temp1[i][j]!=temp1[i][j+1]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i][j+1]
                                    temp1[i][j+1]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)

        if temp1 not in visited and flag6==0:
            stack.append(temp1)
        temp1=copy.deepcopy(temp)
        logic=0
        for i in range (0,n):
            
            for j in range (0,n):
                y=0
                m=[]
                m.append(temp1[i][j])
                if (i-1)>=0:
                    if temp1[i][j]==temp1[i-1][j]:
                        y=y+1
                    else: 
                        if temp1[i-1][j] not in m:
                            m.append(temp1[i-1][j])

                if (i+1)<n:
                    if temp1[i][j]==temp1[i+1][j]:
                        y=y+1
                    else: 
                        if temp1[i+1][j] not in m:
                            m.append(temp1[i+1][j])
                if (j-1)>=0:
                    if temp1[i][j]==temp1[i][j-1]:
                        y=y+1
                    else: 
                        if temp1[i][j-1] not in m:
                            m.append(temp1[i][j-1])
                if (j+1)<n:
                    if temp1[i][j]==temp1[i][j+1]:
                        y=y+1
                    else: 
                        if temp1[i-1][j] not in m:
                            m.append(temp1[i-1][j])
                if y>0:
                    if len(m)==4:
                        logic=temp1[i+1][j]
                    else:
                        if 40 not in m:
                            logic=40
                        elif 20 not in m:
                            logic=20
                        elif 60 not in m:
                            logic=60
                        else:
                            logic=10
                h=random.randint(0,n-1)
                k=random.randint(0,n-1)
  
                flag1=0
                flag2=0
                c5=0
                for w in range(h,n):
                    if flag1==1:
                        break
                    for v in range(k,n):
                        c5=c5+1
                        if temp1[w][v]==logic:
                            t=temp1[i][j]
                            temp1[i][j]=temp1[w][v]
                            temp1[w][v]=t
                            flag1=1
                if flag1==0:
                    for w in range(0,h):
                        if flag2 ==1:
                            break
                        for v in range(0,k):
                            c5=c5+1
                            if temp1[w][v]==logic:
                                t=temp1[i][j]
                                temp1[i][j]=temp1[w][v]
                                temp1[w][v]=t
                                flag2=1
                if c5>=n*n:
                    ###
                    flag6=1
                    temp1=copy.deepcopy(temp)
                    logic=0
                    for i in range (0,n):
                        for j in range (0,n):
                        
                            m.append(temp1[i][j])
                            if (i-1)>=0:
                                if temp1[i][j]!=temp1[i-1][j]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i-1][j]
                                    temp1[i-1][j]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)


                            if (i+1)<n:
                                if temp1[i][j]!=temp1[i+1][j]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i+1][j]
                                    temp1[i+1][j]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)
                                  
                            if (j-1)>=0:
                                if temp1[i][j]!=temp1[i][j-1]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i][j-1]
                                    temp1[i][j-1]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)
                                  
                            if (j+1)<n:
                                if temp1[i][j]!=temp1[i][j+1]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i][j+1]
                                    temp1[i][j+1]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)

        if temp1 not in visited and flag6==0:
            stack.append(temp1)
        temp1=copy.deepcopy(temp)
        logic=0
        for i in range (0,n):
            
            for j in range (0,n):
                y=0
                m=[]
                m.append(temp1[i][j])
                if (i-1)>=0:
                    if temp1[i][j]==temp1[i-1][j]:
                        y=y+1
                    else: 
                        if temp1[i-1][j] not in m:
                            m.append(temp1[i-1][j])

                if (i+1)<n:
                    if temp1[i][j]==temp1[i+1][j]:
                        y=y+1
                    else: 
                        if temp1[i+1][j] not in m:
                            m.append(temp1[i+1][j])
                if (j-1)>=0:
                    if temp1[i][j]==temp1[i][j-1]:
                        y=y+1
                    else: 
                        if temp1[i][j-1] not in m:
                            m.append(temp1[i][j-1])
                if (j+1)<n:
                    if temp1[i][j]==temp1[i][j+1]:
                        y=y+1
                    else: 
                        if temp1[i-1][j] not in m:
                            m.append(temp1[i-1][j])
                if y>0:
                    if len(m)==4:
                        logic=temp1[i+1][j]
                    else:
                        if 60 not in m:
                            logic=60
                        elif 20 not in m:
                            logic=20
                        elif 10 not in m:
                            logic=10
                        else:
                            logic=40
                h=random.randint(0,n-1)
                k=random.randint(0,n-1)
            
                flag1=0
                flag2=0
                c5=0
                for w in range(h,n):
                    if flag1==1:
                        break
                    for v in range(k,n):
                        c5=c5+1
                        if temp1[w][v]==logic:
                            t=temp1[i][j]
                            temp1[i][j]=temp1[w][v]
                            temp1[w][v]=t
                            flag1=1
                if flag1==0:
                    for w in range(0,h):
                        if flag2 ==1:
                            break
                        for v in range(0,k):
                            c5=c5+1
                            if temp1[w][v]==logic:
                                t=temp1[i][j]
                                temp1[i][j]=temp1[w][v]
                                temp1[w][v]=t
                                flag2=1
                if c5>=n*n:
                    ###
                    flag6=1
                    temp1=copy.deepcopy(temp)
                    logic=0
                    for i in range (0,n):
                        for j in range (0,n):
                        
                            m.append(temp1[i][j])
                            if (i-1)>=0:
                                if temp1[i][j]!=temp1[i-1][j]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i-1][j]
                                    temp1[i-1][j]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)


                            if (i+1)<n:
                                if temp1[i][j]!=temp1[i+1][j]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i+1][j]
                                    temp1[i+1][j]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)
                                  
                            if (j-1)>=0:
                                if temp1[i][j]!=temp1[i][j-1]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i][j-1]
                                    temp1[i][j-1]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)
                                  
                            if (j+1)<n:
                                if temp1[i][j]!=temp1[i][j+1]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i][j+1]
                                    temp1[i][j+1]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)

        if temp1 not in visited and flag6==0:
            stack.append(temp1)

def bfs():
    n = int(input('Enter  n : '))
    data = np.random.rand(n, n) * 20
    # create discrete colormap
    cmap = colors.ListedColormap(['red', 'blue','green','yellow'])
    limit = [0,5,10,15,20]
    norm = colors.BoundaryNorm(limit, cmap.N)
    fig,a = p.subplots()
    a.imshow(data, cmap, norm)

    # draw gridlines
    p.axis('off')

    a.grid(False)
    p.title("Before Search , n*n board ")
    p.show()
    matrix = []
    stack =[]
    visited=[]
    temp=[]
    temp1=[]
    flag3=0
    # initialize the number of rows
    for i in range(0,n):
        matrix += [0]
    # initialize the matrix
    for i in range (0,n):
        matrix[i] = [0]*n
    for i in range (0,n):
        for j in range (0,n):
            if data[i][j]>=0 and data[i][j]<5:
                matrix[i][j]=10
            if data[i][j]>=5 and data[i][j]<10:
                matrix[i][j]=20
            if data[i][j]>=10 and data[i][j]<15:
                matrix[i][j]=40
            if data[i][j]>=15 and data[i][j]<=20:
                matrix[i][j]=60
    #Main Logic
    if validation(matrix,n)==1:
        print("Does not have solution ")
        flag3=1
    stack.append(matrix)
    steps=0
    if flag3==0:
        print("WAIT ..............IT WILL GIVE SOLUTION")
    while 1:
        if flag3==1:
            break
        c=0
        flag6=0
        temp=stack.pop(0)
        if (temp in visited) == False:
            visited.append(temp)
            steps=steps+1
            print(visited)
        else:
            continue
        g=0
        for i in range (0,n):
            for j in range (0,n):
                if (i-1)>0:
                    if temp[i][j]==temp[i-1][j]:
                        g=g+1
                if (i+1)<n:
                    if temp[i][j]==temp[i+1][j]:
                        g=g+1
                if (j-1)>0:
                    if temp[i][j]==temp[i][j-1]:
                        g=g+1
                if (j+1)<n:
                    if temp[i][j]==temp[i][j+1]:
                        g=g+1
                c=c+1
                if g>=1:
                    break

        if c== n*n and validation(temp,n)==0:
            print("In BFS : It will give solutions in steps :")
            print(steps)
            cmap = colors.ListedColormap(['red', 'blue','green','yellow'])
            limit = [0,15,25,45,65]
            norm = colors.BoundaryNorm(limit, cmap.N)
            fig,a = r.subplots()
            a.imshow(temp, cmap, norm)
            # draw gridlines
            r.axis('off')

            a.grid(False)
            r.title("After Search in BFS ,resultant n*n board ")
            r.show()
            break   
        temp1=copy.deepcopy(temp)
        logic=0
        for i in range (0,n):
            
            for j in range (0,n):
                y=0
                m=[]
                m.append(temp1[i][j])
                if (i-1)>=0:
                    if temp1[i][j]==temp1[i-1][j]:
                        y=y+1
                    else: 
                        if temp1[i-1][j] not in m:
                            m.append(temp1[i-1][j])

                if (i+1)<n:
                    if temp1[i][j]==temp1[i+1][j]:
                        y=y+1
                    else: 
                        if temp1[i+1][j] not in m:
                            m.append(temp1[i+1][j])
                if (j-1)>=0:
                    if temp1[i][j]==temp1[i][j-1]:
                        y=y+1
                    else: 
                        if temp1[i][j-1] not in m:
                            m.append(temp1[i][j-1])
                if (j+1)<n:
                    if temp1[i][j]==temp1[i][j+1]:
                        y=y+1
                    else: 
                        if temp1[i-1][j] not in m:
                            m.append(temp1[i-1][j])
                if y>0:
                    if len(m)==4:
                        logic=temp1[i+1][j]
                    else:
                        if 10 not in m:
                            logic=10
                        elif 20 not in m:
                            logic=20
                        elif 40 not in m:
                            logic=40
                        else:
                            logic=60
                h=random.randint(0,n-1)
                k=random.randint(0,n-1)
        
                flag1=0
                flag2=0
                c5=0
                for w in range(h,n):
                    if flag1==1:
                        break
                    for v in range(k,n):
                        c5=c5+1
                        if temp1[w][v]==logic:
                            t=temp1[i][j]
                            temp1[i][j]=temp1[w][v]
                            temp1[w][v]=t
                            flag1=1
                if flag1==0:
                    for w in range(0,h):
                        if flag2 ==1:
                            break
                        for v in range(0,k):
                            c5=c5+1
                            if temp1[w][v]==logic:
                                t=temp1[i][j]
                                temp1[i][j]=temp1[w][v]
                                temp1[w][v]=t
                                flag2=1
                if c5>=n*n:
                    ###
                    flag6=1
                    temp1=copy.deepcopy(temp)
                    logic=0
                    for i in range (0,n):
                        for j in range (0,n):
                        
                            m.append(temp1[i][j])
                            if (i-1)>=0:
                                if temp1[i][j]!=temp1[i-1][j]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i-1][j]
                                    temp1[i-1][j]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)


                            if (i+1)<n:
                                if temp1[i][j]!=temp1[i+1][j]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i+1][j]
                                    temp1[i+1][j]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)
                                  
                            if (j-1)>=0:
                                if temp1[i][j]!=temp1[i][j-1]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i][j-1]
                                    temp1[i][j-1]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)
                                  
                            if (j+1)<n:
                                if temp1[i][j]!=temp1[i][j+1]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i][j+1]
                                    temp1[i][j+1]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)

        if temp1 not in visited and flag6==0:
            stack.append(temp1)
        logic=0
        temp1=copy.deepcopy(temp)
        for i in range (0,n):
            
            for j in range (0,n):
                y=0
                m=[]
                m.append(temp1[i][j])
                if (i-1)>=0:
                    if temp1[i][j]==temp1[i-1][j]:
                        y=y+1
                    else: 
                        if temp1[i-1][j] not in m:
                            m.append(temp1[i-1][j])

                if (i+1)<n:
                    if temp1[i][j]==temp1[i+1][j]:
                        y=y+1
                    else: 
                        if temp1[i+1][j] not in m:
                            m.append(temp1[i+1][j])
                if (j-1)>=0:
                    if temp1[i][j]==temp1[i][j-1]:
                        y=y+1
                    else: 
                        if temp1[i][j-1] not in m:
                            m.append(temp1[i][j-1])
                if (j+1)<n:
                    if temp1[i][j]==temp1[i][j+1]:
                        y=y+1
                    else: 
                        if temp1[i-1][j] not in m:
                            m.append(temp1[i-1][j])
                if y>0:
                    if len(m)==4:
                        logic=temp1[i+1][j]
                    else:
                        if 60 not in m:
                            logic=60
                        elif 40 not in m:
                            logic=40
                        elif 20 not in m:
                            logic=20
                        else:
                            logic=10
                h=random.randint(0,n-1)
                k=random.randint(0,n-1)
            
                flag1=0
                flag2=0
                c5=0
                for w in range(h,n):
                    if flag1==1:
                        break
                    for v in range(k,n):
                        c5=c5+1
                        if temp1[w][v]==logic:
                            t=temp1[i][j]
                            temp1[i][j]=temp1[w][v]
                            temp1[w][v]=t
                            flag1=1
                if flag1==0:
                    for w in range(0,h):
                        if flag2 ==1:
                            break
                        for v in range(0,k):
                            c5=c5+1
                            if temp1[w][v]==logic:
                                t=temp1[i][j]
                                temp1[i][j]=temp1[w][v]
                                temp1[w][v]=t
                                flag2=1
                if c5>=n*n:
                    ###
                    flag6=1
                    temp1=copy.deepcopy(temp)
                    logic=0
                    for i in range (0,n):
                        for j in range (0,n):
                        
                            m.append(temp1[i][j])
                            if (i-1)>=0:
                                if temp1[i][j]!=temp1[i-1][j]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i-1][j]
                                    temp1[i-1][j]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)


                            if (i+1)<n:
                                if temp1[i][j]!=temp1[i+1][j]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i+1][j]
                                    temp1[i+1][j]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)
                                  
                            if (j-1)>=0:
                                if temp1[i][j]!=temp1[i][j-1]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i][j-1]
                                    temp1[i][j-1]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)
                                  
                            if (j+1)<n:
                                if temp1[i][j]!=temp1[i][j+1]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i][j+1]
                                    temp1[i][j+1]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)

        if temp1 not in visited and flag6==0:
            stack.append(temp1)
        temp1=copy.deepcopy(temp)
        logic=0
        for i in range (0,n):
            
            for j in range (0,n):
                y=0
                m=[]
                m.append(temp1[i][j])
                if (i-1)>=0:
                    if temp1[i][j]==temp1[i-1][j]:
                        y=y+1
                    else: 
                        if temp1[i-1][j] not in m:
                            m.append(temp1[i-1][j])

                if (i+1)<n:
                    if temp1[i][j]==temp1[i+1][j]:
                        y=y+1
                    else: 
                        if temp1[i+1][j] not in m:
                            m.append(temp1[i+1][j])
                if (j-1)>=0:
                    if temp1[i][j]==temp1[i][j-1]:
                        y=y+1
                    else: 
                        if temp1[i][j-1] not in m:
                            m.append(temp1[i][j-1])
                if (j+1)<n:
                    if temp1[i][j]==temp1[i][j+1]:
                        y=y+1
                    else: 
                        if temp1[i-1][j] not in m:
                            m.append(temp1[i-1][j])
                if y>0:
                    if len(m)==4:
                        logic=temp1[i+1][j]
                    else:
                        if 20 not in m:
                            logic=20
                        elif 60 not in m:
                            logic=60
                        elif 10 not in m:
                            logic=10
                        else:
                            logic=40
                h=random.randint(0,n-1)
                k=random.randint(0,n-1)
             
                flag1=0
                flag2=0
                c5=0
                for w in range(h,n):
                    if flag1==1:
                        break
                    for v in range(k,n):
                        c5=c5+1
                        if temp1[w][v]==logic:
                            t=temp1[i][j]
                            temp1[i][j]=temp1[w][v]
                            temp1[w][v]=t
                            flag1=1
                if flag1==0:
                    for w in range(0,h):
                        if flag2 ==1:
                            break
                        for v in range(0,k):
                            c5=c5+1
                            if temp1[w][v]==logic:
                                t=temp1[i][j]
                                temp1[i][j]=temp1[w][v]
                                temp1[w][v]=t
                                flag2=1
                if c5>=n*n:
                    ###
                    flag6=1
                    temp1=copy.deepcopy(temp)
                    logic=0
                    for i in range (0,n):
                        for j in range (0,n):
                        
                            m.append(temp1[i][j])
                            if (i-1)>=0:
                                if temp1[i][j]!=temp1[i-1][j]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i-1][j]
                                    temp1[i-1][j]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)


                            if (i+1)<n:
                                if temp1[i][j]!=temp1[i+1][j]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i+1][j]
                                    temp1[i+1][j]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)
                                  
                            if (j-1)>=0:
                                if temp1[i][j]!=temp1[i][j-1]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i][j-1]
                                    temp1[i][j-1]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)
                                  
                            if (j+1)<n:
                                if temp1[i][j]!=temp1[i][j+1]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i][j+1]
                                    temp1[i][j+1]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)

        if temp1 not in visited and flag6==0:
            stack.append(temp1)
        temp1=copy.deepcopy(temp)
        logic=0
        for i in range (0,n):
            
            for j in range (0,n):
                y=0
                m=[]
                m.append(temp1[i][j])
                if (i-1)>=0:
                    if temp1[i][j]==temp1[i-1][j]:
                        y=y+1
                    else: 
                        if temp1[i-1][j] not in m:
                            m.append(temp1[i-1][j])

                if (i+1)<n:
                    if temp1[i][j]==temp1[i+1][j]:
                        y=y+1
                    else: 
                        if temp1[i+1][j] not in m:
                            m.append(temp1[i+1][j])
                if (j-1)>=0:
                    if temp1[i][j]==temp1[i][j-1]:
                        y=y+1
                    else: 
                        if temp1[i][j-1] not in m:
                            m.append(temp1[i][j-1])
                if (j+1)<n:
                    if temp1[i][j]==temp1[i][j+1]:
                        y=y+1
                    else: 
                        if temp1[i-1][j] not in m:
                            m.append(temp1[i-1][j])
                if y>0:
                    if len(m)==4:
                        logic=temp1[i+1][j]
                    else:
                        if 40 not in m:
                            logic=40
                        elif 10 not in m:
                            logic=10
                        elif 60 not in m:
                            logic=60
                        else:
                            logic=20
                h=random.randint(0,n-1)
                k=random.randint(0,n-1)
     
                flag1=0
                flag2=0
                c5=0
                for w in range(h,n):
                    if flag1==1:
                        break
                    for v in range(k,n):
                        c5=c5+1
                        if temp1[w][v]==logic:
                            t=temp1[i][j]
                            temp1[i][j]=temp1[w][v]
                            temp1[w][v]=t
                            flag1=1
                if flag1==0:
                    for w in range(0,h):
                        if flag2 ==1:
                            break
                        for v in range(0,k):
                            c5=c5+1
                            if temp1[w][v]==logic:
                                t=temp1[i][j]
                                temp1[i][j]=temp1[w][v]
                                temp1[w][v]=t
                                flag2=1
                if c5>=n*n:
                    ###
                    flag6=1
                    temp1=copy.deepcopy(temp)
                    logic=0
                    for i in range (0,n):
                        for j in range (0,n):
                        
                            m.append(temp1[i][j])
                            if (i-1)>=0:
                                if temp1[i][j]!=temp1[i-1][j]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i-1][j]
                                    temp1[i-1][j]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)


                            if (i+1)<n:
                                if temp1[i][j]!=temp1[i+1][j]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i+1][j]
                                    temp1[i+1][j]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)
                                  
                            if (j-1)>=0:
                                if temp1[i][j]!=temp1[i][j-1]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i][j-1]
                                    temp1[i][j-1]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)
                                  
                            if (j+1)<n:
                                if temp1[i][j]!=temp1[i][j+1]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i][j+1]
                                    temp1[i][j+1]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)

        if temp1 not in visited and flag6==0:
            stack.append(temp1)
        ###
        temp1=copy.deepcopy(temp)
        logic=0
        for i in range (0,n):
            
            for j in range (0,n):
                y=0
                m=[]
                m.append(temp1[i][j])
                if (i-1)>=0:
                    if temp1[i][j]==temp1[i-1][j]:
                        y=y+1
                    else: 
                        if temp1[i-1][j] not in m:
                            m.append(temp1[i-1][j])

                if (i+1)<n:
                    if temp1[i][j]==temp1[i+1][j]:
                        y=y+1
                    else: 
                        if temp1[i+1][j] not in m:
                            m.append(temp1[i+1][j])
                if (j-1)>=0:
                    if temp1[i][j]==temp1[i][j-1]:
                        y=y+1
                    else: 
                        if temp1[i][j-1] not in m:
                            m.append(temp1[i][j-1])
                if (j+1)<n:
                    if temp1[i][j]==temp1[i][j+1]:
                        y=y+1
                    else: 
                        if temp1[i-1][j] not in m:
                            m.append(temp1[i-1][j])
                if y>0:
                    if len(m)==4:
                        logic=temp1[i+1][j]
                    else:
                        if 60 not in m:
                            logic=60
                        elif 40 not in m:
                            logic=40
                        elif 20 not in m:
                            logic=20
                        else:
                            logic=10
                h=random.randint(0,n-1)
                k=random.randint(0,n-1)
                flag1=0
                flag2=0
                c5=0
                for w in range(h,n):
                    if flag1==1:
                        break
                    for v in range(k,n):
                        c5=c5+1
                        if temp1[w][v]==logic:
                            t=temp1[i][j]
                            temp1[i][j]=temp1[w][v]
                            temp1[w][v]=t
                            flag1=1
                if flag1==0:
                    for w in range(0,h):
                        if flag2 ==1:
                            break
                        for v in range(0,k):
                            c5=c5+1
                            if temp1[w][v]==logic:
                                t=temp1[i][j]
                                temp1[i][j]=temp1[w][v]
                                temp1[w][v]=t
                                flag2=1
                if c5>=n*n:
                    ###
                    flag6=1
                    temp1=copy.deepcopy(temp)
                    logic=0
                    for i in range (0,n):
                        for j in range (0,n):
                        
                            m.append(temp1[i][j])
                            if (i-1)>=0:
                                if temp1[i][j]!=temp1[i-1][j]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i-1][j]
                                    temp1[i-1][j]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)


                            if (i+1)<n:
                                if temp1[i][j]!=temp1[i+1][j]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i+1][j]
                                    temp1[i+1][j]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)
                                  
                            if (j-1)>=0:
                                if temp1[i][j]!=temp1[i][j-1]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i][j-1]
                                    temp1[i][j-1]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)
                                  
                            if (j+1)<n:
                                if temp1[i][j]!=temp1[i][j+1]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i][j+1]
                                    temp1[i][j+1]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)

        if temp1 not in visited and flag6==0:
            stack.append(temp1)
        temp1=copy.deepcopy(temp)
        logic=0
        for i in range (0,n):
            
            for j in range (0,n):
                y=0
                m=[]
                m.append(temp1[i][j])
                if (i-1)>=0:
                    if temp1[i][j]==temp1[i-1][j]:
                        y=y+1
                    else: 
                        if temp1[i-1][j] not in m:
                            m.append(temp1[i-1][j])

                if (i+1)<n:
                    if temp1[i][j]==temp1[i+1][j]:
                        y=y+1
                    else: 
                        if temp1[i+1][j] not in m:
                            m.append(temp1[i+1][j])
                if (j-1)>=0:
                    if temp1[i][j]==temp1[i][j-1]:
                        y=y+1
                    else: 
                        if temp1[i][j-1] not in m:
                            m.append(temp1[i][j-1])
                if (j+1)<n:
                    if temp1[i][j]==temp1[i][j+1]:
                        y=y+1
                    else: 
                        if temp1[i-1][j] not in m:
                            m.append(temp1[i-1][j])
                if y>0:
                    if len(m)==4:
                        logic=temp1[i+1][j]
                    else:
                        if 10 not in m:
                            logic=10
                        elif 60 not in m:
                            logic=60
                        elif 20 not in m:
                            logic=20
                        else:
                            logic=40
                        
                h=random.randint(0,n-1)
                k=random.randint(0,n-1)
             
                flag1=0
                flag2=0
                c5=0
                for w in range(h,n):
                    if flag1==1:
                        break
                    for v in range(k,n):
                        c5=c5+1
                        if temp1[w][v]==logic:
                            t=temp1[i][j]
                            temp1[i][j]=temp1[w][v]
                            temp1[w][v]=t
                            flag1=1
                if flag1==0:
                    for w in range(0,h):
                        if flag2 ==1:
                            break
                        for v in range(0,k):
                            c5=c5+1
                            if temp1[w][v]==logic:
                                t=temp1[i][j]
                                temp1[i][j]=temp1[w][v]
                                temp1[w][v]=t
                                flag2=1
                if c5>=n*n:
                    ###
                    flag6=1
                    temp1=copy.deepcopy(temp)
                    logic=0
                    for i in range (0,n):
                        for j in range (0,n):
                        
                            m.append(temp1[i][j])
                            if (i-1)>=0:
                                if temp1[i][j]!=temp1[i-1][j]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i-1][j]
                                    temp1[i-1][j]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)


                            if (i+1)<n:
                                if temp1[i][j]!=temp1[i+1][j]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i+1][j]
                                    temp1[i+1][j]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)
                                  
                            if (j-1)>=0:
                                if temp1[i][j]!=temp1[i][j-1]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i][j-1]
                                    temp1[i][j-1]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)
                                  
                            if (j+1)<n:
                                if temp1[i][j]!=temp1[i][j+1]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i][j+1]
                                    temp1[i][j+1]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)

        if temp1 not in visited and flag6==0:
            stack.append(temp1)
        temp1=copy.deepcopy(temp)
        logic=0
        for i in range (0,n):
            
            for j in range (0,n):
                y=0
                m=[]
                m.append(temp1[i][j])
                if (i-1)>=0:
                    if temp1[i][j]==temp1[i-1][j]:
                        y=y+1
                    else: 
                        if temp1[i-1][j] not in m:
                            m.append(temp1[i-1][j])

                if (i+1)<n:
                    if temp1[i][j]==temp1[i+1][j]:
                        y=y+1
                    else: 
                        if temp1[i+1][j] not in m:
                            m.append(temp1[i+1][j])
                if (j-1)>=0:
                    if temp1[i][j]==temp1[i][j-1]:
                        y=y+1
                    else: 
                        if temp1[i][j-1] not in m:
                            m.append(temp1[i][j-1])
                if (j+1)<n:
                    if temp1[i][j]==temp1[i][j+1]:
                        y=y+1
                    else: 
                        if temp1[i-1][j] not in m:
                            m.append(temp1[i-1][j])
                if y>0:
                    if len(m)==4:
                        logic=temp1[i+1][j]
                    else:
                        if 40 not in m:
                            logic=40
                        elif 20 not in m:
                            logic=20
                        elif 60 not in m:
                            logic=60
                        else:
                            logic=10
                h=random.randint(0,n-1)
                k=random.randint(0,n-1)
  
                flag1=0
                flag2=0
                c5=0
                for w in range(h,n):
                    if flag1==1:
                        break
                    for v in range(k,n):
                        c5=c5+1
                        if temp1[w][v]==logic:
                            t=temp1[i][j]
                            temp1[i][j]=temp1[w][v]
                            temp1[w][v]=t
                            flag1=1
                if flag1==0:
                    for w in range(0,h):
                        if flag2 ==1:
                            break
                        for v in range(0,k):
                            c5=c5+1
                            if temp1[w][v]==logic:
                                t=temp1[i][j]
                                temp1[i][j]=temp1[w][v]
                                temp1[w][v]=t
                                flag2=1
                if c5>=n*n:
                    ###
                    flag6=1
                    temp1=copy.deepcopy(temp)
                    logic=0
                    for i in range (0,n):
                        for j in range (0,n):
                        
                            m.append(temp1[i][j])
                            if (i-1)>=0:
                                if temp1[i][j]!=temp1[i-1][j]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i-1][j]
                                    temp1[i-1][j]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)


                            if (i+1)<n:
                                if temp1[i][j]!=temp1[i+1][j]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i+1][j]
                                    temp1[i+1][j]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)
                                  
                            if (j-1)>=0:
                                if temp1[i][j]!=temp1[i][j-1]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i][j-1]
                                    temp1[i][j-1]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)
                                  
                            if (j+1)<n:
                                if temp1[i][j]!=temp1[i][j+1]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i][j+1]
                                    temp1[i][j+1]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)

        if temp1 not in visited and flag6==0:
            stack.append(temp1)
        temp1=copy.deepcopy(temp)
        logic=0
        for i in range (0,n):
            
            for j in range (0,n):
                y=0
                m=[]
                m.append(temp1[i][j])
                if (i-1)>=0:
                    if temp1[i][j]==temp1[i-1][j]:
                        y=y+1
                    else: 
                        if temp1[i-1][j] not in m:
                            m.append(temp1[i-1][j])

                if (i+1)<n:
                    if temp1[i][j]==temp1[i+1][j]:
                        y=y+1
                    else: 
                        if temp1[i+1][j] not in m:
                            m.append(temp1[i+1][j])
                if (j-1)>=0:
                    if temp1[i][j]==temp1[i][j-1]:
                        y=y+1
                    else: 
                        if temp1[i][j-1] not in m:
                            m.append(temp1[i][j-1])
                if (j+1)<n:
                    if temp1[i][j]==temp1[i][j+1]:
                        y=y+1
                    else: 
                        if temp1[i-1][j] not in m:
                            m.append(temp1[i-1][j])
                if y>0:
                    if len(m)==4:
                        logic=temp1[i+1][j]
                    else:
                        if 60 not in m:
                            logic=60
                        elif 20 not in m:
                            logic=20
                        elif 10 not in m:
                            logic=10
                        else:
                            logic=40
                h=random.randint(0,n-1)
                k=random.randint(0,n-1)
            
                flag1=0
                flag2=0
                c5=0
                for w in range(h,n):
                    if flag1==1:
                        break
                    for v in range(k,n):
                        c5=c5+1
                        if temp1[w][v]==logic:
                            t=temp1[i][j]
                            temp1[i][j]=temp1[w][v]
                            temp1[w][v]=t
                            flag1=1
                if flag1==0:
                    for w in range(0,h):
                        if flag2 ==1:
                            break
                        for v in range(0,k):
                            c5=c5+1
                            if temp1[w][v]==logic:
                                t=temp1[i][j]
                                temp1[i][j]=temp1[w][v]
                                temp1[w][v]=t
                                flag2=1
                if c5>=n*n:
                    ###
                    flag6=1
                    temp1=copy.deepcopy(temp)
                    logic=0
                    for i in range (0,n):
                        for j in range (0,n):
                        
                            m.append(temp1[i][j])
                            if (i-1)>=0:
                                if temp1[i][j]!=temp1[i-1][j]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i-1][j]
                                    temp1[i-1][j]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)


                            if (i+1)<n:
                                if temp1[i][j]!=temp1[i+1][j]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i+1][j]
                                    temp1[i+1][j]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)
                                  
                            if (j-1)>=0:
                                if temp1[i][j]!=temp1[i][j-1]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i][j-1]
                                    temp1[i][j-1]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)
                                  
                            if (j+1)<n:
                                if temp1[i][j]!=temp1[i][j+1]:
                                    t=temp1[i][j]
                                    temp1[i][j]=temp1[i][j+1]
                                    temp1[i][j+1]=t
                                    if temp1 not in visited:
                                        stack.append(temp1)

        if temp1 not in visited and flag6==0:
            stack.append(temp1)
def nothing():
    print("Error in choosing choice ")
if __name__ == "__main__":
    print("To search solution of n*n color board ")
    print("Use 1. BFS")
    print("Use 2. DFS")
    argument=int(input())
    if argument==1:
        bfs()
    elif argument==2:
        dfs()
    else:
        nothing()    
