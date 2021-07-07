# Chapter 9 Exercises

# Review Questions (True/False)
# 1. False. It is pseudo-random numbers.

# 2. False. It returns a pseudo-random float number between 0 <= x < 1.

# 3. True.

# 4. True.

# 5. True.

# 6. True.

# 7. True.

# 8. False. They are not subsitute but complementary.

# 9. False.

# 10. False.


# Multiple Choice
# 1. C (random() < 0.66)
# 2. C (Construct a simplified prototype of the system.)
# 3. D (structure chart)
# 4. A (information flow)
# 5. C (functions)
# 6. A (Monte Carlo)
# 7. B (prototype)
# 8. A (bool)
# 9. A (%)
# 10. B (the bottom)


# Discussion
# 1.
#                                            /----------------------\
#               /--------------------------Main --------\            \
#              /                     /       \           \            \
#             /                     /         \           \            \
#            /                     /           \     (amtNeeded)        \
#           /                     /             \            \           |
#          /             (length, width)   (length, width)   /   (length, width, amtNeeded)
#         /                     /                 \         /            |
#    printIntro()        getDimensions()         amtNeeded()        printReport

# # 2.
# # a.
# from random import randrange
# from random import uniform
# print(randrange(0, 11))
#
# # b.
# print(uniform(-0.5, 0.5))
#
# # c.
# print(randrange(1, 7))
#
# # d.
# print(randrange(2, 12))
#
# # e.
# print(uniform(-10, 10))
#
# # 3.


# Programming Exercises
# # 1.
# from random import random
# def main():
#     print_intro()
#     prob_a, prob_b, n = get_inputs()
#     wins_a, wins_b = simNGames(n, prob_a, prob_b)
#     print_summary(wins_a, wins_b)
#
#
# def print_intro():
#     print("This program simulates a game of racquetball between two")
#     print('players called "A" and "B". The ability of each player is')
#     print("indicated by a probability (a number between 0 and 1) that")
#     print("the player wins the point when serving. Player A always")
#     print("has the first serve.")
#
#
# def get_inputs():
#     # Returns the three simulation parameters
#     a = float(input("What is the prob. player A wins a serve? "))
#     b = float(input("What is the prob. player B wins a serve? "))
#     n = int(input("How many games to simulate? "))
#     return a, b, n
#
#
# def simNGames(n, prob_a, prob_b):
#     # Simulates n games of racquetball between players whose
#     # abilities are represented by the probability of winning a serve.
#     # Returns number of wins for A and B
#     wins_a = wins_b = 0
#     game = 0
#     while (wins_a <= n / 2) and (wins_b <= n / 2):
#         game = game + 1
#         if game % 2 != 0:
#             score_a, score_b = simOneGame(prob_a, prob_b, 'A')
#         else:
#             score_a, score_b = simOneGame(prob_a, prob_b, 'B')
#
#         if score_a > score_b:
#             wins_a += 1
#         else:
#             wins_b += 1
#
#     return wins_a, wins_b
#
#
# def simOneGame(prob_a, prob_b, serving):
#     # Simulates a single game or racquetball between players whose
#     # abilities are represented by the probability of winning a serve.
#     # Returns final scores for A and B
#     score_a = score_b = 0
#     while not gameOver(score_a, score_b):
#         if serving == "A":
#             if random() < prob_a:
#                 score_a += 1
#             else:
#                 serving = "B"
#         else:
#             if random() < prob_b:
#                 score_b += 1
#             else:
#                 serving = 'A'
#
#     return score_a, score_b
#
#
# def gameOver(a, b):
#     # a and b represent scores for a racquetball game
#     # Returns True if the game is over, False otherwise.
#     return a == 15 or b == 15
#
#
# def print_summary(wins_a, wins_b):
#     # Prints a summary of wins for each player.
#     n = wins_a + wins_b
#     print("\nGames simulated: ", n)
#     print("Wins for A: {0} ({1: 0.1%})".format(wins_a, wins_a / n))
#     print("Wins for B: {0} ({1: 0.1%})".format(wins_b, wins_b / n))
#
#
# if __name__ == '__main__': main()
#
# # 2.
# from random import random
# def main():
#     print_intro()
#     prob_a, prob_b, n = get_inputs()
#     wins_a, wins_b, shutout_a, shutout_b = simNGames(n, prob_a, prob_b)
#     print_summary(wins_a, wins_b, shutout_a, shutout_b)
#
#
# def print_intro():
#     print("This program simulates a game of racquetball between two")
#     print('players called "A" and "B". The ability of each player is')
#     print("indicated by a probability (a number between 0 and 1) that")
#     print("the player wins the point when serving. Player A has the")
#     print("first serve in the odd games of the match, and player B")
#     print("serves first in the even games. Moreover, it reports the")
#     print("number of shutout and percentage of wins that are shutouts")
#     print("for each player.")
#
#
# def get_inputs():
#     # Returns the three simulation parameters
#     a = float(input("What is the prob. player A wins a serve? "))
#     b = float(input("What is the prob. player B wins a serve? "))
#     n = int(input("How many games to simulate? "))
#     return a, b, n
#
#
# def simNGames(n, prob_a, prob_b):
#     # Simulates n games of racquetball between players whose
#     # abilities are represented by the probability of winning a serve.
#     # Returns number of wins for A and B
#     wins_a = wins_b = 0
#     shutout_a = shutout_b = 0
#     game = 0
#     while (wins_a <= n / 2) and (wins_b <= n / 2):
#         game = game + 1
#         if game % 2 != 0:
#             score_a, score_b = simOneGame(prob_a, prob_b, 'A')
#         else:
#             score_a, score_b = simOneGame(prob_a, prob_b, 'B')
#
#         if score_a > score_b:
#             wins_a += 1
#         else:
#             wins_b += 1
#
#         if not score_a:
#             shutout_b += 1
#         elif not score_b:
#             shutout_a += 1
#
#     return wins_a, wins_b, shutout_a, shutout_b
#
#
# def simOneGame(prob_a, prob_b, serving):
#     # Simulates a single game or racquetball between players whose
#     # abilities are represented by the probability of winning a serve.
#     # Returns final scores for A and B
#     score_a = score_b = 0
#
#     while not gameOver(score_a, score_b):
#         if serving == "A":
#             if random() < prob_a:
#                 score_a += 1
#             else:
#                 serving = "B"
#         else:
#             if random() < prob_b:
#                 score_b += 1
#             else:
#                 serving = 'A'
#
#     return score_a, score_b
#
#
# def gameOver(a, b):
#     # a and b represent scores for a racquetball game
#     # Returns True if the game is over, False otherwise.
#     return a == 15 or b == 15
#
#
# def print_summary(wins_a, wins_b, shutout_a, shutout_b):
#     # Prints a summary of wins for each player.
#     n = wins_a + wins_b
#     print("\nGames simulated: ", n)
#     print("Wins for A: {0} ({1: 0.1%})".format(wins_a, wins_a / n))
#     print("Shutout for A: {0} ({1: 0.1%})".format(shutout_a, shutout_a / wins_a))
#     print("Wins for B: {0} ({1: 0.1%})".format(wins_b, wins_b / n))
#     print("Shutout for B: {0} ({1: 0.1%})".format(shutout_b, shutout_b / wins_b))
#
#
# if __name__ == '__main__': main()
#
# # 3.
# from random import random
# import time
# def main():
#     print_intro()
#     prob_a, prob_b, n = get_inputs()
#     wins_a, wins_b = sim_n_games(n, prob_a, prob_b)
#     print_summary(wins_a, wins_b)
#
#
# def print_intro():
#     print('This program simulates a game of volleyball between two')
#     print('teams called "A" and "B". The ability of each team is')
#     print('indicated by a probability (a number between 0 and 1) that')
#     print('the team wins the point when serving. Team A always')
#     print('has the first serve.')
#
#
# def get_inputs():
#     # Returns the three simulation parameters
#     a = float(input('What is the prob. team A wins a serve? '))
#     b = float(input('What is the prob. team B wins a serve? '))
#     n = int(input('How many games to simulate? '))
#     return a, b, n
#
#
# def sim_n_games(n, prob_a, prob_b):
#     # Simulates n games of volleyball between teams whose
#     #   abilities are represented by the probability of winning a serve.
#     # Returns number of wins for A and B
#     wins_a = wins_b = 0
#     for i in range(n):
#         score_a, score_b = sim_one_game(prob_a, prob_b)
#         if score_a > score_b:
#             wins_a += 1
#         else:
#             wins_b += 1
#     return wins_a, wins_b
#
#
# def sim_one_game(prob_a, prob_b):
#     # Simulates a single game of volleyball between teams whose
#     #   abilities are represented by the probability of winning a serve.
#     # Returns final scores for A and B
#     serving = 'A'
#     score_a = score_b = 0
#     while not game_over(score_a, score_b):
#         if serving == 'A':
#             if random() < prob_a:
#                 score_a += 1
#             else:
#                 serving = 'B'
#         else:
#             if random() < prob_b:
#                 score_b += 1
#             else:
#                 serving = 'A'
#     return score_a, score_b
#
#
# def game_over(a, b):
#     # a and b represent scores for a volleyball game
#     # Returns True if the game is over, False otherwise.
#     return (a >= 15 or b >= 15) and (abs(a - b) >= 2)
#
#
# def print_summary(wins_a, wins_b):
#     # Prints a summary of wins for each team.
#     n = wins_a + wins_b
#     print('\nGames simulated: {0}'.format(n))
#     print('Wins for A: {0} ({1:0.1%})'.format(wins_a, wins_a / n))
#     print('Wins for B: {0} ({1:0.1%})'.format(wins_b, wins_b / n))
#
#
# if __name__ == '__main__': main()
#
# # 4.
# from random import random
# def main():
#     print_intro()
#     prob_a, prob_b, n = get_inputs()
#     wins_a, wins_b = sim_n_games(n, prob_a, prob_b)
#     print_summary(wins_a, wins_b)
#
#
# def print_intro():
#     print('This program simulates a game of volleyball between two')
#     print('teams called "A" and "B". The ability of each team is')
#     print('indicated by a probability (a number between 0 and 1) that')
#     print('the team wins based on rally scoring. Team A always')
#     print('has the first serve.')
#
#
# def get_inputs():
#     # Returns the three simulation parameters
#     a = float(input('What is the prob. team A wins a serve? '))
#     b = float(input('What is the prob. team B wins a serve? '))
#     n = int(input('How many games to simulate? '))
#     return a, b, n
#
#
# def sim_n_games(n, prob_a, prob_b):
#     # Simulates n games of volleyball between teams whose
#     #   abilities are represented by the probability of winning a serve.
#     # Returns number of wins for A and B
#     wins_a = wins_b = 0
#     for i in range(n):
#         score_a, score_b = sim_one_game(prob_a, prob_b)
#         if score_a > score_b:
#             wins_a += 1
#         else:
#             wins_b += 1
#     return wins_a, wins_b
#
#
# def sim_one_game(prob_a, prob_b):
#     # Simulates a single game of volleyball between teams whose
#     #   abilities are represented by the probability of winning a serve.
#     # Returns final scores for A and B
#     serving = 'A'
#     score_a = score_b = 0
#     while not game_over(score_a, score_b):
#         if serving == 'A':
#             if random() < prob_a:
#                 score_a += 1
#             else:
#                 score_b += 1
#                 serving = 'B'
#         else:
#             if random() < prob_b:
#                 score_b += 1
#             else:
#                 score_a += 1
#                 serving = 'A'
#
#     return score_a, score_b
#
#
# def game_over(a, b):
#     # a and b represent scores for a volleyball game
#     # Returns True if the game is over, False otherwise.
#     return a == 25 or b == 25
#
#
# def print_summary(wins_a, wins_b):
#     # Prints a summary of wins for each team.
#     n = wins_a + wins_b
#     print('\nGames simulated: {0}'.format(n))
#     print('Wins for A: {0} ({1:0.1%})'.format(wins_a, wins_a / n))
#     print('Wins for B: {0} ({1:0.1%})'.format(wins_b, wins_b / n))
#
#
# if __name__ == '__main__': main()
#
# # 5.
# from random import random
# def main():
#     print_intro()
#     prob_a, prob_b, n, m = get_inputs()
#     rally_advantage, regular_advantage = compare_rally_vs_regular(n, prob_a, prob_b)
#     print_summary(n, rally_advantage, regular_advantage)
#
#
# def print_intro():
#     print('This program simulates a game of volleyball between two')
#     print('teams called "A" and "B". The ability of each team is')
#     print('indicated by a probability (a number between 0 and 1). The')
#     print('program investigates whether rally scoring magnifies, reduces,')
#     print('or has no effect on the relative advantage enjoyed by the')
#     print('better team when compared with regular volleyball. Team A')
#     print('always has the first serve.')
#
#
# def get_inputs():
#     # Returns the three simulation parameters
#     a = float(input('What is the prob. team A wins a serve? '))
#     b = float(input('What is the prob. team B wins a serve? '))
#     n = int(input('How many times to simulate? '))
#     m = int(input('How may games per simulation? '))
#     return a, b, n, m
#
#
# def compare_rally_vs_regular(n, prob_a, prob_b):
#     rally_advantage = 0
#     regular_advantage = 0
#     for i in range(n):
#         rally_wins_a, rally_wins_b, regular_wins_a, regular_wins_b = sim_m_games(n, prob_a, prob_b)
#         if prob_a > prob_b:
#             if rally_wins_a > rally_wins_b:
#                 rally_advantage += 1
#             elif regular_wins_a >= regular_wins_b:
#                 regular_advantage += 1
#         else:
#             if rally_wins_b > rally_wins_a:
#                 rally_advantage += 1
#             elif regular_wins_b >= regular_wins_b:
#                 regular_advantage += 1
#
#     return rally_advantage, regular_advantage
#
#
# def sim_m_games(m, prob_a, prob_b):
#     # Simulates n games of volleyball between teams whose
#     #   abilities are represented by the probability of winning a serve.
#     # Returns number of wins for A and B
#     rally_wins_a = rally_wins_b = 0
#     regular_wins_a = regular_wins_b = 0
#     for i in range(m):
#         rally_score_a, rally_score_b = sim_one_game_rally(prob_a, prob_b)
#         regular_score_a, regular_score_b = sim_one_game_regular(prob_a, prob_b)
#
#         if rally_score_a > rally_score_b:
#             rally_wins_a += 1
#         else:
#             rally_wins_b += 1
#
#         if regular_score_a > regular_score_b:
#             regular_wins_a += 1
#         else:
#             regular_wins_b += 1
#
#     return rally_wins_a, rally_wins_b, regular_wins_a, regular_wins_b
#
#
# def sim_one_game_rally(prob_a, prob_b):
#     # Simulates a single game of rally volleyball between teams whose
#     #   abilities are represented by the probability of winning a serve.
#     # Returns final scores for A and B
#     serving = 'A'
#     score_a = score_b = 0
#     while not game_over_rally(score_a, score_b):
#         if serving == 'A':
#             if random() < prob_a:
#                 score_a += 1
#             else:
#                 score_b += 1
#                 serving = 'B'
#         else:
#             if random() < prob_b:
#                 score_b += 1
#             else:
#                 score_a += 1
#                 serving = 'A'
#
#     return score_a, score_b
#
#
# def sim_one_game_regular(prob_a, prob_b):
#     # Simulates a single game of regular volleyball between teams whose
#     #   abilities are represented by the probability of winning a serve.
#     # Returns final scores for A and B
#     serving = 'A'
#     score_a = score_b = 0
#     while not game_over_regular(score_a, score_b):
#         if serving == 'A':
#             if random() < prob_a:
#                 score_a += 1
#             else:
#                 serving = 'B'
#         else:
#             if random() < prob_b:
#                 score_b += 1
#             else:
#                 serving = 'A'
#
#     return score_a, score_b
#
#
# def game_over_rally(a, b):
#     # a and b represent scores for a volleyball game
#     # Returns True if the game is over, False otherwise.
#     return a == 25 or b == 25
#
#
# def game_over_regular(a, b):
#     # a and b represent scores for a volleyball game
#     # Returns True if the game is over, False otherwise.
#     return (a >= 15 or b >= 15) and (abs(a - b) >= 2)
#
#
# def print_summary(n, rally_advantage, regular_advantage):
#     # Prints a summary of wins for each team.
#     print('\nTimes simulated: {0}'.format(n))
#     print('Wins for better team (rally scoring): {}'.format(rally_advantage))
#     print('Wins for better team (regular scoring): {}'.format(regular_advantage))
#
#
# if __name__ == '__main__': main()
#
# # 6.
# from random import random
# def main():
#     print_intro()
#     prob_a, prob_b, n = get_inputs()
#     wins_a, wins_b = sim_n_games(n, prob_a, prob_b)
#     print_summary(wins_a, wins_b)
#
#
# def print_intro():
#     print('This program simulates a game of table tennis between two')
#     print('players called "A" and "B". The ability of each player is')
#     print('indicated by a probability (a number between 0 and 1). Team A')
#     print('always has the first serve. The winner is decided by the best')
#     print('of n games. A player can win points, even he/she was not the')
#     print('serving player. (https://www.teamusa.org/usa-table-tennis/rules)')
#
#
# def get_inputs():
#     # Returns the three simulation parameters
#     a = float(input('What is the prob. team A wins a serve? '))
#     b = float(input('What is the prob. team B wins a serve? '))
#     n = int(input('How many games to simulate? '))
#     return a, b, n
#
#
# def sim_n_games(n, prob_a, prob_b):
#     # Simulates n games of table tennis between teams whose
#     #   abilities are represented by the probability of winning a serve.
#     # Returns number of wins for A and B
#     wins_a = wins_b = 0
#     while (wins_a <= n / 2) and (wins_b <= n / 2):
#         score_a, score_b = sim_one_game(prob_a, prob_b)
#         if score_a > score_b:
#             wins_a += 1
#         else:
#             wins_b += 1
#     return wins_a, wins_b
#
#
# def sim_one_game(prob_a, prob_b):
#     # Simulates a single game of table tennis between teams whose
#     #   abilities are represented by the probability of winning a serve.
#     # Returns final scores for A and B
#     serving = 'A'
#     score_a = score_b = 0
#     while not game_over(score_a, score_b):
#         if serving == 'A':
#             if random() < prob_a:
#                 score_a += 1
#             else:
#                 score_b += 1
#         else:
#             if random() < prob_b:
#                 score_b += 1
#             else:
#                 score_a += 1
#
#         total_score = score_a + score_b
#
#         if is_deuce(score_a, score_b): # TODO
#             while not game_over_deuce(score_a, score_b):
#                 if serving == 'A':
#                     if random() < prob_a:
#                         score_a += 1
#                     else:
#                         score_b += 1
#                     serving = 'B'
#                 else:
#                     if random() < prob_b:
#                         score_b += 1
#                     else:
#                         score_a += 1
#                     serving = 'A'
#             return score_a, score_b
#
#         if (total_score % 2 == 1) and (total_score > 1):
#             if serving == 'A':
#                 serving = 'B'
#             else:
#                 serving = 'A'
#
#     return score_a, score_b
#
#
# def game_over(a, b):
#     # a and b represent scores for a table tennis game
#     # Returns True if the game is over, False otherwise.
#     return a == 11 or b == 11
#
#
# def game_over_deuce(a, b):
#     return (a >= 11 or b >= 11) and (abs(a - b) >= 2)
#
#
# def is_deuce(a, b):
#     return (a == 10) and (b == 10)
#
#
# def print_summary(wins_a, wins_b):
#     # Prints a summary of wins for each team.
#     n = wins_a + wins_b
#     print('\nGames simulated: {0}'.format(n))
#     print('Wins for A: {0} ({1:0.1%})'.format(wins_a, wins_a / n))
#     print('Wins for B: {0} ({1:0.1%})'.format(wins_b, wins_b / n))
#
#
# if __name__ == '__main__': main()

# 7.
