player1 =  input("Player 1 input: ")
while ((player1!='R') and (player1!='P') and (player1!='S')):
        player1 = input('Invalid input. Player 1 input: ')
player2 =  input("Player 2 input: ")
while ((player2!='R') and (player2!='P') and (player2!='S')):
        player2 = input('Invalid input. Player 2 input: ')
        
if player1 == player2:
    print("It is a tie game.")
elif player1 =="R":
    if player2 == "P":
        print('The winner is player 2.')
    else:
        print('The winner is player 1.')
elif player1 =="P":
    if player2 == "S":
        print('The winner is player 2.')
    else:
        print('The winner is player 1.')
elif player1 =="S":
    if player2 == "R":
        print('The winner is player 2.')
    else:
        print('The winner is player 1.')
        

        