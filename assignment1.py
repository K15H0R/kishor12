import random

shapes = ['Rock', 'Paper', 'Scissors']
scores = {'Rock': 1, 'Paper': 2, 'Scissors': 3}

def play_round(player_shape):
    computer_shape = random.choice(shapes)
    outcome = (scores[player_shape] - scores[computer_shape]) % 3
    
    if outcome == 0:
        return 0
    elif outcome == 1:
        return 6
    else:
        return 3

total_score = 0

# Example of playing 5 rounds
for _ in range(5):
    player_shape = random.choice(shapes)
    round_score = play_round(player_shape)
    total_score += scores[player_shape] + round_score

print(f"Total Score: {total_score}")
