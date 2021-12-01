def read_file(filename: str):
    depths = []
    with open(filename) as new_file:
        for line in new_file:
            depths.append(int(line.strip()))

    return depths

def count_increases(depths: list):
    count = 0
    for i in range(len(depths)):
        if i == 0:
            continue

        if depths[i] > depths[i-1]:
            count += 1

    return count

def create_part_two(depths: list):
    part_two_depths = []
    for i in range(len(depths)-2):
        part_two_depths.append(depths[i]+depths[i+1]+depths[i+2])

    return part_two_depths

if __name__ == '__main__':
    depths = read_file('input.txt')

    # part one
    part_one_count = count_increases(depths)
    print(f'The answer to part one is: {part_one_count}')

    #part two
    depths_two = create_part_two(depths)
    part_two_count = count_increases(depths_two)
    print(f'The answer to part two is: {part_two_count}')