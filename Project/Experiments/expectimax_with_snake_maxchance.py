import copy
import random
import math


def numberofzeroes(bb):
    count = 0
    b = copy.deepcopy(bb)

    for i in range(4):
        for j in range(4):
            if b[i][j] == 0:
                count = count + 1
    return count


def calculate(board1):
    b = copy.deepcopy(board1)
    sum = 0
    for i in range(3):
        for j in range(3):
            sum = sum + b[i][j] * boardm[i][j]
    return sum


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
    b = copy.deepcopy(bb)
    picked_location = pick_random_place(b)
    q = random.randint(0, 100)
    f = 0  # since i am checking only for 2 as min
    if q < 80:

        f = 0
    else:
        f = 1

    b[picked_location[0]][picked_location[1]] =choices[f]
    # print_board(b)
    return b


def push_up(bb):
    s = 0

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
    return b_new, s


def push_down(bb):
    s = 0

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
    return b_new, s


def push_left(bb):
    s = 0

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

    return b_new, s


def push_right(bb):
    s = 0

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

    return b_new, s


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
    l=b[0][0]
    for i in range(4):
        for j in range(4):
            if b[i][j]>l:
                l=b[i][j]
    return l

def minimax(board, is_maximising, depth, alpha, beta, score, action, max_depth):
    global choices

    # print("depth:", depth, score)
    # print_board(board)

    if is_done(board):
        return score, 0, action

    if depth == max_depth:
        # print("Depth Reached", depth)
        return (score + numberofzeroes(board) * 4 + calculate(board)), 0, action

    if is_maximising==1:

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

                return_value = minimax(temp_board, 2, depth + 1, alpha, beta, (score + result[1] + numberofzeroes(temp_board * 4) + calculate(board)), action + " " + i, max_depth)
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

    elif is_maximising==2:
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
            return_value = minimax(temp_board, 1, depth, alpha, beta, (score + numberofzeroes(temp_board) * 4 + calculate(temp_board)), action, max_depth)
            return_value1 = minimax(temp_board, 1, depth, alpha, beta, (score + numberofzeroes(temp_board) * 4 + calculate(temp_board)), action, max_depth)
            # print("Return at Min: ", return_value)
            # if best_min > return_value[0]:
                # print("Replacing at Min with", return_value[0], best_min)
            best_min = 0.8 * return_value[0]+0.2*return_value1[0]
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
 



board = [[2, 16, 4, 8],
         [8, 4, 32, 4],
         [2, 32, 16, 8],
         [4, 4, 2, 0]]

boardm = [[4 ** 15, 4 ** 14, 4 ** 13, 4 ** 12],
          [4 ** 8, 4 ** 9, 4 ** 10, 4 ** 11],
          [4 ** 7, 4 ** 6, 4 ** 5, 4 ** 4],
          [4 ** 0, 4 ** 1, 4 ** 2, 4 ** 3]]

board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
score1 = 0
choices = [2, 4]

score = 0

max_depth = 2

board = place_random(board)
arr=[]

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
        # print_board(board)
        score1 = score1 + result[1]
        score = score + result[1] + numberofzeroes(board) * 4 + calculate(board)
        print("\n")
        print("=" * 20)
        print("score", score1)
        print("Final----")
        print_board(board)
        board = place_random(board)
    