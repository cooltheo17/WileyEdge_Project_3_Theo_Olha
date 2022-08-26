def printBoard(whiteMoves, blackMoves, player):
    global colour_1
    if player == 1:  # if player 1 - print in casual way
        rangeVal = range(8, -2, -1)
        rows = ["a", "b", "c", "d", "e", "f", "g", "h"]
    else:  # if player 2 - print reverse way
        rangeVal = range(-1, 9, 1)
        rows = ["h", "g", "f", "e", "d", "c", "b", "a"]
    for j in rangeVal:
        if j != 0 and j != -1:
            print("\033[0;0m" + str(j) + " |", end="")  # print frame vertically
        elif j == -1:
            print("   ", end="")
        elif j == 0:
            print("\033[0;0m---", end="")  # print frame horizontally
        for i in rows:  # printing rows
            if j == -1:
                print(" " + i + " ", end="")  # printing board numeric values
            elif j == 0:
                print("---", end="")
            elif i + str(j) in whiteMoves:  # printing all player's 1 pieces
                piece = whiteMoves.get(i + str(j))[0]
                if piece == "p":
                    print(colour_1 + " ♟ ", end="")
                elif piece == "r":
                    print(colour_1 + " ♜ ", end="")
                elif piece == "k":
                    print(colour_1 + " ♞ ", end="")
                elif piece == "b":
                    print(colour_1 + " ♝ ", end="")
                elif piece == "Q":
                    print(colour_1 + " ♛ ", end="")
                else:
                    print(colour_1 + " ♚ ", end="")
            elif i + str(j) in blackMoves: # printing all player's 2 pieces
                piece = blackMoves.get(i + str(j))[0]
                if piece == "p":
                    print(colour_2 + " ♟ ", end="")
                elif piece == "r":
                    print(colour_2 + " ♜ ", end="")
                elif piece == "k":
                    print(colour_2 + " ♞ ", end="")
                elif piece == "b":
                    print(colour_2 + " ♝ ", end="")
                elif piece == "Q":
                    print(colour_2 + " ♛ ", end="")
                else:
                    print(colour_2 + " ♚ ", end="")
            else:  # printing empty board positions
                if j % 2 != 0:
                    if i in "aceg":
                        print(colour_2 + " ◼ ", end="")
                    else:
                        print(colour_1 + " ◼ ", end="")
                else:
                    if i in "bdfh":
                        print(colour_2 + " ◼ ", end="")
                    else:
                        print(colour_1 + " ◼ ", end="")
        print("")


def chooseColour(player):  # player can choose the figures color
    colour = ""
    while colour == "":
        colour_choice1 = input("\033[0;0mPlayer " + player + " - Choose your colour :")
        if colour_choice1 == "1" or colour_choice1 == "red":
            colour = "\033[1;31m"
        elif colour_choice1 == "2" or colour_choice1 == "green":
            colour = "\033[1;32m"
        elif colour_choice1 == "3" or colour_choice1 == "yellow":
            colour = "\033[1;33m"
        elif colour_choice1 == "4" or colour_choice1 == "blue":
            colour = "\033[1;34m"
        elif colour_choice1 == "5" or colour_choice1 == "purple":
            colour = "\033[1;35m"
        elif colour_choice1 == "6" or colour_choice1 == "cyan":
            colour = "\033[1;36m"
        elif colour_choice1 == "7" or colour_choice1 == "white":
            colour = "\033[1;0m"
        elif colour_choice1 == "8" or colour_choice1 == "black":
            colour = "\033[1;30m"
        else:
            print("Invalid choice!")
    return colour


def startGame():
    player = 0  # player val to swap turns
    combDict = [whiteDict, blackDict] # player1 and player2 pieces
    while True:
        print(f"Player {player + 1} makes a move...")
        printBoard(combDict[0], combDict[1], player + 1)  # printing board
        # old position to get player's piece there
        oldPos = input("\033[0;0mPlease type the position of the piece you want to move: ")
        if oldPos in combDict[player]:  # check if there's a player's piece on that position (letter + digit)
            while True:
                print("Type - back - to cancel.")
                newPos = input("Please type the new position of the piece: ") # input new position (letter + digit)
                if newPos == "back":
                    player = 1 - player
                    break
                if len(newPos) == 2 and is_move_valid(player + 1, oldPos, newPos):  # check if such move is valid
                    if newPos in combDict[1 - player]:  # if player kills opponent's piece,
                        combDict[1 - player].pop(newPos)  # delete that piece for opponent
                    combDict[player][newPos] = combDict[player].pop(oldPos)  # place piece on new position
                    break
                else:
                    print("Move is invalid...")
                print("\n================================\n")
                if "K" not in list(combDict[1 - player].values()):
                    return player + 1
                player = 1 - player
        else:
            print("Invalid piece position!\nTry again.")


def is_move_valid(player, init_pos, new_pos):
    rows = ["a", "b", "c", "d", "e", "f", "g", "h"]  # all board rows namings
    cols = [1, 2, 3, 4, 5, 6, 7, 8]  # all board columns namings
    if player == 1:  # if it's player's 1 turn -
        multiplier = 1  # multiplier is 1 according to player's 1 board view
        moves1 = whiteDict  # copy of current player pieces
        moves2 = blackDict  # copy of opponent player pieces
    else:  # if it's player 2 - via versa
        multiplier = -1
        moves1 = blackDict
        moves2 = whiteDict
    # check if new pos is out of bounds
    if new_pos == "" or new_pos[0] not in rows or int(new_pos[1]) not in cols or init_pos == new_pos:
        return False
    piece = moves1[init_pos]  # get piece's
    possible_moves = []  # for some pieces all possible moves are stored here
    if piece[0] == "p":
        # if 1 step forward
        if init_pos[0] + str(int(init_pos[1]) + 1 * multiplier) not in moves2.keys() and \
                init_pos[0] + str(int(init_pos[1]) + 1 * multiplier) not in moves1.keys():
            possible_moves.append(init_pos[0] + str(int(init_pos[1]) + 1 * multiplier))
        # if 2 steps forward
        if init_pos[0] + str(int(init_pos[1]) + 2 * multiplier) not in moves2.keys() and \
                init_pos[0] + str(int(init_pos[1]) + 2 * multiplier) not in moves1.keys():
            # check if there's any piece on the way
            if init_pos[0] + str(int(init_pos[1]) + 1 * multiplier) not in moves2.keys() and \
                    init_pos[0] + str(int(init_pos[1]) + 1 * multiplier) not in moves1.keys():
                possible_moves.append(init_pos[0] + str(int(init_pos[1]) + 2 * multiplier))
        # if killing to the right
        if -1 < rows.index(init_pos[0]) + 1 * multiplier < 8 and rows[rows.index(init_pos[0]) + 1 * multiplier] \
                + str(int(init_pos[1]) + 1 * multiplier) in moves2.keys():
            possible_moves.append(rows[rows.index(init_pos[0]) + 1 * multiplier]
                                  + str(int(init_pos[1]) + 1 * multiplier))
        # if killing to the left
        if -1 < rows.index(init_pos[0]) - 1 * multiplier < 8 and rows[rows.index(init_pos[0]) - 1 * multiplier] \
                + str(int(init_pos[1]) + 1 * multiplier) in moves2.keys():
            possible_moves.append(rows[rows.index(init_pos[0]) - 1 * multiplier]
                                  + str(int(init_pos[1]) + 1 * multiplier))
        if new_pos in possible_moves:  # if new position corresponds to any possible position - it's valid
            return True
    elif piece[0] == "r":
        if init_pos[0] != new_pos[0] and init_pos[1] != new_pos[1]:  # if move is not vertical or horizontal - not valid
            return False
        if init_pos[0] == new_pos[0]:  # if vertical
            oldY = int(init_pos[1])  # old position digit value
            newY = int(new_pos[1])   # new position digit value
            killed = 0  # to track down if something is killed
            if newY > oldY:  # changing multiplier value depending on
                mult = 1
            else:
                mult = -1
            for i in range(oldY, newY, mult):
                oldY += mult
                # if ally piece on the way or piece killed on the way - invalid move
                if (init_pos[0] + str(oldY)) in moves1 or killed == 1:
                    return False
                elif (init_pos[0] + str(oldY)) in moves2:
                    if killed == 0 and new_pos in moves2:
                        killed = 1
                    else:
                        return False
        else:  # if horizontal
            oldX = rows.index(init_pos[0])
            newX = rows.index(new_pos[0])
            killed = 0
            if newX > oldX:
                mult = 1
            else:
                mult = -1
            for i in range(oldX, newX, mult):
                oldX += mult
                if (rows[oldX] + init_pos[1]) in moves1 or killed == 1:
                    return False
                elif (rows[oldX] + init_pos[1]) in moves2:
                    if killed == 0 and new_pos in moves2:
                        killed = 1
                    else:
                        return False
        return True
    elif piece[0] == "k":
        # change pos by 2 right
        letter1 = rows.index(init_pos[0]) + 2 * multiplier
        # change pos by 2 left
        letter1_1 = rows.index(init_pos[0]) - 2 * multiplier
        # change pos by 1 right
        letter2 = rows.index(init_pos[0]) + 1 * multiplier
        # change pos by 1 left
        letter2_1 = rows.index(init_pos[0]) - 1 * multiplier
        # change pos by 1 up
        num1 = int(init_pos[1]) + 1 * multiplier
        # change pos by 1 down
        num1_1 = int(init_pos[1]) - 1 * multiplier
        # change pos by 2 up
        num2 = int(init_pos[1]) + 2 * multiplier
        # change pos by 2 down
        num2_1 = int(init_pos[1]) - 2 * multiplier
        if 0 <= letter1 < 8 and rows[letter1] + str(num1) not in moves1:
            possible_moves.append(rows[letter1] + str(num1))
        if 0 <= letter1 < 8 and rows[letter1] + str(num1_1) not in moves1:
            possible_moves.append(rows[letter1] + str(num1_1))
        if 0 <= letter1_1 < 8 and rows[letter1_1] + str(num1) not in moves1:
            possible_moves.append(rows[letter1_1] + str(num1))
        if 0 <= letter1_1 < 8 and rows[letter1_1] + str(num1_1) not in moves1:
            possible_moves.append(rows[letter1_1] + str(num1_1))
        if 0 <= letter2 < 8 and rows[letter2] + str(num2) not in moves1:
            possible_moves.append(rows[letter2] + str(num2))
        if 0 <= letter2 < 8 and rows[letter2] + str(num2_1) not in moves1:
            possible_moves.append(rows[letter2] + str(num2_1))
        if 0 <= letter2_1 < 8 and rows[letter2_1] + str(num2) not in moves1:
            possible_moves.append(rows[letter2_1] + str(num2))
        if 0 <= letter2_1 < 8 and rows[letter2_1] + str(num2_1) not in moves1:
            possible_moves.append(rows[letter2_1] + str(num2_1))
        if new_pos in possible_moves:
            return True
    elif piece[0] == "K":
        if rows.index(new_pos[0]) - rows.index(init_pos[0]) > 1 or \
                rows.index(new_pos[0]) - rows.index(init_pos[0]) < -1:
            return False
        elif int(new_pos[1]) - int(init_pos[1]) > 1 or int(new_pos[1]) - int(init_pos[1]) < -1:
            return False
        if new_pos not in moves1:
            return True
    elif piece[0] == "Q":
        # if same letter or same digit - execute rook code
        if init_pos[0] == new_pos[0] or init_pos[1] == new_pos[1]:
            if init_pos[0] == new_pos[0]:
                oldY = int(init_pos[1])
                newY = int(new_pos[1])
                killed = 0
                if newY > oldY:
                    mult = 1
                else:
                    mult = -1
                for i in range(oldY, newY, mult):
                    oldY += mult
                    if (init_pos[0] + str(oldY)) in moves1 or killed == 1:
                        return False
                    elif (init_pos[0] + str(oldY)) in moves2:
                        if killed == 0 and new_pos in moves2:
                            killed = 1
                        else:
                            return False
            else:
                oldX = rows.index(init_pos[0])
                newX = rows.index(new_pos[0])
                killed = 0
                if newX > oldX:
                    mult = 1
                else:
                    mult = -1
                for i in range(oldX, newX, mult):
                    oldX += mult
                    if (rows[oldX] + init_pos[1]) in moves1 or killed == 1:
                        return False
                    elif (rows[oldX] + init_pos[1]) in moves2:
                        if killed == 0 and new_pos in moves2:
                            killed = 1
                        else:
                            return False
        # if diagonally correct - execute bishop code
        elif abs(ord(new_pos[0]) - ord(init_pos[0])) == abs(int(new_pos[1]) - int(init_pos[1])):
            if abs(ord(new_pos[0]) - ord(init_pos[0])) != abs(int(new_pos[1]) - int(init_pos[1])):
                return False
            else:
                if ord(new_pos[0]) - ord(init_pos[0]) > 0 and int(new_pos[1]) - int(init_pos[1]) > 0:
                    i = 1
                    j = 1
                elif ord(new_pos[0]) - ord(init_pos[0]) > 0 > int(new_pos[1]) - int(init_pos[1]):
                    i = 1
                    j = -1
                elif ord(new_pos[0]) - ord(init_pos[0]) < 0 and int(new_pos[1]) - int(init_pos[1]) < 0:
                    i = -1
                    j = -1
                elif ord(new_pos[0]) - ord(init_pos[0]) < 0 < int(new_pos[1]) - int(init_pos[1]):
                    i = -1
                    j = 1
                while init_pos != new_pos:
                    init_pos = rows[rows.index(init_pos[0]) + i] + str(int(init_pos[1]) + j)
                    if init_pos in moves1:
                        return False
                    elif init_pos in moves2 and init_pos != new_pos:
                        return False
                return True
        # if both false - illegal move
        else:
            return False
    elif piece[0] == "b":
        if abs(ord(new_pos[0]) - ord(init_pos[0])) != abs(int(new_pos[1]) - int(init_pos[1])):
            return False
        else:
            if abs(ord(new_pos[0]) - ord(init_pos[0])) != abs(int(new_pos[1]) - int(init_pos[1])):
                return False
            else:
                if ord(new_pos[0]) - ord(init_pos[0]) > 0 and int(new_pos[1]) - int(init_pos[1]) > 0:
                    i = 1
                    j = 1
                elif ord(new_pos[0]) - ord(init_pos[0]) > 0 > int(new_pos[1]) - int(init_pos[1]):
                    i = 1
                    j = -1
                elif ord(new_pos[0]) - ord(init_pos[0]) < 0 and int(new_pos[1]) - int(init_pos[1]) < 0:
                    i = -1
                    j = -1
                elif ord(new_pos[0]) - ord(init_pos[0]) < 0 < int(new_pos[1]) - int(init_pos[1]):
                    i = -1
                    j = 1
                while init_pos != new_pos:
                    init_pos = rows[rows.index(init_pos[0]) + i] + str(int(init_pos[1]) + j)
                    if init_pos in moves1:
                        return False
                    elif init_pos in moves2 and init_pos != new_pos:
                        return False
                return True


whiteDict = {"a2": "p1", "b2": "p2", "c2": "p3", "d2": "p4", "e2": "p5", "f2": "p6", "g2": "p7", "h2": "p8", "a1": "r1",
             "b1": "k1", "c1": "b1", "d1": "Q", "e1": "K", "f1": "b2", "g1": "k2", "h1": "r2"}
blackDict = {"a7": "p1", "b7": "p2", "c7": "p3", "d7": "p4", "e7": "p5", "f7": "p6", "g7": "p7", "h7": "p8", "a8": "r1",
             "b8": "k1", "c8": "b1", "d8": "Q", "e8": "K", "f8": "b2", "g8": "k2", "h8": "r2"}
player = 1

print("\033[0;0m1. \033[1;31m◼  ", end="")
print("\033[0;0m2. \033[1;32m◼  ", end="")
print("\033[0;0m3. \033[1;33m◼  ", end="")
print("\033[0;0m4. \033[1;34m◼  ", end="")
print("\033[0;0m5. \033[1;35m◼  ", end="")
print("\033[0;0m6. \033[1;36m◼  ", end="")
print("\033[0;0m7. \033[1;0m◼  ", end="")
print("\033[0;0m8. \033[1;30m◼")

colour_1 = chooseColour("1")
colour_2 = chooseColour("2")
winner = startGame()
if winner == 1:
    winning_colour = colour_1
else:
    winning_colour = colour_2
print(winning_colour + "Player "+str(winner)+" has won the game!")
