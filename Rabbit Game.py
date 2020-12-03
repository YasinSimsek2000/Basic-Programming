import ast

map = list(ast.literal_eval(input('Please enter feeding map as a list: \n')))
plan = list(ast.literal_eval(input('Please enter direction of movements as a list: \n')))

global horizontal, vertical, Posions, Walls, value
horizontal, vertical, Posions, Walls, value = 0, 0, [], [], 0
Score, Items = 0, {'C': 10, 'A': 5, 'M': -5, 'X': 0}

def printing_board(x):
    for i in x:
        for j in i:
            print(j, end=' ')
            if j == 'P':
                Posions.append([map.index(i), map[map.index(i)].index(j)])
            elif j == 'W':
                Walls.append([map.index(i), map[map.index(i)].index(j)])
            elif j == '*':
                horizontal, vertical = map.index(i), map[map.index(i)].index(j)
        print(' ')
    return [horizontal, vertical]

print('Your board is: ')
a = printing_board(map)
horizontal, vertical = a[0], a[1]

def next_index(x):
    a = horizontal
    b = vertical
    if x == 'U':
        a = horizontal - 1
    elif x == 'D':
        a = horizontal + 1
    elif x == 'L':
        b = vertical - 1
    elif x == 'R':
        b = vertical + 1
    new_position = [a, b]
    return new_position

for step in plan:
    step = next_index(step)
    if step[0] < 0 or step[1] < 0 or step[0] > len(map) or step[1] > len(map):
        continue
    elif step in Walls:
        continue
    elif step in Posions:
        map[horizontal][vertical], map[step[0]][step[1]] = 'X', '*'
        break
    else:
        value = map[step[0]][step[1]]
        Score += Items[value]
        map[horizontal][vertical] = 'X'
        horizontal, vertical = step[0], step[1]
        map[horizontal][vertical] = '*'

print('Your output should be like this: ')
printing_board(map)
print('Your score is', Score)