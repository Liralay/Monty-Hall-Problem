import random

wins = 0
loses = 0

wins1 = 0
loses1 = 0


num_simulations = 10000
for i in range(num_simulations):
    doors = [0, 0, 1]
    random.shuffle(doors)
    
    user_choice = random.choice([0, 1, 2])
    
    host_choice = next(i for i in range(3) if i != user_choice and doors[i] == 0)
    
    new_user_choice = next(i for i in range(3) if i != user_choice and i != host_choice)
    
    if doors[user_choice] == 1:
        wins += 1
    else:
        loses += 1

    if doors[new_user_choice] == 1:
        wins1 += 1
    else:
        loses1 += 1

print(f"Wins: {wins}, Loses: {loses} if you don't switch. Winrate: {int((wins/num_simulations*100))}%")
print(f"Wins: {wins1}, Loses: {loses1} if you switch. Winrate: {(int(wins1/num_simulations*100))}%")
