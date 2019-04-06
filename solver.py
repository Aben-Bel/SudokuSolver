sudoku = [[{"value": 0, "guesses": []}, {"value": 0, "guesses": []},
           {"value": 0, "guesses": []}, {"value": 0, "guesses": []},
           {"value": 0, "guesses": []}, {"value": 0, "guesses": []},
           {"value": 0, "guesses": []}, {"value": 4, "guesses": []},
           {"value": 3, "guesses": []}],
          [{"value": 0, "guesses": []}, {"value": 0, "guesses": []},
           {"value": 7, "guesses": []}, {"value": 5, "guesses": []},
           {"value": 3, "guesses": []}, {"value": 0, "guesses": []},
           {"value": 2, "guesses": []}, {"value": 9, "guesses": []},
           {"value": 0, "guesses": []}],
          [{"value": 2, "guesses": []}, {"value": 0, "guesses": []},
           {"value": 0, "guesses": []}, {"value": 0, "guesses": []},
           {"value": 7, "guesses": []}, {"value": 0, "guesses": []},
           {"value": 0, "guesses": []}, {"value": 0, "guesses": []},
           {"value": 0, "guesses": []}],
          [{"value": 0, "guesses": []}, {"value": 0, "guesses": []},
           {"value": 0, "guesses": []}, {"value": 0, "guesses": []},
           {"value": 4, "guesses": []}, {"value": 0, "guesses": []},
           {"value": 0, "guesses": []}, {"value": 0, "guesses": []},
           {"value": 0, "guesses": []}],
          [{"value": 0, "guesses": []}, {"value": 4, "guesses": []},
           {"value": 3, "guesses": []}, {"value": 7, "guesses": []},
           {"value": 0, "guesses": []}, {"value": 6, "guesses": []},
           {"value": 0, "guesses": []}, {"value": 1, "guesses": []},
           {"value": 0, "guesses": []}],
          [{"value": 0, "guesses": []}, {"value": 0, "guesses": []},
           {"value": 2, "guesses": []}, {"value": 8, "guesses": []},
           {"value": 9, "guesses": []}, {"value": 0, "guesses": []},
           {"value": 0, "guesses": []}, {"value": 0, "guesses": []},
           {"value": 0, "guesses": []}],
          [{"value": 7, "guesses": []}, {"value": 0, "guesses": []},
           {"value": 0, "guesses": []}, {"value": 0, "guesses": []},
           {"value": 0, "guesses": []}, {"value": 0, "guesses": []},
           {"value": 5, "guesses": []}, {"value": 0, "guesses": []},
           {"value": 0, "guesses": []}],
          [{"value": 0, "guesses": []}, {"value": 1, "guesses": []},
           {"value": 9, "guesses": []}, {"value": 0, "guesses": []},
           {"value": 0, "guesses": []}, {"value": 0, "guesses": []},
           {"value": 3, "guesses": []}, {"value": 0, "guesses": []},
           {"value": 0, "guesses": []}],
          [{"value": 0, "guesses": []}, {"value": 0, "guesses": []},
           {"value": 0, "guesses": []}, {"value": 2, "guesses": []},
           {"value": 0, "guesses": []}, {"value": 4, "guesses": []},
           {"value": 0, "guesses": []}, {"value": 0, "guesses": []},
           {"value": 0, "guesses": []}],
          ]


def repeated(l):
    """takes a list and return True if there is repeated value otherwise False"""
    # sort the list and check convective elements
    l.sort()
    for i in range(len(l)):
        if i < len(l) - 1:
            if l[i] == l[i + 1]:
                return True
    return False


def horizontalNumberCollector(i):
    collector = []
    for k in range(9):
        if sudoku[i][k]["value"] != 0:
            collector.append(sudoku[i][k]["value"])
    return collector


def verticalNumberCollector(j):
    collector = []
    for k in range(9):
        if sudoku[k][j]["value"] != 0:
            collector.append(sudoku[k][j]["value"])
    return collector


def boxNumberCollector(i, j):
    collector = []
    for k in range(9):
        for m in range(9):
            if sudoku[k][m]["value"] != 0:
                # top most left 3x3 box
                if i < 3 and j < 3 and m < 3 and k < 3:
                    collector.append(sudoku[k][m]["value"])
                # top middle 3x3 box
                if i < 3 and j < 6 and j >= 3 and m >= 3 and m < 6 and k < 3:
                    collector.append(sudoku[k][m]["value"])
                # top most right 3x3 box
                if i < 3 and j >= 6 and m >= 6 and k < 3:
                    collector.append(sudoku[k][m]["value"])

                # middle most left 3x3 box
                if i >= 3 and i < 6 and j < 3 and m < 3 and k >= 3 and k < 6:
                    collector.append(sudoku[k][m]["value"])
                # middle middle 3x3 box
                if i >= 3 and i < 6 and j >= 3 and j < 6 and m >= 3 and m < 6 and k >= 3 and k < 6:
                    collector.append(sudoku[k][m]["value"])
                # middle most right 3x3 box
                if i >= 3 and i < 6 and j >= 6 and m >= 6 and k >= 3 and k < 6:
                    collector.append(sudoku[k][m]["value"])

                # bottom most left 3x3 box
                if i >= 6 and j < 3 and m < 3 and k >= 6:
                    collector.append(sudoku[k][m]["value"])
                # bottom middle 3x3 box
                if i >= 6 and j < 6 and j >= 3 and m >= 3 and m < 6 and k >= 6:
                    collector.append(sudoku[k][m]["value"])
                # bottom most right 3x3 box
                if i >= 6 and j >= 6 and m >= 6 and k >= 6:
                    collector.append(sudoku[k][m]["value"])
    return collector


def sudokuRuleViolated(i, j):
    """takes coordinate of a cell and checks whether it violates
       sudoku ruler from the global sudoku 2D list,
       if it doesn't return False, otherwise True"""

    # function to collect all numbers in the horizontal adjacent of the cell (i,j)
    buff = horizontalNumberCollector(i)

    # checking the numbers collected from the horizontal are following sudoku rules
    if repeated(buff[:]):
        return False
    buff.clear()

    # function to collect all numbers in the vertical adjacent of the cell (i,j)
    buff = verticalNumberCollector(j)

    # checking the numbers collected from the vertical are following sudoku rules
    if repeated(buff[:]):
        return False
    buff.clear()

    # function to collect all numbers in the 3x3 box of the cell (i,j)
    buff = boxNumberCollector(i, j)

    # checking the numbers collected from the boxex are following sudoku rules
    if repeated(buff[:]):
        return False

    return True


def editSudoku(i, j, value):
    sudoku[i][j]["value"] = value


def sudokuPrinter():
    """prints sudoku to user"""
    for i in range(9):
        for j in range(9):
            if j == 8:
                print(sudoku[i][j]["value"], end=" |")
            if j == 0:
                print("|", sudoku[i][j]["value"], end=" | ")
            if j != 8 and j != 0:
                print(sudoku[i][j]["value"], end=" | ")

        print("")
        if (i + 1) % 3 == 0:
            for k in range(9):
                print("----", end="")
        print("")


def promptForInput():
    """prompts the user to input values for sudoku"""
    while True:
        key, i, j = eval(input("key, i , j: "))

        if key == 0:
            break
        elif str(key).isdigit() and str(i).isdigit() and str(j).isdigit():
            temp = sudoku[i][j]["value"]
            editSudoku(i, j, key)
            if not sudokuRuleViolated(i, j):
                editSudoku(i, j, temp)
    sudokuPrinter()


def mustBeInNumber():
    for i in range(1, 10):
        if i == 1:
            box = set(boxNumberCollector(0, 0))
            numbers = set([1, 2, 3, 4, 5, 6, 7, 8, 9]).difference(box)

            for num in numbers:
                record = []
                for k in range(9):
                    for m in range(9):
                        if m < 3 and k < 3:
                            if sudoku[k][m]["value"] == 0:
                                if num in horizontalNumberCollector(k) or num in verticalNumberCollector(m):
                                    pass
                                else:
                                    record += [[k, m]]
                if len(record) == 1:
                    sudoku[record[0][0]][record[0][1]]["value"] = num
        if i == 2:
            box = set(boxNumberCollector(0, 3))
            numbers = set([1, 2, 3, 4, 5, 6, 7, 8, 9]).difference(box)

            for num in numbers:
                record = []
                for k in range(9):
                    for m in range(9):
                        if m >= 3 and m < 6 and k < 3:
                            if sudoku[k][m]["value"] == 0:
                                if num in horizontalNumberCollector(k) or num in verticalNumberCollector(m):
                                    pass
                                else:
                                    record += [[k, m]]
                if len(record) == 1:
                    sudoku[record[0][0]][record[0][1]]["value"] = num
        if i == 3:
            box = set(boxNumberCollector(0, 6))
            numbers = set([1, 2, 3, 4, 5, 6, 7, 8, 9]).difference(box)

            for num in numbers:
                record = []
                for k in range(9):
                    for m in range(9):
                        if m >= 6 and k < 3:
                            if sudoku[k][m]["value"] == 0:
                                if num in horizontalNumberCollector(k) or num in verticalNumberCollector(m):
                                    pass
                                else:
                                    record += [[k, m]]
                if len(record) == 1:
                    sudoku[record[0][0]][record[0][1]]["value"] = num
        if i == 4:
            box = set(boxNumberCollector(3, 0))
            numbers = set([1, 2, 3, 4, 5, 6, 7, 8, 9]).difference(box)

            for num in numbers:
                record = []
                for k in range(9):
                    for m in range(9):
                        if m < 3 and k >= 3 and k < 6:
                            if sudoku[k][m]["value"] == 0:
                                if num in horizontalNumberCollector(k) or num in verticalNumberCollector(m):
                                    pass
                                else:
                                    record += [[k, m]]
                if len(record) == 1:
                    sudoku[record[0][0]][record[0][1]]["value"] = num
        if i == 5:
            box = set(boxNumberCollector(3, 3))
            numbers = set([1, 2, 3, 4, 5, 6, 7, 8, 9]).difference(box)

            for num in numbers:
                record = []
                for k in range(9):
                    for m in range(9):
                        if m >= 3 and m < 6 and k >= 3 and k < 6:
                            if sudoku[k][m]["value"] == 0:
                                if num in horizontalNumberCollector(k) or num in verticalNumberCollector(m):
                                    pass
                                else:
                                    record += [[k, m]]
                if len(record) == 1:
                    sudoku[record[0][0]][record[0][1]]["value"] = num
        if i == 6:
            box = set(boxNumberCollector(3, 6))
            numbers = set([1, 2, 3, 4, 5, 6, 7, 8, 9]).difference(box)

            for num in numbers:
                record = []
                for k in range(9):
                    for m in range(9):
                        if m >= 6 and k >= 3 and k < 6:
                            if sudoku[k][m]["value"] == 0:
                                if num in horizontalNumberCollector(k) or num in verticalNumberCollector(m):
                                    pass
                                else:
                                    record += [[k, m]]
                if len(record) == 1:
                    sudoku[record[0][0]][record[0][1]]["value"] = num
        if i == 7:
            box = set(boxNumberCollector(6, 0))
            numbers = set([1, 2, 3, 4, 5, 6, 7, 8, 9]).difference(box)

            for num in numbers:
                record = []
                for k in range(9):
                    for m in range(9):
                        if m < 3 and k >= 6:
                            if sudoku[k][m]["value"] == 0:
                                if num in horizontalNumberCollector(k) or num in verticalNumberCollector(m):
                                    pass
                                else:
                                    record += [[k, m]]
                if len(record) == 1:
                    sudoku[record[0][0]][record[0][1]]["value"] = num
        if i == 8:
            box = set(boxNumberCollector(6, 3))
            numbers = set([1, 2, 3, 4, 5, 6, 7, 8, 9]).difference(box)

            for num in numbers:
                record = []
                for k in range(9):
                    for m in range(9):
                        if m >= 3 and m < 6 and k >= 6:
                            if sudoku[k][m]["value"] == 0:
                                if num in horizontalNumberCollector(k) or num in verticalNumberCollector(m):
                                    pass
                                else:
                                    record += [[k, m]]
                if len(record) == 1:
                    sudoku[record[0][0]][record[0][1]]["value"] = num
        if i == 9:
            box = set(boxNumberCollector(6, 6))
            numbers = set([1, 2, 3, 4, 5, 6, 7, 8, 9]).difference(box)

            for num in numbers:
                record = []
                for k in range(9):
                    for m in range(9):
                        if m >= 6 and k >= 6:
                            if sudoku[k][m]["value"] == 0:
                                if num in horizontalNumberCollector(k) or num in verticalNumberCollector(m):
                                    pass
                                else:
                                    record += [[k, m]]
                if len(record) == 1:
                    sudoku[record[0][0]][record[0][1]]["value"] = num


def guessPossibleValues():
    changes_made = True
    while changes_made:
        changes_made = False
        for i in range(9):
            for j in range(9):
                if sudoku[i][j]["value"] == 0:
                    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

                    to_be_deleted = set()
                    to_be_deleted.update(set(horizontalNumberCollector(i)))
                    to_be_deleted.update(set(verticalNumberCollector(j)))
                    to_be_deleted.update(set(boxNumberCollector(i, j)))

                    for n in to_be_deleted:
                        try:
                            numbers.remove(n)
                        except ValueError:
                            pass

                    if len(numbers) == 1:
                        temp = sudoku[i][j]["value"]
                        editSudoku(i, j, numbers[0])
                        if not sudokuRuleViolated(i, j):
                            editSudoku(i, j, temp)
                        changes_made = True
                    elif len(sudoku[i][j]["guesses"]) == 0:
                        sudoku[i][j]["guesses"] += numbers
            mustBeInNumber()
    #sudokuPrinter()

def completed():
    for i in range(9):
        for j in range(9):
            if sudoku[i][j]["value"] == 0:
                return False
    return True

def main():
    global sudoku
    guessPossibleValues()
    bruteForce = {"loc":[],
                  "guesses":[]
                  }

    if not completed():
        for i in range(9):
            for j in range(9):
                if sudoku[i][j]["value"] == 0:
                    bruteForce["loc"] = [i, j]
                    bruteForce["guesses"] = sudoku[i][j]["guesses"]
        copy = sudoku[:]
        for i in range(len(bruteForce["guesses"])):
            n = bruteForce["guesses"][i]
            sudoku[bruteForce["loc"][0]][bruteForce["loc"][1]]["value"] = n

            guessPossibleValues()

            if not completed():
                sudoku = copy[:]
            else:
                sudokuPrinter()
                break
    sudokuPrinter()






main()
