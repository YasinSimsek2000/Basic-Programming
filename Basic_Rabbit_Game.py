map0 = open('Basic_Rabbit_Game_Map.txt', 'r+')
map1 = [x.split() for x in map0.readlines()]

Hollows, Walls, Score, Move = [],[], 0, 0
Items = {'B':lambda x: x+5, 'C':lambda x: x+15, 'P':lambda x: x-15, 'M':lambda x: x-5, 'X':lambda x: x, 'F':lambda x: x}

for i in range(len(map1)):
        for j in range(len(map1[0])):
            item = map1[i][j]
            print(item, end=' ')
            if item == 'W':
                Walls.append((i,j))
            elif item == '*':
                horizontal, vertical = i,j
        print(' ')
        
Walls = tuple(Walls)

def printing_board(x):
    print()
    for i in x:
        for j in i:
            print(j, end=' ')
        print(' ')
    print()
    return x

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
    if a < 0 or b < 0 or a == len(map1) or b == len(map1[0]):
        exit('You are lost!')
    new_position = (a, b)
    return new_position

while True:
    Move += 1
    step = input()
    step = next_index(step)
    if step in Walls:
        print('You cannot pass walls!')
        continue
    else:
        Position = map1[step[0]][step[1]]
        if Position == 'H':
            print('You fell into hollow!')
            break
        Score = Items[Position](Score)
        map1[horizontal][vertical] = 'X'
        horizontal, vertical = step[0], step[1]
        map1[horizontal][vertical] = '*'
        printing_board(map1)
        if Position == 'F':
            print('You reached finish line :D Your score is:', Score)
            break
