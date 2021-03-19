


def loadBoard(filename):
        boardMatrix = []
        board = open(filename, "r")
        lines = board.readlines()
        count = 0
        for line in lines:
            line = str(line)
            row = line[:-1].split(' ') if count < (len(lines) - 1) else line.split(
                ' ')  # The extra control here is done to be able to read the board from the example board.
            boardMatrix.append(row)
            count += 1
        board.close()
        return boardMatrix

def writeSolutionToBoard(board, cellMap, filename):
    boardFile = open(filename, "w")
    for cell in cellMap:
        if cellMap[cell].solution_value() == 1.0:
            print(cellMap[cell])
            coords = cell.split("|")
            board[int(coords[0])][int(coords[1])] = "L"
    for line in board:
        boardFile.writelines(line)
        boardFile.write("\n")

def printBoard(boardMatrix):
    for i in range(len(boardMatrix)):
        for j in range(len(boardMatrix[i])):
            print(boardMatrix[i][j], end=" ") if j< len(boardMatrix[i]) -1 else \
            print(boardMatrix[i][j], end="")

def getVariables(boardMatrix, solver):
    cellMap = {}
    for i in range(len(boardMatrix)):
        for j in range(len(boardMatrix[i])):
            if boardMatrix[i][j] == "0":
                cellMap[str(i) + "|" + str(j)] = solver.BoolVar(str(i) + "|" + str(j))
    return cellMap

def createkRangeConst(boardMatrix, i, j):
    variablesInVerticalRange = []
    variablesInHorizontalRange = []
    #Check upward
    count = i - 1
    while count >= 0  and boardMatrix[count][j] == "0":
        variablesInVerticalRange.append(str(count) + "|" + str(j))
        count -= 1
    #check downward
    count = i + 1
    while count < len(boardMatrix) and boardMatrix[count][j] == "0":
        variablesInVerticalRange.append(str(count) + "|" + str(j))
        count += 1
    #check rightward
    count = j + 1
    while count < len(boardMatrix[i]) and boardMatrix[i][count] == "0":
        variablesInHorizontalRange.append(str(i) + "|" + str(count))
        count += 1
    #check leftward
    count = j - 1
    while count >= 0 and boardMatrix[i][count] == "0":
        variablesInHorizontalRange.append(str(i) + "|" + str(count))
        count -= 1
    return variablesInVerticalRange, variablesInHorizontalRange

def checkAdjacent(boardMatrix, i, j):
    adjacentWhiteSquaresList = []
    if i == 0:
        if j == 0:
            if boardMatrix[i][j + 1] == "0":
                adjacentWhiteSquaresList.append(str(i) + "|" + str(j+1))
            if boardMatrix[i+1][j] == "0":
                adjacentWhiteSquaresList.append(str(i+1) + "|" + str(j))
        elif j == (len(boardMatrix[i])-1):
            if boardMatrix[i][j-1] == "0":
                adjacentWhiteSquaresList.append(str(i) + "|" + str(j-1))
            if boardMatrix[i+1][j] == "0":
                adjacentWhiteSquaresList.append(str(i + 1) + "|" + str(j))
        else:
            if boardMatrix[i][j+1] == "0":
                adjacentWhiteSquaresList.append(str(i) + "|" + str(j+1))
            if boardMatrix[i][j-1] == "0":
                adjacentWhiteSquaresList.append(str(i) + "|" + str(j-1))
            if boardMatrix[i+1][j] == "0":
                adjacentWhiteSquaresList.append(str(i + 1) + "|" + str(j))
    elif i == len(boardMatrix)-1:
        if j == 0:
            if boardMatrix[i][j+1] == "0":
                adjacentWhiteSquaresList.append(str(i) + "|" + str(j+1))
            if boardMatrix[i-1][j] == "0":
                adjacentWhiteSquaresList.append(str(i - 1) + "|" + str(j))
        elif j == (len(boardMatrix[i]) - 1):
            if boardMatrix[i][j-1] == "0":
                adjacentWhiteSquaresList.append(str(i) + "|" + str(j-1))
            if boardMatrix[i-1][j-1] == "0":
                adjacentWhiteSquaresList.append(str(i-1) + "|" + str(j-1))
        else:
            if boardMatrix[i][j+1] == "0":
                adjacentWhiteSquaresList.append(str(i) + "|" + str(j+1))
            if boardMatrix[i][j-1] == "0":
                adjacentWhiteSquaresList.append(str(i) + "|" + str(j-1))
            if boardMatrix[i-1][j] == "0":
                adjacentWhiteSquaresList.append(str(i-1) + "|" + str(j))
    else:
        if j == 0:
            if boardMatrix[i][j+1] == "0":
                adjacentWhiteSquaresList.append(str(i) + "|" + str(j+1))
            if boardMatrix[i-1][j] == "0":
                adjacentWhiteSquaresList.append(str(i-1) + "|" + str(j))
            if boardMatrix[i+1][j] == "0":
                adjacentWhiteSquaresList.append(str(i+1) + "|" + str(j))
        elif j == (len(boardMatrix[i]) - 1):
            if boardMatrix[i][j-1] == "0":
                adjacentWhiteSquaresList.append(str(i) + "|" + str(j-1))
            if boardMatrix[i-1][j] == "0":
                adjacentWhiteSquaresList.append(str(i-1) + "|" + str(j))
            if boardMatrix[i+1][j] == "0":
                adjacentWhiteSquaresList.append(str(i+1) + "|" + str(j))
        else:
            if boardMatrix[i+1][j] == "0":
                adjacentWhiteSquaresList.append(str(i+1) + "|" + str(j))
            if boardMatrix[i-1][j] == "0":
                adjacentWhiteSquaresList.append(str(i-1) + "|" + str(j))
            if boardMatrix[i][j+1] == "0":
                adjacentWhiteSquaresList.append(str(i) + "|" + str(j+1))
            if boardMatrix[i][j-1] == "0":
                adjacentWhiteSquaresList.append(str(i) + "|" + str(j-1))
    return adjacentWhiteSquaresList






