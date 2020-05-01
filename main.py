def show_field(current_state, size=3):
    cell_num = 1

    for line in range(size):
        for cell in range(size):
            print(f" {current_state[cell_num - 1]} {cell_num}", end='')
            cell_num += 1
        print("\n")
    print("\n")


def process_user_input():
    while True:
        try:
            usr_input = int(input(": "))
            break
        except Exception as e:
            print(F"Error {e}. Wrong input type, please insert number", end='')

    return usr_input


def make_move(current_state, gamer):
    while True:
        print(f"{'X' if gamer else 'O'}'s turn")
        print("Enter cell number", end='')

        cell_num = process_user_input()

        if cell_num > len(current_state) or cell_num <= 0:
            print(f"Cell number should be between 1 and {len(current_state)} but was {cell_num}")
            print("try another one, please")
        elif current_state[cell_num - 1] != '_':
            print(f"cell {cell_num} already occupied, look at field")
            show_field(current_state)
            print("try another one, please")
        else:
            break

    current_state[cell_num - 1] = 'X' if gamer else 'O'

    return current_state


def check_final(f):
    show_field(f)

    def check_line(line_in_checkline):
        item_compare_with = line_in_checkline[0]
        for item in line_in_checkline:
            if item == '_' or item != item_compare_with: return False
        return True

    all_wins_lines = [[f[0], f[1], f[2]], [f[3], f[4], f[5]], [f[6], f[7], f[8]],
                      [f[0], f[3], f[6]], [f[1], f[4], f[7]], [f[2], f[5], f[8]],
                      [f[0], f[4], f[8]], [f[2], f[4], f[6]]
                      ]

    for line in all_wins_lines:
        if check_line(line):
            return False  # gamer = 'winner', game finished

    return True


def start_game():
    make_turn()


def make_turn():
    current_state = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
    gamer = 0
    while check_final(current_state):
        gamer = 1 - gamer
        make_move(current_state, gamer)

    print(f"{'X' if gamer else 'O'} wins, game finished")
    end_game()


def end_game():
    print("Press 8 to start new game, or 13 to finish", end='')
    usr_input = process_user_input()
    if usr_input == 8:
        start_game()
    else:
        print("See ya!")
        exit(0)


start_game()
