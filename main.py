from math import sqrt


def show_field(current_state, size=3):
    cell_num = 1

    for line in range(size):
        for cell in range(size):
            print(f"[ {current_state[cell_num - 1]} {cell_num} ]", end='')
            cell_num += 1
        print("\n")
    print("\n\n")


def process_user_input():
    pass

    # cell_num = 0
    # print(f"{'X' if gamer == 1 else 'O'}'s gamer turn")
    # try:
    #     cell_num = int(input("Enter cell number: "))
    # except ValueError as e:
    #     print(F"Wrong input type, please insert number more than 0 and less or equal {len(current_state)}")
    #     make_move(current_state, gamer)
    #
    # if cell_num <= 0 or cell_num >= len(current_state):
    #     print(F"{cell_num} is wrong input, please insert number more than 0 and less or equal {len(current_state)}")
    #     make_move(current_state, gamer)
    # else:
    #     cell_num -= 1


def make_move(current_state, gamer):
    # process_user_input()
    print(f"{'X' if gamer else 'O'}'s turn")
    cell_num = int(input("Enter cell number: ")) - 1

    if current_state[cell_num] == '_':
        current_state[cell_num] = 'X' if gamer else 'O'
    else:
        print(f"cell {current_state[cell_num]} already occupied, look")
        show_field(current_state)
        print("try another one, please")
        make_move(current_state, gamer)

    return current_state


def check_final(current_state):
    show_field(current_state)

    def check_line(line):
        item_compare_with = line[0]
        for item in line:
            if item == '_' or item != item_compare_with: return False
        return True

    size = int(sqrt(len(current_state)))

    def chunks(lst, n):
        """Yield successive n-sized chunks from lst."""
        for i in range(0, len(lst), n):
            yield lst[i:i + n]

    for line in chunks(current_state, size):
        if check_line(line):
            # gamer = 'winner', game finished
            return False

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
    if int(input("Press 8 to start new game, or 13 to finish: ")) == 8:
        start_game()
    else:
        exit(0)


start_game()
