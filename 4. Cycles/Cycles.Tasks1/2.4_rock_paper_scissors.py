import random

print("Let's start the game!.")
pieces = ('rock', 'scissors', 'paper')
while True:
    tries = 0
    usr_count = 0
    comp_count = 0
    while True:
        comp_piece = random.choice(pieces)
        usr_piece = input("Rock, scissors, paper. One, two, three! Choose your piece: ")
        print(f"Computer's choice: {comp_piece}")
        if usr_piece not in pieces:
            print("Please use correct elements.")
            break
        elif comp_piece == usr_piece:
            print("It's a tie!")
            if tries >= 5:
                print("The game ended in a draw!")
                break
        else:
            if comp_piece == 'rock' and usr_piece == 'scissors' \
                or comp_piece == 'scissors' and usr_piece == 'paper' \
                or comp_piece == 'paper' and usr_piece == 'rock':
                    print("Computer wins!")
                    comp_count += 1
                    usr_count = 0
            else:
                print("You win!")
                usr_count += 1
                comp_count = 0
            if comp_count == 2:
                print("Сomputer won. Two victories in a row!")
            elif usr_count == 2:
                print("You won. Two victories in a row!")
        tries += 1
    usrInput = input("Press any key to continue or q to exit ")
    if usrInput == 'q':
        break