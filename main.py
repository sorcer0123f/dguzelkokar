import utils
from ortools.linear_solver import pywraplp


filename = "board2.txt"
resultFilename = "board3Results.txt"
board = utils.loadBoard(filename)
solver = pywraplp.Solver("Akari Solver", pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
constraintList = []
variableList = []
cellMap = utils.getVariables(board, solver)

for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] == "0":
            variablesInVerticalRange, variablesInHorizontalRange = utils.createkRangeConst(board, i, j)

            constraint1 = solver.Constraint(1, 2)
            [constraint1.SetCoefficient(cellMap[var], 1) for var in variablesInVerticalRange]
            [constraint1.SetCoefficient(cellMap[var], 1) for var in variablesInHorizontalRange]
            constraint1.SetCoefficient(cellMap[str(i) + "|" + str(j)], 1)
            print(variablesInVerticalRange)
            print(variablesInHorizontalRange)
            constraint2 = solver.Constraint(0, 1)
            [constraint2.SetCoefficient(cellMap[var], 1) for var in variablesInVerticalRange]
            constraint2.SetCoefficient(cellMap[str(i) + "|" + str(j)], 1)

            constraint3 = solver.Constraint(0, 1)
            [constraint3.SetCoefficient(cellMap[var], 1) for var in variablesInHorizontalRange]
            constraint3.SetCoefficient(cellMap[str(i) + "|" + str(j)], 1)

        else:
            if board[i][j] != "-1":

                adjacentSquares = utils.checkAdjacent(board, i, j)
                if board[i][j] == "-":
                    if len(adjacentSquares) > 0:
                        constraint = solver.Constraint(0, 0)
                        [constraint.SetCoefficient(cellMap[var], 1) for var in adjacentSquares]
                else:
                    if len(adjacentSquares) > 0:
                        constraint = solver.Constraint(int(board[i][j]), int(board[i][j]))
                        [constraint.SetCoefficient(cellMap[var], 1) for var in adjacentSquares]



print(solver.NumConstraints())
solver.Solve()
for cell in cellMap:
    print(cellMap[cell].name(), cellMap[cell].solution_value())

utils.writeSolutionToBoard(board, cellMap, resultFilename)