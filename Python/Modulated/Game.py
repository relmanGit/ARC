from RubiksCube import *

def menu():
    print('Welcome to Project ARC - Ariel\'s Rubik\'s Cube')
    print()
    print('Valid inputs: R R2 R\' (and LUBFD [xyz soon], etc.)')
    print('Additional commands: reset, exit')
    print()

def game():
    global cube
    menu()
    save_HTML()
    open_HTML()
    while True:
        user_input = input('Enter a sequence of moves separated by spaces: ')
        if user_input.upper() == 'EXIT':
            return
        elif user_input.upper() == 'RESET':
            reset()
            continue
        split_input = user_input.upper().split() #splits on space
        #CURRENTLY RESTRICTED TO ONE CASE, REQS FIX FOR 2 LAYER TURNS
        #cmds - R,R2,R', and LUBFD
        for cmd in split_input:
            if cmd == 'R':
                R()
            elif cmd == 'R2':
                R2()
            elif cmd == 'R\'':
                Rprime()
            elif cmd == 'L':
                L()
            elif cmd == 'L2':
                L2()
            elif cmd == 'L\'':
                Lprime()
            elif cmd == 'U':
                U()
            elif cmd == 'U2':
                U2()
            elif cmd == 'U\'':
                Uprime()
            elif cmd == 'B':
                B()
            elif cmd == 'B2':
                B2()
            elif cmd == 'B\'':
                Bprime()
            elif cmd == 'F':
                F()
            elif cmd == 'F2':
                F2()
            elif cmd == 'F\'':
                Fprime()
            elif cmd == 'D':
                D()
            elif cmd == 'D2':
                D2()
            elif cmd == 'D\'':
                Dprime()
            else:
                print('Unknown input!', cmd)
        save_HTML()

game()
