p1s = 0
p2s = 0
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
            p2s = p2s+1
        else:
            print('The winner is player 1.')
            p1s = p1s+1
    elif player1 =="P":
        if player2 == "S":
            print('The winner is player 2.')
            p2s = p2s+1
        else:
            print('The winner is player 1.')
            p1s = p1s+1
    elif player1 =="S":
        if player2 == "R":
            print('The winner is player 2.')
            p2s = p2s+1
        else:
            print('The winner is player 1.')
            p1s = p1s+1
        
print("Overall result:")
print("Player 1 score : ", p1s)
print("Player 2 score : ", p2s)
print("Number of ties : ", tie)

if p1s > p2s:
    print("The overall winner is player 1.")
elif p2s > p1s:
    print("The overall winner is player 2.")
elif p1s == p2s:
    print("This is an overall tie.")

        