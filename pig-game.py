import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    
    return roll

while True:
  players = input('Enter num of players 2-4 >')
  if players.isdigit():
      players = int(players)
      if 2 <= players <= 4:
          break
      
      else:
          print('Invalid input enter 2-4')

max_score = 100
players_scores = [0 for _ in range(players)]

while max(players_scores) < max_score:
    
    for player_index in range(players):
      print("\nPlayer", player_index + 1, "turn has just started")
      current_score = 0
    
      while True:
          option1 = input('Would you like to roll? (y/n) ')
          if option1.lower() != 'y':
              break
          
          value = roll()
          if value == 1:
              print('You rolled 1 turn done')
              current_score = 0
              break
              
          else:
              current_score += value
              print("You rolled a >", value)
              
          print("Your score is:", current_score)
          
      players_scores[player_index] += current_score
      print("Your total score is >", players_scores[player_index])
          

    
