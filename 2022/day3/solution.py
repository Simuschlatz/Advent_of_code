with open("input.txt", "r") as file:
    data = file.readlines()
    data =[line.rstrip() for line in data]

priority = [chr(i + j) for i in [97, 65] for j in range(26)]
def part_one():
    intersections = [(set(line[:len(line)//2]) & set(line[len(line)//2:])).pop() for line in data]
    total = 0
    for intersection in intersections:
        total += priority.index(intersection) + 1
    return total

def part_two():
    def batch(iterable, n=3):
        l = len(iterable)
        for ndx in range(0, l, n):
            yield iterable[ndx:min(ndx + n, l)]
    lines = [set(line) for line in data]
    total = 0
    for group in batch(lines):
        common = (group[0] & group[1] & group[2]).pop()
        total += priority.index(common) + 1
    return total
    
print(f"part one: {part_one()}")  
print(f"part two: {part_two()}")