import sys
import numpy as np
import gym
import gym_maze
import random
import math
import matplotlib.pyplot as plt
def sarsa():
    episode=500
    #Maximum Steps
    maximum_steps=200
    #Learning Rate
    learning_rate=0.2

    discount_factor=0.2
    explore_rate=0.2
    state_initial=0
    q_table=[]
    for i in range(25):
        s=[]
        for j in range(4):
            s.append(0)
        q_table.append(s)
    # print(q_table)
    total_reward1=-math.inf
    total_reward=0
    counter=0
    global iterations
    global steps
    iterations=[]
    steps=[]
    count=0
    for i in range(episode):
        iterations.append(i)
        steps.append(count)
        env.reset()
        if total_reward==total_reward1:
                counter=counter + 1
        if counter==5:
            print("Episodes taken for Convergence : ",i-5)
            break
        total_reward1=total_reward
        total_reward=0
        
        count=0
        while True:
            count=count+1
            env.render()
        
            p=0
            p=random.random()
            if p<explore_rate:
                action=env.action_space.sample()
            else:
                count2=0
                l=q_table[state_initial][0]
                for k in range(len(q_table[state_initial])):
                    if l ==q_table[state_initial][k]:
                        count2=count2+1
                if count2==len(q_table[state_initial]):
                    action=random.randint(0,3)
                   
                else:
                    action=q_table[state_initial].index(max(q_table[state_initial]))
                pass
            
            obs,reward,done,extras = env.step(action)
            total_reward=total_reward + reward
            
            
            p=0
            p=random.random()
            if p<explore_rate:
                action1=env.action_space.sample()
            else:
                action1=q_table[obs[0]*5+obs[1]].index(max(q_table[obs[0]*5+obs[1]]))
                pass
            
            q_alpha=q_table[obs[0]*5+obs[1]][action1]
            q_table[state_initial][action]=q_table[state_initial][action]+learning_rate*(reward + discount_factor*q_alpha - q_table[state_initial][action])
            state_initial=obs[0]*5+obs[1]
            if state_initial==24:
                break

def q_learning():
    episode=500
 
    #Learning Rate
    learning_rate=0.2

    discount_factor=0.2
    explore_rate=0.2
    state_initial=0
    q_table=[]
    for i in range(25):
        s=[]
        for j in range(4):
            s.append(0)
        q_table.append(s)
    # print(q_table)
    total_reward1=-math.inf
    total_reward=0
    counter=0
    global iterations
    global steps
    iterations=[]
    steps=[]
    count=0
    for i in range(episode):
        iterations.append(i)
        steps.append(count)
        env.reset()
        if total_reward==total_reward1:
                counter=counter + 1
        if counter==5:
            print("Episodes taken for Convergence : ",i)
            break
        total_reward1=total_reward
        total_reward=0
        count=0
        p=0
        while True:
            count=count+1
            env.render()
            p=random.random()
            if p<explore_rate:
                action=env.action_space.sample()
            else:
                count2=0
                l=q_table[state_initial][0]
                for k in range(len(q_table[state_initial])):
                    if l ==q_table[state_initial][k]:
                        count2=count2+1
                if count2==len(q_table[state_initial]):
                    action=random.randint(0,3)
                   
                else:
                    action=q_table[state_initial].index(max(q_table[state_initial]))
            
            obs,reward,done,extras = env.step(action)
            total_reward=total_reward + reward
            q_alpha=max(q_table[obs[0]*5+obs[1]])
            q_table[state_initial][action]=q_table[state_initial][action]+learning_rate*(reward+discount_factor*q_alpha-q_table[state_initial][action])
            state_initial=obs[0]*5+obs[1]
            if state_initial==24 or done ==True:
                
                break
            # print("End ",i+1)
    # print(q_table)
    print("Done")
    env1 = gym.make("maze-random-5x5-v0")
    state_initial=0 
    env1.reset()
    while True:
        # count=count+1
        env1.render()
        p=random.random()
        # if p<explore_rate:
        #action=env.action_space.sample()
        # else:
        action=q_table[state_initial].index(max(q_table[state_initial]))
        
        obs,reward,done,extras = env1.step(action)
        # total_reward=total_reward + reward
        q_alpha=max(q_table[obs[0]*5+obs[1]])
        # q_table[state_initial][action]=q_table[state_initial][action]+learning_rate*(reward+discount_factor*q_alpha-q_table[state_initial][action])
        state_initial=obs[0]*5+obs[1]
        if state_initial==24 or done ==True:
            
            break

steps=[]
iterations=[]
env = gym.make("maze-random-5x5-v0")
if __name__=='__main__':
    
    print("1. Q - learning ")
    print("2. SARSA ")
    print("3. For Comparing Both")
    count1=0
 
    while True:
        choice=int(input("Enter the Choice : "))
        
        # env = gym.make("maze-random-5x5-v0")
        if choice ==1:
            f=0
            
            q_learning()
        
        elif choice ==2:
            # env = gym.make("maze-random-5x5-v0")
            f=1
            sarsa()
        elif choice ==3:
            q_learning()
            env.reset()
            sarsa()
            # env = gym.make("maze-random-5x5-v0")
            f=2
            print("Wrong Choice ")
        if f==0:
            plt.plot(iterations[1:],steps[1:],count1)
            plt.ylabel('Steps')
            plt.xlabel('Episodes')
            plt.title("Q- Learning Analysis")
            plt.show()
        elif f==1:
            plt.plot(iterations[1:],steps[1:],count1)
            plt.ylabel('Steps')
            plt.xlabel('Episodes')
            plt.title("SARSA Learning  Analysis")
            plt.show()
        else:
            pass
        count1=count1+1
    
     
    
    
    
  
    
