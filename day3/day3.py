import collections

def prep_file(filename: str):
    with open(filename) as new_file:
        return [c.strip() for c in new_file]

def power_consumption(values: list):
    
    gamma_rate = ''
    for i in range(12):
        count = 0
        for j in range(len(file)):
            if file[j][i] == '1':
                count += 1
        if count > len(file)/2:     # if there are more 1s than 0s
            gamma_rate += '1'
        else:
            gamma_rate += '0'

    epsilon_rate = ''.join('1' if x == '0' else '0' for x in gamma_rate)

    return(int(gamma_rate,2)*int(epsilon_rate,2))

if __name__ == '__main__':
    file = prep_file('input.txt')

    consumption = power_consumption(file)
    print(f'The answer to part 1 is: {consumption}')