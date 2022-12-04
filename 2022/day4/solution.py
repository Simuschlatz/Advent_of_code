with open("input.txt", "r") as file:
    data = file.readlines()
    data = [[int(char) for char in line.rstrip().replace("-", ",").split(",")] for line in data]

def is_contained(i1, j1, i2, j2):
    return (i1 <= i2 and j1 >= j2) or (i2 <= i1 and j2 >= j1)

def overlaps(i1, j1, i2, j2):
    return i1 <= j2 and j1 >= i2
    
contained = 0
num_overlaps = 0
for pair in data:
    contained += is_contained(*pair)
    num_overlaps += overlaps(*pair)
print(f"part one: {contained} \npart two: {num_overlaps}")