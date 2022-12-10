from collections import defaultdict
with open("input.txt", "r") as file:
    data = [line.rstrip().replace("$ ", "").split() for line in file.readlines()]
# process data
cwd = []
sizes = defaultdict(int)
for line in data:
    command = line[0]
    if command in ["ls", "dir"]:
        continue
    if command == "cd":
        directory = line[1]
        if directory == "..": cwd.pop()
        else: cwd.append(directory)
        continue
    if command.isdigit():
        size = int(command)
        # backpropagate
        for i in range(1, len(cwd)+1):
            directory = "/".join(cwd[:i])
            sizes[directory] += size

part_one = sum(filter(lambda size: size <= 100_000, sizes.values()))
def part_two():
    delete_size = sizes["/"] - 40_000_000
    return min(filter(lambda size: size >= delete_size, sizes.values()))

print("part one:", part_one)
print("part two:", part_two())