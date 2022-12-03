with open("input.txt", "r") as file:
    data = file.readlines()

current_elf = 0
elf_cals = [0]
for row in data:
    if row == "\n":
        current_elf += 1
        elf_cals.append(0)
        continue
    cals = int(row.rstrip())
    elf_cals[current_elf] += cals

# by recursion
def get_top_cals(depth, elf_cals, top_what):
    if depth == top_what:
        c_max = max(elf_cals)
        elf_cals.remove(c_max)
        return c_max
    total = get_top_cals(depth+1, elf_cals, top_what)
    c_max = max(elf_cals)
    elf_cals.remove(c_max) 
    total += c_max
    return total
print(get_top_cals(1, elf_cals, 3))