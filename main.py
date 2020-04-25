def show_field(current_state, size=3):
    cell_num = 1

    for line in range(size):
        for cell in range(size):
            print(f"[ {current_state[cell_num - 1]} {cell_num} ]", end='')
            cell_num += 1
        print("\n")
    print("\n\n")


def make_move(current_state, gamer):

    print(f"{'X' if gamer == 1 else 'O'}'s gamer turn")
    cell_num = int(input("Enter cell number: ")) - 1

    if current_state[cell_num] is '_':
        current_state[cell_num] = 'X' if gamer == 1 else 'O'
    else:
        print(f"cell {current_state[cell_num]} already occupied, look")
        show_field(current_state)
        print("try another one, please")
        make_move(current_state, gamer)

    return current_state


def check_final(current_state, gamer):
    #print(current_state)

    def a_eq_b(a, b):
        return a == b
    #print(list(map(a_eq_b, current_state[0], current_state[1])))
    show_field(current_state)

    return True


def start_game():
    make_turn()


def make_turn():
    current_state = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
    show_field(current_state)
    gamer = 1
    make_move(current_state, gamer)
    while check_final(current_state, gamer):
        gamer =  1 - gamer
        make_move(current_state, gamer)


def end_game():
    pass


start_game()
