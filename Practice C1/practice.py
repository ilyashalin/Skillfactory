MARK_UNKNOWN = ' '
MARK_X = 'X'
MARK_0 = '0'

class Cell:
    def __init__(self):
        self.mark = MARK_UNKNOWN

    def setMark(self, mark):
        self.mark = mark

    def getMark(self):
        return self.mark
class Board:
    def __init__(self, r = 3, c = 3):
        self.cells = []
        self.rowsCount = r
        self.columnsCount = c
        for i in range(r*c):
            self.cells.append(Cell())

    def getRowsCount(self):
        return self.rowsCount

    def getColumnsCount(self):
        return self.columnsCount

    def isCellAvailible(self, index):
        return self.cells[index-1].getMark() == MARK_UNKNOWN

    def getMarkInCell(self, index):
        return self.cells[index-1].getMark()

    def setCell(self, index, mark):
        self.cells[index-1].setMark(mark)

    def getCells(self):
        return self.cells
class Player:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def getName(self):
        return self.name

    def getMark(self):
        return self.mark
def winCondition(board):
    win_combo = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]

    winMark = MARK_UNKNOWN
    for combo in win_combo:
        m1 = board.getMarkInCell(combo[0])
        m2 = board.getMarkInCell(combo[1])
        m3 = board.getMarkInCell(combo[2])
        if (m1 == m2 == m3) :
            winMark = m1
            break

    return winMark


def render(board):
    rc = board.getRowsCount()
    cl = board.getColumnsCount()

    for r in range(rc):
        row = []
        for c in range(cl):
            row.append(board.getMarkInCell(r * cl + c + 1))
        print("|".join(row))


if __name__ == '__main__':
    # get users
    # swich turns
    # get action

    board = Board()
    p1 = Player("1", MARK_X)
    p2 = Player("2", MARK_0)

    board.setCell(5, p1.getMark())
    board.setCell(1, p2.getMark())
    board.setCell(3, p1.getMark())
    board.setCell(2, p2.getMark())

    print("win:" + winCondition(board))
    render(board)

    print("----------------------------------------------------------------")
    board.setCell(7, p1.getMark())
    print("win:" + winCondition(board))
    render(board)
print()
