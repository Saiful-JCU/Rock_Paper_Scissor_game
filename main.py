def get_winner(p1, p2):
    if p1 == p2:
        return "It's a tie!"
    elif p1 == 'rock':
        if p2 == 'scissors':
            return 'First player wins!'
        else:
            return 'Second player wins!'
    elif p1 == 'scissors':
        if p2 == 'paper':
            return 'first player wins!'
        else:
            return 'second player wins!'
    elif p1 == 'paper':
        if p2 == 'rock':
            return 'First player wins!'
        else:
            return 'Second player wins!'
    else:
        return 'Invalid Input!'
player1 = input('First player: rock, paper, scissor___ ')
player2 = input('Second player: rock, paper, scissor___ ')
print(get_winner(player1, player2))
