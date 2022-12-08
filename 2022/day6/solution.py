with open("input.txt", "r") as file:
    data = file.read()
def solution(distinct_chars):
    for pointer in range(len(data) - distinct_chars + 1):
        batch = data[pointer:pointer+distinct_chars]
        if len(set(batch)) == len(batch):
            return pointer + distinct_chars
print(f"part one: {solution(4)}", f"part two: {solution(14)}", sep="\n")