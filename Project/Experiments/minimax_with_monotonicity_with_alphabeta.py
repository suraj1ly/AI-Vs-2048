import copy
import random
import math
from timeit import default_timer as timer
def is_sorted(l):
    return all(a <= b for a, b in zip(l, l[1:]))
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


def numberofzeroes(b):
    count = 0

    for i in range(4):
        for j in range(4):
            if b[i][j] == 0:
                count = count + 1
    return count



def calculate_total_hueristics(b):
    return (numberofzeroes(b) * 16 + monotonocity_hueristics(b) + monotonocity_hueristics2(b))


def is_done(b):
    if b == push_down(b)[0] and b == push_up(b)[0] and b == push_left(b)[0] and b == push_right(b)[0]:
        return True
    else:
        return False


def print_board(b):
    for i in b:
        print(i)


def find_zeros(b):
    list = []
    for i in range(4):
        for j in range(4):
            if b[i][j] == 0:
                list.append((i, j))
    return list


def pick_random_place(b):
    list = find_zeros(b)
    return random.choice(list)


def place_random(bb):
    b = copy.deepcopy(bb)
    picked_location = pick_random_place(b)
    # q = random.randint(0, 100)
    # f = 2  # since i am checking only for 2 as min
    # if q < 80:

    #     f = 2
    # else:
    #     f = 4

    b[picked_location[0]][picked_location[1]] = random.choice(choices)
    print_board(b)
    return b


def push_up(bb):
    s = 0
    merges = 0

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
                merges += 1
                s = s + (2 * l[0])
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
    return b_new, s, merges


def push_down(bb):
    s = 0
    merges = 0

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
                merges += 1
                s = s + (2 * l[0])
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
    return b_new, s, merges


def push_left(bb):
    s = 0
    merges = 0

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
                merges += 1
                s = s + (2 * l[0])
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

    return b_new, s, merges


def push_right(bb):
    s = 0
    merges = 0

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
                merges += 1
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

    return b_new, s, merges


# def calculate_snake_weight(b):
#     sum = 0
#     for i in range(3):
#         for j in range(3):
#             sum = sum + b[i][j] * snake_weights[i][j]
#     return sum

# def non_decreasing(L):
#     return all(x<=y for x, y in zip(L, L[1:]))

def minimax(board, is_maximising, depth, alpha, beta, score, action, max_depth):
    global choices

    # print("depth:", depth, score)
    # print_board(board)

    if is_done(board):
        return score, 0, action

    if depth == max_depth:
        # print("Depth Reached", depth)
        return (score + calculate_total_hueristics(board)), 0, action

    if is_maximising:

        # print("\n\n***Max")

        actions = ['up', 'down', 'left', 'right']

        best = -math.inf
        best_move = actions[0]

        for i in actions:
            temp_board = []
            temp_board = copy.deepcopy(board)

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

                # print("Result1:", result[1])

                # print(score, result[1] * int(math.sqrt(score)), result[2] * int(math.sqrt(score)), numberofzeroes(temp_board) * 10 * int(math.sqrt(score))), monotonocity_hueristics(temp_board) * int(math.sqrt(score))

                return_value = minimax(temp_board, False, depth + 1, alpha, beta, (score + result[1]) + result[2] + calculate_total_hueristics(board), action + " " + i,
                                       max_depth)
                if best < return_value[0]:
                    # print("Return at Max: ", return_value[0], best, i, "Depth:", depth)
                    # print("Replacing at Max with", return_value[0], best)
                    best = return_value[0]
                    best_move = i
                alpha = max(alpha, best)
                if beta <= alpha:
                    return score, best_move, action
                if len(choices) == 1:
                    if alpha < best:
                        alpha = best
                    if beta <= alpha:
                        break
        return best, best_move, action

    else:
        empty = find_zeros(board)
        # print(empty)

        if len(empty) == 0:
            return score, 0

        # print("\n\n***Min")
        best_min = +math.inf
        best_min_move = empty[0]

        for num in choices:
            for i in empty:
                temp_board = copy.deepcopy(board)
                temp_board[i[0]][i[1]] = num
                return_value = minimax(temp_board, True, depth, alpha, beta, (score + calculate_total_hueristics(board)), action, max_depth)
                # print("Return at Min: ", return_value)
                if best_min > return_value[0]:
                    # print("Replacing at Min with", return_value[0], best_min)
                    best_min = return_value[0]
                    best_min_move = i
                beta = min(beta, best_min)
                if beta <= alpha:
                    return score, best_min_move, action
                if len(choices) == 1:
                    if beta > best_min:
                        beta = best_min
                    if beta <= alpha:
                        break

        return best_min, best_min_move


# board = [[2, 16, 4, 8],
#          [8, 4, 32, 4],
#          [2, 32, 16, 8],
#          [4, 4, 2, 0]]
#
# snake_weights = [[15, 14, 13, 12],
#                  [8, 9, 10, 11],
#                  [7, 6, 5, 4],
#                  [0, 1, 2, 3]]

board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
score1 = 0
choices = [2]

score = 0

max_depth = 2

board = place_random(board)

while not is_done(board):

    start = timer()

    t = minimax(board, True, 0, float("-inf"), float("inf"), score, "", max_depth)[1]

    end = timer()
    print((end - start) * 1000)

    print("\nFinal Action:", t)
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
        score1 = score1 + result[1]
        score = score + result[1] + calculate_total_hueristics(board)
        print("\n")
        print("=" * 20)
        print("score", score1)
        print("Final----")
        board = place_random(board)