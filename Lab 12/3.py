import random

dice1 = [1, 2, 3, 4, 5, 6]
dice2 = [1, 2, 3, 4, 5, 6]

player1_score = random.choice(dice1) + random.choice(dice2)
player2_score = random.choice(dice1) + random.choice(dice2)

print("Player 1 rolled:", player1_score)
print("Player 2 rolled:", player2_score)

if player1_score > player2_score:
    print("Player 1 wins!")
elif player2_score > player1_score:
    print("Player 2 wins!")
else:
    print("It's a tie!")
