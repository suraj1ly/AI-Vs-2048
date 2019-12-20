import gym_2048
import gym
import numpy as np
import random
import copy

from itertools import permutations
from collections import Counter


def push_up(bb):
    s = 0
    s1 = 0

    b = copy.deepcopy(bb)
    b_new = copy.deepcopy(bb)

    for i in [0, 1, 2, 3]:
        l = []
        for j in range(0, 4):
            l.append(b[j][i])

        l = list(filter((0).__ne__, l))

        l_n = []
        while len(l) > 1:
            if l[0] == l[1] and l[0] != 0:
                l_n.append(2 * l[0])
                s = s + (2 * l[0])
                s1 = s1 + 1
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
    return b_new, s, s1 * 16


def push_down(bb):
    s = 0
    s1 = 0

    b = copy.deepcopy(bb)
    b_new = copy.deepcopy(bb)

    for i in [0, 1, 2, 3]:
        l = []
        for j in [3, 2, 1, 0]:
            l.append(b[j][i])

        l = list(filter((0).__ne__, l))

        l_n = []
        while len(l) > 1:
            if l[0] == l[1] and l[0] != 0:
                l_n.append(2 * l[0])
                s = s + (2 * l[0])
                s1 = s1 + 1
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
    return b_new, s, s1


def push_left(bb):
    s = 0
    s1 = 0

    b = copy.deepcopy(bb)
    b_new = copy.deepcopy(bb)

    for i in [0, 1, 2, 3]:
        l = []
        for j in [0, 1, 2, 3]:
            l.append(b[i][j])

        l = list(filter((0).__ne__, l))

        l_n = []
        while len(l) > 1:
            if l[0] == l[1] and l[0] != 0:
                l_n.append(2 * l[0])
                s = s + (2 * l[0])
                s1 = s1 + 1
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

    return b_new, s, s1


def push_right(bb):
    s = 0
    s1 = 0

    b = copy.deepcopy(bb)
    b_new = copy.deepcopy(bb)
    for i in [0, 1, 2, 3]:
        l = []
        for j in [3, 2, 1, 0]:
            l.append(b[i][j])

        l = list(filter((0).__ne__, l))

        l_n = []
        while len(l) > 1:
            if l[0] == l[1] and l[0] != 0:
                l_n.append(2 * l[0])
                s = s + (2 * l[0])
                s1 = s1 + 1
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

    return b_new, s, s1


def is_done(bb):
    b = copy.deepcopy(bb)

    if b == push_down(b)[0] and b == push_up(b)[0] and b == push_left(b)[0] and b == push_right(b)[0]:
        return True
    else:
        return False


def is_monotonic(L):
    return all(x >= y for x, y in zip(L, L[1:])) or all(x <= y for x, y in zip(L, L[1:]))

def get_total_merges(bb):
    b = copy.deepcopy(bb)
    count = push_down(b)[2] + push_left(b)[2]
    # print("Merges : ",push_down(b)[2]+push_left(b)[2])
    return count



def generate_monotonic_data():
    a = [True, False, True, False, True, False, True, False]

    b = list(permutations(a, 4))

    c = list(set(b))

    d = list(permutations(c + c, 2))

    return list(set(d))


def get_monotonicity_index(a):
    l = []
    for MN in [a, a.T]:
        k = []
        for i in MN:
            k.append(is_monotonic(i))

        l.append(tuple(k))

    return Monotonicity_master_data.index(tuple(l)), Counter(l)[True], Counter(l)[False]


def get_empty_cells(bb):
    count = 0
    b = copy.deepcopy(bb)

    for i in range(4):
        for j in range(4):
            if b[i][j] == 0:
                count = count + 1
    return count


Monotonicity_master_data = generate_monotonic_data()

env = gym.make('2048-v0')
# env.seed(42)

Q = np.zeros((256, 16, 9, 4))

env.reset()
env.render()

done = False

moves = 0
episodes = 100

explore_rate = 0.02
discount_factor = 0.8
learning_rate = 0.8

total_reward = 0

state = (0, 0, 0)

dump = []

for iteration in range(1, episodes + 1):
    env.reset()

    # print("Iteration : ", iteration)

    counter = 0

    while True:

        # print("")
        counter += 1

        # env.render()

        p = 0
        p = random.random()

        if p < explore_rate:
            action = env.action_space.sample()
        else:
            count = 0
            for i in (Q[state[0], state[1], state[2]]):
                if i == 0.0:
                    count = count + 1
            if count == 4:
                action = random.randint(0, 3)
            else:
                action = np.argmax(Q[state[0], state[1], state[2]])
            pass

        observation, reward, done, _ = env.step(action + 1)

        # print("Action : ", action + 1)

        merges = get_total_merges(observation)
        empty_cells = get_empty_cells(observation)
        monotonicity = get_monotonicity_index(np.array(observation))

        # print(reward)
        reward = merges + 10 * empty_cells + 10 * monotonicity[1] - 5 * monotonicity[2]

        dump.append((list(observation),reward, action))

        # print(reward)
        total_reward = total_reward + reward

        q_alpha = np.max(Q[monotonicity[0], empty_cells, merges])

        Q[state][action] += learning_rate * (reward + discount_factor * q_alpha - Q[state][action])

        state = (monotonicity[0], empty_cells, merges)

        if done:
            print("\n\nIteration : ", iteration)
            print(observation)
            print("")
            print("Unique Q:", (np.count_nonzero(Q)))
            break
