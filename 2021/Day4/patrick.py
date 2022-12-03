with open('data.txt', "r") as file:
    inpt = file.readlines()

data = []
firstline = None
for line in inpt:
    if firstline == None:
        firstline = line[:-1]
        continue
    if line != "\n":
        data.append(line[:-1])



class Board:
    def init(self, rows):
        self.rows = []
        for i in range(0, 5):
            self.rows.append(rows[i].split(" "))

    def check_new_number(self, num):
        for row in range(0, 5):
            for col in range(0, 5):
                if self.rows[row][col] == num:
                    self.rows[row][col] = "MARKED"

    def check_bingo(self):
        for row in self.rows:# Horizontale linien
            row_full = True
            for col in row:
                if col != "MARKED":
                    row_full = False

        for col in range(0, 5):
            col_full = True
            for row in range(0, 5):
                if self.rows[row][col] != "MARKED":
                    col_full = False

        if row_full or col_full:
            print("WOAH GEWONNEN HHHH")
            return True

        return False

boards = []

for i in range(0, len(data), 5):
    boards.append(Board([data[i], data[i+1], data[i+2], data[i+3], data[i+4]]))


for num in firstline.split(","):
    for board in boards:
        board.check_new_number(num)
        if board.check_bingo():
            print(board.rows)
            quit()
