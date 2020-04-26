from math import sqrt


def show_field(current_state, size=3):
    cell_num = 1

    for line in range(size):
        for cell in range(size):
            print(f"[ {current_state[cell_num - 1]} {cell_num} ]", end='')
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
    
    print("Press 8 to start new game, or 13 to finish", end='')
    usr_input = process_user_input()
    if usr_input == 8:
        start_game()
    else:
        print("See ya!")
        exit(0)


start_game()
