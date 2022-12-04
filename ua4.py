player1score = 0
player2score = 0
tie = 0

n = int(input("How many times do you want to play? " ))

for i in range(0,n):
    print("Game", i+1)

    player1 =  input("Player 1 input: ")
    while ((player1!='R') and (player1!='P') and (player1!='S')):
            player1 = input('Invalid input. Player 1 input: ')
    player2 =  input("Player 2 input: ")
    while ((player2!='R') and (player2!='P') and (player2!='S')):
            player2 = input('Invalid input. Player 2 input: ')

    if player1 =="P":
        print("Player 1 choose paper.")
    elif player1 =="R":
        print("Player 1 choose rock.")
    else: 
        print("Player 1 choose scissors.")

    if player2 =="P":
        print("Player 2 choose paper.")
    elif player2 =="R":
        print("Player 2 choose rock.")
    else:
        print("Player 2 choose scissors.")

    if player1 == player2:
        print("It is a tie game.")
        tie = tie+1
    elif player1 =="R":
        if player2 == "P":
            print('The winner is player 2.')
            player2score = player2score+1
        else:
            print('The winner is player 1.')
            player1score = player1score+1
    elif player1 =="P":
        if player2 == "S":
            print('The winner is player 2.')
            player2score = player2score+1
        else:
            print('The winner is player 1.')
            player1score = player1score+1
    elif player1 =="S":
        if player2 == "R":
            print('The winner is player 2.')
            player2score = player2score+1
        else:
            print('The winner is player 1.')
            player1score = player1score+1
        
print("Overall result:")
print("Player 1 score : ", player1score)
print("Player 2 score : ", player2score)
print("Number of ties : ", tie)

if player1score > player2score:
    print("The overall winner is player 1.")
elif player2score > player1score:
    print("The overall winner is player 2.")
elif player1score == player2score:
    print("This is an overall tie.")

        