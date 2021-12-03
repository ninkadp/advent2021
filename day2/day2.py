def move_pt_1(direction: str, change: int, location: list):
    if direction == 'forward':
        location[0] += change  # location[0] is x coord.

    if direction == 'up':
        location[1] -= change  # location[1] is y coord, "up" => smaller depth

    if direction == 'down':
        location[1] += change  # location[1] is y coord, "down" => greater depth

def move_pt_2(direction: str, change: int, location: list):
    if direction == 'forward':
        location[0] += change
        location[1] += location[2]*change

    if direction == 'up':
        location[2] -= change

    if direction == 'down':
        location[2] += change

def prep_file(filename: str):
    with open(filename) as new_file:
        return [(c.split()[0], int(c.split()[1])) for c in new_file.read().splitlines()]

if __name__ == '__main__':
    directions = prep_file('input.txt')     # get list of directions
    position_pt_1 = [0,0]                        # starting position is (0,0)

    for step in directions:
        move_pt_1(step[0], step[1], position_pt_1)

    print(f'the answer to part 1 is: {position_pt_1[0]*position_pt_1[1]}')

    position_pt_2 = [0,0,0]

    for step in directions:
        move_pt_2(step[0], step[1], position_pt_2)

    print(f'the answer to part 2 is: {position_pt_2[0]*position_pt_2[1]}')