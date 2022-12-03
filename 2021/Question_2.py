from os import defpath
with open("pilot_this_shit.txt", "r") as file:
    cmds = file.read()
    print(cmds)
cmds = cmds.split("\n")

x = 0
depth = 0
aim = 0

for element in cmds:
    command_and_value = element.split(" ")
    print(command_and_value)
    if command_and_value[0] == "forward":
        x += int(command_and_value[1])
        depth += (int(command_and_value[1]) * aim)
    if command_and_value[0] == "down":
        aim += int(command_and_value[1])
    if command_and_value[0] == "up":
        aim -= int(command_and_value[1])

print(x * depth)