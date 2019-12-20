
import copy
import math
countz=0
def check(tic):
    if (tic[0]==tic[1] and tic[1]==tic[2] and tic[0]=='X') or (tic[3]==tic[4] and tic[4]==tic[5] and tic[4]=='X') or(tic[6]==tic[7]and tic[7]==tic[8]and tic[8]=='X'):
        return -1
    if (tic[0]==tic[1] and tic[1]==tic[2] and tic[0]=='O') or (tic[3]==tic[4] and tic[4]==tic[5] and tic[4]=='O') or(tic[6]==tic[7]and tic[7]==tic[8]and tic[8]=='O'):
        return 1
    if (tic[0]==tic[3] and tic[3]==tic[6] and tic[0]=='X') or (tic[1]==tic[4] and tic[4]==tic[7] and tic[1]=='X') or (tic[2]==tic[5] and tic[5]==tic[8] and tic[2]=='X'):
        return -1
    if (tic[0]==tic[3] and tic[3]==tic[6] and tic[0]=='O') or (tic[1]==tic[4] and tic[4]==tic[7] and tic[1]=='O') or (tic[2]==tic[5] and tic[5]==tic[8] and tic[2]=='O'):
        return 1
    if (tic[0]==tic[4] and tic[4]==tic[8] and tic[0]=='X') or (tic[2]==tic[4]and tic[4]==tic[6] and tic[2]=='X'):
        return -1
    if (tic[0]==tic[4] and tic[4]==tic[8] and tic[0]=='O') or (tic[2]==tic[4]and tic[4]==tic[6] and tic[2]=='O'):
        return 1
    count1=0
    for i in range(9):
        if tic[i]==' ':
            count1=count1+1
    if count1>0:
        return -10
    else:
        return 0

def recerminmax1(tic2,flag,a,b):#used third return value as dummy
    global countz
    countz=countz+1
    if check(tic2)==1:
        return (1,copy.deepcopy(tic2),[],1,math.inf)
    if check(tic2)==0 and flag==1:
        return (0,copy.deepcopy(tic2),[],-math.inf,0)
    if check(tic2)==0 and flag==0:
        return (0,copy.deepcopy(tic2),[],0,math.inf)
    if check(tic2)==-1:
        return (-1,copy.deepcopy(tic2),[],-math.inf,-1)
    #print("Iteration")
    #print(tic2)
    #print("For each state Alpha :",a)
    #print("For each state Beta: ",b)
    power=[]
    node=[]
   
    for i in range(9):
        
        if tic2[i]==' ':
            if flag==1:
                tic2[i]='O'
                #print("Isme1")
                t,s,f,c,d=recerminmax1(copy.deepcopy(tic2),0,a,b)
                #print("Alpha :",a)
                #print("Beta: ",b)
                power.append(t)
                node.append(s)

                if t>=b:
                    #print("Pruning is done 1")
                    q=power.index(max(power))
                    g=node[q]
                    if t>a:
                        a=t
                    return max(power),tic2,g,a,b
                   
                if t>a:
                    a=t
                    #print("Updation in alpha 1")
            
                #print("Completed 1")
                #print(s)
                tic2[i]=' '
                
                flag=1
                #print(" S : ",s)
                

            else:
                tic2[i]='X'
                #print("Isme2")
                t,s,f,c,d=recerminmax1(copy.deepcopy(tic2),1,a,b)
                #print("Alpha :",a)
                #print("Beta: ",b)
                power.append(t)
                node.append(s)
                if t<=a:
                    #print("Pruning is done 2")
                    q=power.index(min(power))
                    
                    g=node[q]
                    if t<b:
                        b=t
                    return min(power),tic2,g,a,b
                if t<b:
                    b=t
                    #print("Updation in beta 1")
                #print("Completed 2")
                tic2[i]=' '
                
                #print(" S :",s)
                flag=0
                
    #print("Power :",power)
    #print("Node : ",node[power.index(max(power))])
    if flag==1:
        q=power.index(max(power))
        g=node[q]
        return max(power),tic2,g,a,b
    else:
        q=power.index(min(power))
      
        g=node[q]
        return min(power),tic2,g,a,b



def recerminmax(tic2,flag):
    
    #used third return value as dummy
    global countz
    countz=countz+1
    if check(tic2)==1:
        return (1,copy.deepcopy(tic2),[])
    if check(tic2)==0:
        return (0,copy.deepcopy(tic2),[])
    if check(tic2)==-1:
        return (-1,copy.deepcopy(tic2),[])
    #print("Iteration")
    #print(tic2)


    power=[]
    node=[]
   
    for i in range(9):
        if tic2[i]==' ':
            if flag==1:
                tic2[i]='O'
                #print("Isme1")
                t,s,f=recerminmax(copy.deepcopy(tic2),0)
                #print("Completed 1")
                #print(s)
                tic2[i]=' '
                
                flag=1
                #print(" S : ",s)
                power.append(t)
                node.append(s)

            else:
                tic2[i]='X'
               # print("Isme2")
                t,s,f=recerminmax(copy.deepcopy(tic2),1)
               # print("Completed 2")
                tic2[i]=' '
                
                #print(" S :",s)
                flag=0
                power.append(t)
                node.append(s)
    #print("Power :",power)
    #print("Node : ",node[power.index(max(power))])
    if flag==1:
        q=power.index(max(power))
        g=node[q]
        return max(power),tic2,g
    else:
        q=power.index(min(power))
      
        g=node[q]
        return min(power),tic2,g


    
    
def newstate(tic4,flag):
    tic3=copy.deepcopy(tic4)
    
    m,n,b=recerminmax(copy.deepcopy(tic3),flag)
    return b
     
def minimax(tic):
    global countz
    tic1=copy.deepcopy(tic)
    sum=0
    count=0
    while (check(tic1)!=1 and check(tic1)!=-1 and check(tic1)!=0 and count<=8):
        if count%2==0:  #Chance of User
            print("Enter the move ")
            move=int(input())
            if (tic1[move-1]=='X' or tic1[move-1]=='O' or move<1 or move>9 or tic1[move-1]=='O'):
                print("Invalid move or Already occupied Space")
                continue
            tic1[move-1]='X'
            print("Move By User")
            for i in range(3):
                print("|",tic1[3*i],"|",tic1[3*i+1],"|",tic1[3*i+2],"|")
            count=count+1
        else:
            flag=1
           # print("Bug")
            tic1=newstate(copy.deepcopy(tic1),flag)
            print("Node traced : ")
            print(countz-sum)
            sum=countz
           # print("Bug2")
            print("Move By System")
            for i in range(3):
                print("|",tic1[3*i],"|",tic1[3*i+1],"|",tic1[3*i+2],"|")
            count=count+1
    if check(tic1)==-1:
        print("User Win ")
    elif(check(tic1)==1):
        print("Computer Win")
    elif(check(tic1)==0):
        print("Draw")
    else:
        print("Some Error Occured")
def newstate1(tic4,flag):
    tic3=copy.deepcopy(tic4)
    a=-math.inf
    b=math.inf
    #print("Original Alpha :",a)
    #print("Original Beta: ",b)
    m,n,f,a,b=recerminmax1(copy.deepcopy(tic3),flag,a,b)
    return f

def alphabeta(tic):
    tic1=copy.deepcopy(tic)
    count=0
    sum=0
    global countz
    while (check(tic1)!=1 and check(tic1)!=-1 and check(tic1)!=0 and count<=8):
        if count%2==0:  #Chance of User
            print("Enter the move ")
            move=int(input())
            if (tic1[move-1]=='X' or tic1[move-1]=='O' or move<1 or move>9 or tic1[move-1]=='O'):
                print("Invalid move or Already occupied Space")
                continue
            tic1[move-1]='X'
            print("Move By User")
            for i in range(3):
                print("|",tic1[3*i],"|",tic1[3*i+1],"|",tic1[3*i+2],"|")
            count=count+1
        else:
            flag=1
            #print("Bug")
            tic1=newstate1(copy.deepcopy(tic1),flag)
            #print("Bug2")
            print("Nodes Traced : ")
            print(countz-sum)
            sum=countz
        
            print("Move By System")
            for i in range(3):
                print("|",tic1[3*i],"|",tic1[3*i+1],"|",tic1[3*i+2],"|")
            count=count+1
    if check(tic1)==-1:
        print("User Win ")
    elif(check(tic1)==1):
        print("Computer Win")
    elif(check(tic1)==0):
        print("Draw")
    else:
        print("Some Error Occured")
    pass
def nothing():
    print("Error in choosing choice ")
if __name__ == "__main__":
    print(".........Tic Tac Toe...........")

    tic=[]
    j=0
    
    tic=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
    for i in range(3):
        print("|",tic[3*i],"|",tic[3*i+1],"|",tic[3*i+2],"|")
        
    print("Start Play by entering the Choice ")
    print("1. Using Minimax")
    print("2. AlphaBeta Pruning")
    choice = int(input())
    if choice == 1:
        minimax(tic)
        pass
        
    elif choice == 2:
        alphabeta(tic)
        pass
        
    else:
        nothing()
