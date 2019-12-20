import gym_2048
import gym
import numpy as np
import random
import copy
from itertools import permutations


def is_monotonoc(L):
    return all(x >= y for x, y in zip(L, L[1:])) or all(x <= y for x, y in zip(L, L[1:]))


def generate_monotonic_data():
    a = [True, False,True, False,True, False,True, False]

    b = list(permutations(a, 4))

    c = list(set(b))

    d = list(permutations(c+c, 2))

    return list(set(d))
monotonocity=generate_monotonic_data()

def get_monotonocity_index(a):
    l = []
    for MN in [a, a.T]:
        k = []
        for i in MN:
            k.append(is_monotonoc(i))

        l.append(tuple(k))

    return monotonocity.index(tuple(l))

def push_up(bb):
    s = 0
    s1=0

    b = copy.deepcopy(bb)
    b_new = copy.deepcopy(bb)

    for i in [0, 1, 2, 3]:
        l = []
        for j in range(0, 4):
            l.append(b[j][i])

        l = list(filter((0).__ne__, l))

        l_n = []
        while len(l) > 1:
            if l[0] == l[1] and l[0]!=0:
                l_n.append(2 * l[0])
                s = s + (2 * l[0])
                s1=s1+1
                l.pop(0)
                l.pop(0)

            else:
                l_n.append(l[0])
                l.pop(0)
        if len(l) == 1:
            l_n.append(l[0])
            l.pop(0)

        for k in range(4 - len(l_n)):
            l_n.append(0)

        for j in range(0, 4):
            b_new[j][i] = l_n[j]
    return b_new, s,s1*16

def push_down(bb):
    s = 0
    s1=0

    b = copy.deepcopy(bb)
    b_new = copy.deepcopy(bb)

    for i in [0, 1, 2, 3]:
        l = []
        for j in [3, 2, 1, 0]:
            l.append(b[j][i])

        l = list(filter((0).__ne__, l))

        l_n = []
        while len(l) > 1:
            if l[0] == l[1] and l[0]!=0:
                l_n.append(2 * l[0])
                s = s + (2 * l[0])
                s1=s1+1
                l.pop(0)
                l.pop(0)

            else:
                l_n.append(l[0])
                l.pop(0)
        if len(l) == 1:
            l_n.append(l[0])
            l.pop(0)

        for k in range(4 - len(l_n)):
            l_n.append(0)

        for j in range(0, 4):
            b_new[j][i] = l_n[3 - j]
    return b_new, s,s1


def push_left(bb):
    s = 0
    s1=0

    b = copy.deepcopy(bb)
    b_new = copy.deepcopy(bb)

    for i in [0, 1, 2, 3]:
        l = []
        for j in [0, 1, 2, 3]:
            l.append(b[i][j])

        l = list(filter((0).__ne__, l))

        l_n = []
        while len(l) > 1:
            if l[0] == l[1] and l[0]!=0:
                l_n.append(2 * l[0])
                s = s + (2 * l[0])
                s1=s1+1
                l.pop(0)
                l.pop(0)

            else:
                l_n.append(l[0])
                l.pop(0)
        if len(l) == 1:
            l_n.append(l[0])
            l.pop(0)

        for k in range(4 - len(l_n)):
            l_n.append(0)

        for j in range(0, 4):
            b_new[i][j] = l_n[j]

    return b_new, s,s1


def push_right(bb):
    s = 0
    s1=0

    b = copy.deepcopy(bb)
    b_new = copy.deepcopy(bb)
    for i in [0, 1, 2, 3]:
        l = []
        for j in [3, 2, 1, 0]:
            l.append(b[i][j])

        l = list(filter((0).__ne__, l))

        l_n = []
        while len(l) > 1:
            if l[0] == l[1] and l[0]!=0:
                l_n.append(2 * l[0])
                s = s + (2 * l[0])
                s1=s1 + 1 
                l.pop(0)
                l.pop(0)
            else:
                l_n.append(l[0])
                l.pop(0)
        if len(l) == 1:
            l_n.append(l[0])
            l.pop(0)

        for k in range(4 - len(l_n)):
            l_n.append(0)

        for j in range(0, 4):
            b_new[i][j] = l_n[3 - j]

    return b_new, s,s1
def merges(bb):
    b=copy.deepcopy(bb)
    count=push_down(b)[2]+push_left(b)[2]
    # print("Merges : ",push_down(b)[2]+push_left(b)[2])
    return count


def is_done(bb):
    b = copy.deepcopy(bb)

    if b == push_down(b)[0] and b == push_up(b)[0] and b == push_left(b)[0] and b == push_right(b)[0]:
        return True
    else:
        return False

def numberofzeroes(bb):
    count = 0
    b = copy.deepcopy(bb)

    for i in range(4):
        for j in range(4):
            if b[i][j] == 0:
                count = count + 1
    return count


if __name__ == '__main__':
    env = gym.make('2048-v0')
    env.seed(42)
    q_table=np.zeros((256,16,9,4))
    # print(q_table)

    env.reset()
    env.render()
    done = False
    moves = 0
    episodes=100
    discount_factor=0.6
    explore_rate=0.2
    state_initial=(0,0,0)
    learning_rate=0.1
    total_reward=0
    # print("Environmet :",env.action_space.n)
    for i in range(episodes):
        env.reset()
     
        print("Iteration : ",i+1)
        counter=0
        while True:
            print()
            counter=counter+1
            env.render()
        
            p=0
            p=random.random()
            if p<explore_rate:
                action=env.action_space.sample()
            else:
                count=0
                for i in (q_table[state_initial[0],state_initial[1],state_initial[2]]):
                    if i==0.0:
                        count=count+1
                if count==4:
                    action=random.randint(0,3)
                else:
                    action=np.argmax(q_table[state_initial[0],state_initial[1],state_initial[2]])
                pass
            
            
            obs,reward,done,extras = env.step(action+1)
            print("Action : ",action+1)
            total_reward=total_reward + reward
            # print("Obs: \n",obs)
            count1=merges(copy.deepcopy(obs))
            z=numberofzeroes(copy.deepcopy(obs))
            monoton1=get_monotonocity_index(np.array(obs))
            # print("Zeroes",z)
            # print("Monotonci",monoton1)
        
            q_alpha=np.max(q_table[monoton1,z,count1])
            q_table[state_initial][action]=q_table[state_initial][action]+learning_rate*(reward + discount_factor*q_alpha - q_table[state_initial][action])
            state_initial=copy.deepcopy((monoton1,z,count1))

            if done:
                break
            ########3


            # print("Environmet :",env.action_space.n)

            # action = env.np_random.choice(range(4), 1).item()
            # next_state, reward, done, info = env.step(action)
            # moves += 1

            # print('Next Action: "{}"\n\nReward: {}'.format(
            # gym_2048.Base2048Env.ACTION_STRING[action], reward))
            # env.render()
            # print("Environmet :",env.action_space.n)

    # print('\nTotal Moves: {}'.format(moves))
    # print("Environmet :",env.action_space.n)