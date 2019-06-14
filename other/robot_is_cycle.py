def is_cycle(moves):
    moves = list(moves.upper())

    x = y = 0
    for move in moves:
        if move == 'R':
            x += 1
        elif move == 'L':
            x += -1
        elif move == 'U':
            y += 1
        elif move == 'D':
            y = -1
    return y == 0 and x == 0

def main():
    if is_cycle('RLUDDRRULLRULDRRLLUUDDDU'):
        print('程式狗已回到原點')
    else:
        print('程式狗沒有回到原點')

if __name__ == '__main__':
    main()