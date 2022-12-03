# index 0: Lose, 1: draw, 2: win
outcomes = {
    "A": "ZXY",
    "B": "XYZ",
    "C": "YZX"
}
outcome_points = lambda opponent_move, your_move: outcomes[opponent_move].index(your_move) * 3
shapes = "XYZ"
play_points = lambda shape: shapes.index(shape) + 1

with open("input.txt", "r") as file:
    data = file.readlines()
    data = [line.rstrip().replace(" ", "") for line in data]

def part_one():
    total_score = 0
    for match in data:
        opponent_move, your_move = match
        total_score += play_points(your_move)
        total_score += outcome_points(opponent_move, your_move)
    return total_score

given_outcome = shapes
outcome_from_char = lambda char: given_outcome.index(char)
get_your_move = lambda opponent_move, outcome: outcomes[opponent_move][outcome]
def part_two():
    total_score = 0
    for match in data:
        opponent_move, char_outcome = match
        outcome = outcome_from_char(char_outcome)
        your_move = get_your_move(opponent_move, outcome)
        total_score += play_points(your_move)
        total_score += outcome * 3
    return total_score

print(f"part one: {part_one()}")  
print(f"part two: {part_two()}")