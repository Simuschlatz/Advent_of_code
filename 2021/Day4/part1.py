with open("data.txt", "r") as file:
    file = file.readlines()
'''
[[],
 [],
 [],
 [],
 []
 ]'''
order_nums = file[0]
file = file[2:]

class Board:
	def __init__(self, board):
		self.board = []
		for i, row in enumerate(board): # formatting into integers
			self.board.append([])
			for char in row:
				self.board[i].append(int(char))
		self.bingo = False
		self.last_checked_num = None

	def mark_num(self, num):
		row = None
		col = None
		found = False
		for i, row in enumerate(self.board):
			if num in row:
				found = True
				c = row.index(num)
				r = i
		if found:
			self.board[r][c] = "x"
			self.last_checked_num = num

	def check_bingo(self):
		bingo_cols = []
		for i in range(5):
			bingo_cols.append(True)

		for i, row in enumerate(self.board):### This approach is not time efficient but this way it would work
			for j, char in enumerate(row): 	### in other non-iterative checking methods aswell as it already 				
					if char != "x":			### loops through the board every time
						break
						bingo_cols[j] = False# if we know thre's not a possible bingo in the row,
					if j == len(row) - 1:		# there also can't be a bingo in the correlated colum
						self.bingo = True
						print("horizontal")
						return True

		for i, row in enumerate(self.board):
			for j, col in enumerate(row):
				if not bingo_cols[j]: continue
				if col != "x":
					bingo_cols[j] = False
					continue
				if i == len(self.board) - 1:
					self.bingo = True
					print("vertical")
					return True
		return False

	@staticmethod
	def calculate_remaining_sum(board):
		s = 0
		for row in board:
			for col in row:
				if col == "x": continue
				s += col
		return s


rows = []
for i, row in enumerate(file):
	r = row.split()
	if r == []: continue
	rows.append(r)
#[['62', '5', '77', '94', '75'], ['59', '10', '23', '44', '29']... (x500)]

boards = []
for i in range(100): # dividing the entire file into sublists, the boards
	board = []
	for j in range(5):
		board.append(rows[i * 5 + j])
	boards.append(Board(board))

order_nums = order_nums.split(",") # formatting the input numbers
inpt_data = []
for col in order_nums:
	inpt_data.append(int(col))

bingo = False
'''part 1'''
# for number in inpt_data: # cba to comment this shit read it yourself
# 	if not bingo:
# 		for board in boards:
# 			board.mark_num(number)
# 			board.check_bingo()
# 			if board.bingo:
# 				bingo = True
# 				for i in range(5):
# 					print(board.board[i])
# 				print("")
# 				print(board.bingo)
# 				print(board.calculate_remaining_sum(board.board) * board.last_checked_num)
# 				break
# 	else: break
'''part 2'''
def part_tow(boards):
	b = None
	bingos = 0
	bingo_boards = []
	for i, number in enumerate(inpt_data): # cba to comment this shit read it yourself
		if bingos < len(boards) - 1:
			for board in boards:
				if board.bingo: continue
				board.mark_num(number)
				board.check_bingo()
				if board.bingo:
					bingos += 1
					# b = board
					print(bingos)
		elif not b:
			print(number)
			for board in boards:
				if not board.bingo:
					b = board
					print(b.board)
		else:
			b.mark_num(number)
			b.check_bingo()
			if b.bingo:
				for i in range(5):
					print(b.board[i])
				print("")
				print(b.last_checked_num * b.calculate_remaining_sum(b.board))
				return True
	return False

# part_tow(boards)
# print(boards[0].calculate_remaining_sum(boards[0].board) * boards[0].last_checked_num)
