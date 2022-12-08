"""I ain't a numpy pro leave me alone"""
import numpy as np

with open("input.txt", "r") as file:
    lines = file.readlines()
stacks, commands = None, []
for i, line in enumerate(lines):
    if line[0] == "m":
        command = list(map(int, filter(lambda char: char.isdigit(), line.split())))
        commands.append(command)
    elif line[0] == " ":
        stacks = np.array([[line[i] for i in range(1, len(line), 4)] for line in lines[:i]]).T
        stacks = [tuple(filter(lambda package: package != " ", stack)) for stack in stacks]

def solution(part):
    s = stacks[:]
    for command in commands:
        n, from_idx, to_idx = command[0], command[1] - 1, command[2] - 1
        s[to_idx] = s[from_idx][:n] + s[to_idx] if part - 1 else s[from_idx][:n][::-1] + s[to_idx]
        s[from_idx] = s[from_idx][n:]
    return "".join([stack[0] if len(stack) else "" for stack in s])
print(f"part one: {solution(1)}\npart two: {solution(2)}")