import math
with open("data05.txt", "r") as inpt:
	file = inpt.readlines()

class Line:
	def __init__(self, start_pos, end_pos):
		self.start_x, self.start_y = start_pos
		self.end_x, self.end_y = end_pos
		self.points = [start_pos]
		for i in range(1, abs(self.start_x - self.end_x) + 1):
			if self.start_x < self.end_x:
				self.points.append((self.start_x + i, self.start_y))
				continue
			self.points.append((self.start_x - i, self.start_y))

		for i in range(1, abs(self.start_y - self.end_y) + 1):
			if self.start_y < self.end_y:
				self.points.append((self.start_x, self.start_y + i))
				continue
			self.points.append((self.start_x, self.start_y - i))

lines = []
points = {}
for i, line in enumerate(file):
	l = line.replace("->", "").split()
	coordinates = []
	for element in l:
		x, y = element.split(",")
		coordinates.append((int(x), int(y)))
	lines.append(Line(coordinates[0], coordinates[1]))

for line in lines:
	for point in line.points:
		points[point] = points.get(point, 0) + 1
print(len(points))
count = 0
intraversable = []
for point, val in points.items():
	if val < 2: continue
	count += 1
	
print(count)

