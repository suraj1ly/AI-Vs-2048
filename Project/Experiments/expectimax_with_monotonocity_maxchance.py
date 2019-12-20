codeimport copy
import random
import math
import numpy as np
import time
from collections import Counter
def is_sorted(l):
    return all(a <= b for a, b in zip(l, l[1:]))
def calculate(board1):
    b = copy.deepcopy(board1)
    sum = 0
    for i in range(3):
        for j in range(3):
            sum = sum + b[i][j] * boardm1[i][j]
    return sum


def is_monotonoc(L):
    return all(x >= y for x, y in zip(L, L[1:])) or all(x <= y for x, y in zip(L, L[1:]))

def monotonocity_hueristics(b):
    count = 0
    for i in b:
        if not is_monotonoc(i):
            count =count+1

    t_matrix = zip(*b)

    for i in t_matrix:
        if not is_monotonoc(i):
            count =count+1

    return (-1)*count*16

def monotonocity_hueristics2(b):
 
    count1=0
    count2=0
    count3=0
    for i in b:
        if not is_monotonoc(i):
            
            count3=count3+1
    if count3==0:
        count1=count1+1
    

    t_matrix = zip(*b)

    for i in t_matrix:
        if not is_monotonoc(i):
            
            count2=count2+1
    if count2==0:
        count1=count1+1
    
        

    return count1*16
def cal(board):
    s1=0
    l=board[0][0]
    l1=0
    l2=0
    for i in range(4):
        for j in range(4):
            if board[i][j]>l:
                l=board[i][j]
                l1=i
                l2=j
    if l1==0 and (l2==0 or l2==3):
        s1=1
    if l1==3 and(l2==0 or l2==3):
        s1=1
    return s1 *16

def calculate_total_hueristics(b):
    return  (numberofzeroes(b)*8 + cal(b) +monotonocity_hueristics2(b) + monotonocity_hueristics(b))




def numberofzeroes(bb):
    count = 0
    b = copy.deepcopy(bb)

    for i in range(4):
        for j in range(4):
            if b[i][j] == 0:
                count = count + 1
    return count





def is_done(bb):
    b = copy.deepcopy(bb)

    if b == push_down(b)[0] and b == push_up(b)[0] and b == push_left(b)[0] and b == push_right(b)[0]:
        return True
    else:
        return False


def print_board(bb):
    b = copy.deepcopy(bb)
    for i in b:
        print(i)


def find_zeros(bb):
    b = copy.deepcopy(bb)
    list = []
    for i in range(4):
        for j in range(4):
            if b[i][j] == 0:
                list.append((i, j))
    return list


def pick_random_place(bb):
    b = copy.deepcopy(bb)
    list = find_zeros(b)
    return random.choice(list)


def place_random(bb):
    global choices
    b = copy.deepcopy(bb)
    picked_location = pick_random_place(b)
    q = random.randint(0, 100)
    f = 0  # since i am checking only for 2 as min
    if q < 80:

        f = 0
    else:
        f = 1

    b[picked_location[0]][picked_location[1]] = choices[f]
    # print_board(b)
    return b


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
            if l[0] == l[1]:
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
            if l[0] == l[1]:
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
            if l[0] == l[1]:
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
            if l[0] == l[1]:
                l_n.append(2 * l[0])
                s = s + (2 * l[0])
                s1=0
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


# score = 0

# while not is_done(board):
#     try:
#         print("is Done:", is_done(board))
#         choice = int(input("\nChoice:\n1.Left\n2.Right\n3.Up\n4.Down"))
#
#         t = 1
#
#         print("")
#
#         if choice == 1:
#             result = push_left(board)
#
#         elif choice == 2:
#             result = push_right(board)
#
#         elif choice == 3:
#             result = push_up(board)
#
#         elif choice == 4:
#             result = push_down(board)
#
#         if result[0] != board:
#             board = copy.deepcopy(result[0])
#             print_board(board)
#             score = score + result[1]
#         else:
#             t = 0
#
#         if t == 1:
#             board = place_random(board)
#
#             print("\n\n===========================================\n\nScore", score, "\n")
#
#             print_board(board)
#         else:
#             print("\nNot a Valid Move")
#     except:
#         print("Exception")
def max1(b):
    l = b[0][0]
    for i in range(4):
        for j in range(4):
            if b[i][j] > l:
                l = b[i][j]
    return l


def minimax(board, is_maximising, depth, alpha, beta, score, action, max_depth):
    global choices

    # print("depth:", depth, score)
    # print_board(board)

    if is_done(board):
        return score, 0, action

    if depth == max_depth:
        # print("Depth Reached", depth)
        return (calculate_total_hueristics(board)), 0, action

    if is_maximising == 1:

        # print("\n\n***Max")

        actions = ['up', 'down', 'left', 'right']

        best = -math.inf
        best_move = actions[0]

        for i in actions:
            temp_board = []
            temp_board = copy.deepcopy(board)
            # print("\nAction", i)

            if i == 'left':
                result = push_left(temp_board)

            elif i == 'right':
                result = push_right(temp_board)

            elif i == 'up':
                result = push_up(temp_board)

            elif i == 'down':
                result = push_down(temp_board)

            if result[0] != board:
                temp_board = copy.deepcopy(result[0])
                # print_board(temp_board)

                return_value = minimax(temp_board, 2, depth + 1, alpha, beta, (result[2] +calculate_total_hueristics(temp_board)), action + " " + i, max_depth)
                if best < return_value[0]:
                    # print("Return at Max: ", return_value[0], best, i, "Depth:", depth)
                    # print("Replacing at Max with", return_value[0], best)
                    best = return_value[0]
                    best_move = i
                # alpha = max(alpha, best)
                # if beta <= alpha:
                #     return score, best_move, action
                # if len(choices) == 1:
                #     if alpha < best:
                #         alpha = best
                #     if beta <= alpha:
                #         break
        return best, best_move, action

    elif is_maximising == 2:
        empty = find_zeros(board)
        # print(empty)

        if len(empty) == 0:
            return score, 0

        # print("\n\n***Min")
        best_min = +math.inf
        best_min_move = empty[0]

        for i in empty:
            temp_board = copy.deepcopy(board)
            temp_board[i[0]][i[1]] = 2
            return_value = minimax(temp_board, 1, depth, alpha, beta, (calculate_total_hueristics(temp_board)), action, max_depth)
            return_value1 = minimax(temp_board, 1, depth, alpha, beta, ( calculate_total_hueristics(temp_board)), action, max_depth)
            # print("Return at Min: ", return_value)
            # if best_min > return_value[0]:
            # print("Replacing at Min with", return_value[0], best_min)
            best_min = 0.8 * return_value[0] + 0.2 * return_value1[0]
            best_min_move = i
            # beta = min(beta, best_min)
            # if beta <= alpha:
            #     return score, best_min_move, action
            # if len(choices) == 1:
            #     if beta > best_min:
            #         beta = best_min
            #     if beta <= alpha:
            #         break

        return best_min, best_min_move
    else:
        h = []

        best = 0
        flag = 0
        temp_board = copy.deepcopy(board)
        for i in range(len(temp_board)):
            if flag == 1:
                break
            for j in range(len(temp_board)):
                if temp_board[i][j] == -1:

                    for num in choices:
                        best_min_move = num
                        temp_board[i][j] = num
                        return_value = minimax(temp_board, 1, depth, alpha, beta, ( calculate_total_hueristics(temp_board)), action, max_depth)
                        h.append(return_value[0])

                    best = 0.8 * h[0] + 0.2 * h[1]
                    flag = 1
                    break
        return best, best_min_move

        pass


boardm1 = [[7, 6,  5, 4],
          [3, 4, 5, 6],
          [2, 3, 4,  5],
          [ 1, 2,  3, 4]]

board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
score1 = 0
choices = [2, 4]

score = 0

max_depth = 3

board = place_random(board)
arr = []

boardm = [[1,0,0, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [1,0,0, 1]]
def tristy(a):
    print("cores")
    master_score = []
    high_value = []
    for ii in range(2):

        boardm = [[1,0,0, 1],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [1,0,0, 1]]

        board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        score1 = 0
        choices = [2, 4]

        score = 0

        max_depth = 2

        board = place_random(board)
        arr = []

        while not is_done(board):
            t = minimax(board, 1, 0, float("-inf"), float("inf"), score, "", max_depth)[1]
            # print("\nFinal Action:", t)
            if t == 'left':
                result = push_left(board)

            elif t == 'right':
                result = push_right(board)

            elif t == 'up':
                result = push_up(board)

            elif t == 'down':
                result = push_down(board)

            if result[0] != board:
                board = copy.deepcopy(result[0])
                print_board(board)
                print()
                score1 = score1 + result[1]
                score = result[1] + calculate_total_hueristics(board)
                # print("\n")
                # print("=" * 20)
                # print("score", score1)
                # print("Final----")
                board = place_random(board)

            if is_done(board):
                print("")
                print("-----Iteration", ii, "------")
                print_board(board)
                print("Score", score1)
                master_score.append(score1)

                a = np.array(board)

                b = a.ravel()

                b.sort()

                c = b[15:]
                print("Max Value:", c)
                high_value.append(c[0])

    print("")
    print("\n\n#############Final Results#############")
    print(master_score)
    print(high_value)
    print("Frequency:", Counter(high_value))
    print("Max Score:", max(master_score))
    print("Avg Score:", sum(master_score) / len(master_score))
    print("\n\n")


# tristy("")
import time
from collections import Counter

start = time.time()

from multiprocessing import Pool

if __name__ == '__main__':
    p = Pool(1)
    p.map(tristy, [1])

elapsed = time.time() - start
print("Time: %.08f" % elapsed)

# 0.07017900 - 2 CORES


