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
from random import randrange
from random import choices
from random import choice
from graphics import *
from random import random
from math import *
import time
# 1.
def main():
    print_intro()
    prob_a, prob_b, n = get_inputs()
    wins_a, wins_b = simNGames(n, prob_a, prob_b)
    print_summary(wins_a, wins_b)


def print_intro():
    print("This program simulates a game of racquetball between two")
    print('players called "A" and "B". The ability of each player is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("the player wins the point when serving. Player A always")
    print("has the first serve.")


def get_inputs():
    # Returns the three simulation parameters
    a = float(input("What is the prob. player A wins a serve? "))
    b = float(input("What is the prob. player B wins a serve? "))
    n = int(input("How many games to simulate? "))
    return a, b, n


def simNGames(n, prob_a, prob_b):
    # Simulates n games of racquetball between players whose
    # abilities are represented by the probability of winning a serve.
    # Returns number of wins for A and B
    wins_a = wins_b = 0
    game = 0
    while (wins_a <= n / 2) and (wins_b <= n / 2):
        game = game + 1
        if game % 2 != 0:
            score_a, score_b = simOneGame(prob_a, prob_b, 'A')
        else:
            score_a, score_b = simOneGame(prob_a, prob_b, 'B')

        if score_a > score_b:
            wins_a += 1
        else:
            wins_b += 1

    return wins_a, wins_b


def simOneGame(prob_a, prob_b, serving):
    # Simulates a single game or racquetball between players whose
    # abilities are represented by the probability of winning a serve.
    # Returns final scores for A and B
    score_a = score_b = 0
    while not gameOver(score_a, score_b):
        if serving == "A":
            if random() < prob_a:
                score_a += 1
            else:
                serving = "B"
        else:
            if random() < prob_b:
                score_b += 1
            else:
                serving = 'A'

    return score_a, score_b


def gameOver(a, b):
    # a and b represent scores for a racquetball game
    # Returns True if the game is over, False otherwise.
    return a == 15 or b == 15


def print_summary(wins_a, wins_b):
    # Prints a summary of wins for each player.
    n = wins_a + wins_b
    print("\nGames simulated: ", n)
    print("Wins for A: {0} ({1: 0.1%})".format(wins_a, wins_a / n))
    print("Wins for B: {0} ({1: 0.1%})".format(wins_b, wins_b / n))


if __name__ == '__main__': main()

# 2.
def main():
    print_intro()
    prob_a, prob_b, n = get_inputs()
    wins_a, wins_b, shutout_a, shutout_b = simNGames(n, prob_a, prob_b)
    print_summary(wins_a, wins_b, shutout_a, shutout_b)


def print_intro():
    print("This program simulates a game of racquetball between two")
    print('players called "A" and "B". The ability of each player is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("the player wins the point when serving. Player A has the")
    print("first serve in the odd games of the match, and player B")
    print("serves first in the even games. Moreover, it reports the")
    print("number of shutout and percentage of wins that are shutouts")
    print("for each player.")


def get_inputs():
    # Returns the three simulation parameters
    a = float(input("What is the prob. player A wins a serve? "))
    b = float(input("What is the prob. player B wins a serve? "))
    n = int(input("How many games to simulate? "))
    return a, b, n


def simNGames(n, prob_a, prob_b):
    # Simulates n games of racquetball between players whose
    # abilities are represented by the probability of winning a serve.
    # Returns number of wins for A and B
    wins_a = wins_b = 0
    shutout_a = shutout_b = 0
    game = 0
    while (wins_a <= n / 2) and (wins_b <= n / 2):
        game = game + 1
        if game % 2 != 0:
            score_a, score_b = simOneGame(prob_a, prob_b, 'A')
        else:
            score_a, score_b = simOneGame(prob_a, prob_b, 'B')

        if score_a > score_b:
            wins_a += 1
        else:
            wins_b += 1

        if not score_a:
            shutout_b += 1
        elif not score_b:
            shutout_a += 1

    return wins_a, wins_b, shutout_a, shutout_b


def simOneGame(prob_a, prob_b, serving):
    # Simulates a single game or racquetball between players whose
    # abilities are represented by the probability of winning a serve.
    # Returns final scores for A and B
    score_a = score_b = 0

    while not gameOver(score_a, score_b):
        if serving == "A":
            if random() < prob_a:
                score_a += 1
            else:
                serving = "B"
        else:
            if random() < prob_b:
                score_b += 1
            else:
                serving = 'A'

    return score_a, score_b


def gameOver(a, b):
    # a and b represent scores for a racquetball game
    # Returns True if the game is over, False otherwise.
    return a == 15 or b == 15


def print_summary(wins_a, wins_b, shutout_a, shutout_b):
    # Prints a summary of wins for each player.
    n = wins_a + wins_b
    print("\nGames simulated: ", n)
    print("Wins for A: {0} ({1: 0.1%})".format(wins_a, wins_a / n))
    print("Shutout for A: {0} ({1: 0.1%})".format(shutout_a, shutout_a / wins_a))
    print("Wins for B: {0} ({1: 0.1%})".format(wins_b, wins_b / n))
    print("Shutout for B: {0} ({1: 0.1%})".format(shutout_b, shutout_b / wins_b))


if __name__ == '__main__': main()

# 3.
def main():
    print_intro()
    prob_a, prob_b, n = get_inputs()
    wins_a, wins_b = sim_n_games(n, prob_a, prob_b)
    print_summary(wins_a, wins_b)


def print_intro():
    print('This program simulates a game of volleyball between two')
    print('teams called "A" and "B". The ability of each team is')
    print('indicated by a probability (a number between 0 and 1) that')
    print('the team wins the point when serving. Team A always')
    print('has the first serve.')


def get_inputs():
    # Returns the three simulation parameters
    a = float(input('What is the prob. team A wins a serve? '))
    b = float(input('What is the prob. team B wins a serve? '))
    n = int(input('How many games to simulate? '))
    return a, b, n


def sim_n_games(n, prob_a, prob_b):
    # Simulates n games of volleyball between teams whose
    #   abilities are represented by the probability of winning a serve.
    # Returns number of wins for A and B
    wins_a = wins_b = 0
    for i in range(n):
        score_a, score_b = sim_one_game(prob_a, prob_b)
        if score_a > score_b:
            wins_a += 1
        else:
            wins_b += 1
    return wins_a, wins_b


def sim_one_game(prob_a, prob_b):
    # Simulates a single game of volleyball between teams whose
    #   abilities are represented by the probability of winning a serve.
    # Returns final scores for A and B
    serving = 'A'
    score_a = score_b = 0
    while not game_over(score_a, score_b):
        if serving == 'A':
            if random() < prob_a:
                score_a += 1
            else:
                serving = 'B'
        else:
            if random() < prob_b:
                score_b += 1
            else:
                serving = 'A'
    return score_a, score_b


def game_over(a, b):
    # a and b represent scores for a volleyball game
    # Returns True if the game is over, False otherwise.
    return (a >= 15 or b >= 15) and (abs(a - b) >= 2)


def print_summary(wins_a, wins_b):
    # Prints a summary of wins for each team.
    n = wins_a + wins_b
    print('\nGames simulated: {0}'.format(n))
    print('Wins for A: {0} ({1:0.1%})'.format(wins_a, wins_a / n))
    print('Wins for B: {0} ({1:0.1%})'.format(wins_b, wins_b / n))


if __name__ == '__main__': main()

# 4.
def main():
    print_intro()
    prob_a, prob_b, n = get_inputs()
    wins_a, wins_b = sim_n_games(n, prob_a, prob_b)
    print_summary(wins_a, wins_b)


def print_intro():
    print('This program simulates a game of volleyball between two')
    print('teams called "A" and "B". The ability of each team is')
    print('indicated by a probability (a number between 0 and 1) that')
    print('the team wins based on rally scoring. Team A always')
    print('has the first serve.')


def get_inputs():
    # Returns the three simulation parameters
    a = float(input('What is the prob. team A wins a serve? '))
    b = float(input('What is the prob. team B wins a serve? '))
    n = int(input('How many games to simulate? '))
    return a, b, n


def sim_n_games(n, prob_a, prob_b):
    # Simulates n games of volleyball between teams whose
    #   abilities are represented by the probability of winning a serve.
    # Returns number of wins for A and B
    wins_a = wins_b = 0
    for i in range(n):
        score_a, score_b = sim_one_game(prob_a, prob_b)
        if score_a > score_b:
            wins_a += 1
        else:
            wins_b += 1
    return wins_a, wins_b


def sim_one_game(prob_a, prob_b):
    # Simulates a single game of volleyball between teams whose
    #   abilities are represented by the probability of winning a serve.
    # Returns final scores for A and B
    serving = 'A'
    score_a = score_b = 0
    while not game_over(score_a, score_b):
        if serving == 'A':
            if random() < prob_a:
                score_a += 1
            else:
                score_b += 1
                serving = 'B'
        else:
            if random() < prob_b:
                score_b += 1
            else:
                score_a += 1
                serving = 'A'

    return score_a, score_b


def game_over(a, b):
    # a and b represent scores for a volleyball game
    # Returns True if the game is over, False otherwise.
    return a == 25 or b == 25


def print_summary(wins_a, wins_b):
    # Prints a summary of wins for each team.
    n = wins_a + wins_b
    print('\nGames simulated: {0}'.format(n))
    print('Wins for A: {0} ({1:0.1%})'.format(wins_a, wins_a / n))
    print('Wins for B: {0} ({1:0.1%})'.format(wins_b, wins_b / n))


if __name__ == '__main__': main()

# 5.
def main():
    print_intro()
    prob_a, prob_b, n, m = get_inputs()
    rally_advantage, regular_advantage = compare_rally_vs_regular(n, prob_a, prob_b)
    print_summary(n, rally_advantage, regular_advantage)


def print_intro():
    print('This program simulates a game of volleyball between two')
    print('teams called "A" and "B". The ability of each team is')
    print('indicated by a probability (a number between 0 and 1). The')
    print('program investigates whether rally scoring magnifies, reduces,')
    print('or has no effect on the relative advantage enjoyed by the')
    print('better team when compared with regular volleyball. Team A')
    print('always has the first serve.')


def get_inputs():
    # Returns the three simulation parameters
    a = float(input('What is the prob. team A wins a serve? '))
    b = float(input('What is the prob. team B wins a serve? '))
    n = int(input('How many times to simulate? '))
    m = int(input('How may games per simulation? '))
    return a, b, n, m


def compare_rally_vs_regular(n, prob_a, prob_b):
    rally_advantage = 0
    regular_advantage = 0
    for i in range(n):
        rally_wins_a, rally_wins_b, regular_wins_a, regular_wins_b = sim_m_games(n, prob_a, prob_b)
        if prob_a > prob_b:
            if rally_wins_a > rally_wins_b:
                rally_advantage += 1
            elif regular_wins_a >= regular_wins_b:
                regular_advantage += 1
        else:
            if rally_wins_b > rally_wins_a:
                rally_advantage += 1
            elif regular_wins_b >= regular_wins_b:
                regular_advantage += 1

    return rally_advantage, regular_advantage


def sim_m_games(m, prob_a, prob_b):
    # Simulates n games of volleyball between teams whose
    #   abilities are represented by the probability of winning a serve.
    # Returns number of wins for A and B
    rally_wins_a = rally_wins_b = 0
    regular_wins_a = regular_wins_b = 0
    for i in range(m):
        rally_score_a, rally_score_b = sim_one_game_rally(prob_a, prob_b)
        regular_score_a, regular_score_b = sim_one_game_regular(prob_a, prob_b)

        if rally_score_a > rally_score_b:
            rally_wins_a += 1
        else:
            rally_wins_b += 1

        if regular_score_a > regular_score_b:
            regular_wins_a += 1
        else:
            regular_wins_b += 1

    return rally_wins_a, rally_wins_b, regular_wins_a, regular_wins_b


def sim_one_game_rally(prob_a, prob_b):
    # Simulates a single game of rally volleyball between teams whose
    #   abilities are represented by the probability of winning a serve.
    # Returns final scores for A and B
    serving = 'A'
    score_a = score_b = 0
    while not game_over_rally(score_a, score_b):
        if serving == 'A':
            if random() < prob_a:
                score_a += 1
            else:
                score_b += 1
                serving = 'B'
        else:
            if random() < prob_b:
                score_b += 1
            else:
                score_a += 1
                serving = 'A'

    return score_a, score_b


def sim_one_game_regular(prob_a, prob_b):
    # Simulates a single game of regular volleyball between teams whose
    #   abilities are represented by the probability of winning a serve.
    # Returns final scores for A and B
    serving = 'A'
    score_a = score_b = 0
    while not game_over_regular(score_a, score_b):
        if serving == 'A':
            if random() < prob_a:
                score_a += 1
            else:
                serving = 'B'
        else:
            if random() < prob_b:
                score_b += 1
            else:
                serving = 'A'

    return score_a, score_b


def game_over_rally(a, b):
    # a and b represent scores for a volleyball game
    # Returns True if the game is over, False otherwise.
    return a == 25 or b == 25


def game_over_regular(a, b):
    # a and b represent scores for a volleyball game
    # Returns True if the game is over, False otherwise.
    return (a >= 15 or b >= 15) and (abs(a - b) >= 2)


def print_summary(n, rally_advantage, regular_advantage):
    # Prints a summary of wins for each team.
    print('\nTimes simulated: {0}'.format(n))
    print('Wins for better team (rally scoring): {}'.format(rally_advantage))
    print('Wins for better team (regular scoring): {}'.format(regular_advantage))


if __name__ == '__main__': main()

# 6.
def main():
    print_intro()
    prob_a, prob_b, n = get_inputs()
    wins_a, wins_b = sim_n_games(n, prob_a, prob_b)
    print_summary(wins_a, wins_b)


def print_intro():
    print('This program simulates a game of table tennis between two')
    print('players called "A" and "B". The ability of each player is')
    print('indicated by a probability (a number between 0 and 1). Team A')
    print('always has the first serve. The winner is decided by the best')
    print('of n games. A player can win points, even he/she was not the')
    print('serving player. (https://www.teamusa.org/usa-table-tennis/rules)')


def get_inputs():
    # Returns the three simulation parameters
    a = float(input('What is the prob. team A wins a serve? '))
    b = float(input('What is the prob. team B wins a serve? '))
    n = int(input('How many games to simulate? '))
    return a, b, n


def sim_n_games(n, prob_a, prob_b):
    # Simulates n games of table tennis between teams whose
    #   abilities are represented by the probability of winning a serve.
    # Returns number of wins for A and B
    wins_a = wins_b = 0
    while (wins_a <= n / 2) and (wins_b <= n / 2):
        score_a, score_b = sim_one_game(prob_a, prob_b)
        if score_a > score_b:
            wins_a += 1
        else:
            wins_b += 1
    return wins_a, wins_b


def sim_one_game(prob_a, prob_b):
    # Simulates a single game of table tennis between teams whose
    #   abilities are represented by the probability of winning a serve.
    # Returns final scores for A and B
    serving = 'A'
    score_a = score_b = 0
    while not game_over(score_a, score_b):
        if serving == 'A':
            if random() < prob_a:
                score_a += 1
            else:
                score_b += 1
        else:
            if random() < prob_b:
                score_b += 1
            else:
                score_a += 1

        total_score = score_a + score_b

        if is_deuce(score_a, score_b):
            while not game_over_deuce(score_a, score_b):
                if serving == 'A':
                    if random() < prob_a:
                        score_a += 1
                    else:
                        score_b += 1
                    serving = 'B'
                else:
                    if random() < prob_b:
                        score_b += 1
                    else:
                        score_a += 1
                    serving = 'A'
            return score_a, score_b

        if (total_score % 2 == 1) and (total_score > 1):
            if serving == 'A':
                serving = 'B'
            else:
                serving = 'A'

    return score_a, score_b


def game_over(a, b):
    # a and b represent scores for a table tennis game
    # Returns True if the game is over, False otherwise.
    return a == 11 or b == 11


def game_over_deuce(a, b):
    return (a >= 11 or b >= 11) and (abs(a - b) >= 2)


def is_deuce(a, b):
    return (a == 10) and (b == 10)


def print_summary(wins_a, wins_b):
    # Prints a summary of wins for each team.
    n = wins_a + wins_b
    print('\nGames simulated: {0}'.format(n))
    print('Wins for A: {0} ({1:0.1%})'.format(wins_a, wins_a / n))
    print('Wins for B: {0} ({1:0.1%})'.format(wins_b, wins_b / n))


if __name__ == '__main__': main()

# 7.
def main():
    print_intro()
    n = get_input()
    wins = simulate_n_games(n)
    print_summary(wins, n)


def print_intro():
    print('This program simulates a game of craps. A player rolls a pair')
    print('of normal six-sided dice.  If the initial roll is 2, 3, or 12,')
    print('the player loses. If the roll is 7 or 11, the player wins. Any')
    print('other initial roll causes the player to "roll for point." That')
    print('is, the player keeps rolling the dice until either rolling a 7')
    print('or re-rolling the value of the initial roll. If the player re-')
    print("rolls the initial value before rolling a 7, it's a win. Rolling")
    print('a 7 first is a loss.')


def get_input():
    n = int(input('Please! Enter the number of games to simulate: '))
    return n


def simulate_n_games(n):
    wins = 0
    for i in range(n):
        initial_roll = roll()
        if is_win(initial_roll):
            wins += 1
        elif is_roll_for_point(initial_roll):
            while True:
                consecutive_roll = roll()
                if consecutive_roll == 7:
                    break
                if consecutive_roll == initial_roll:
                    wins += 1
                    break
        else:
            continue

    return wins


def roll():
    return randrange(2, 12)


def is_win(initial_roll):
    return (initial_roll == 7) or (initial_roll == 11)


def is_roll_for_point(initial_roll):
    if initial_roll not in [2, 3, 7, 11, 12]:
        return True
    return False


def print_summary(wins, n):
    print('The player won {0} games out of {1} with a percentage of {2:0.1%}.'.format(wins, n, wins / n))


if __name__ == '__main__':
    main()

# 8.
def main():
    print_intro()
    n = get_inputs()
    dealer_busted = simulate_n_games(n)
    print_summary(dealer_busted, n)


def print_intro():
    print('This program simulates a game of blackjack. The goal of the')
    print('game is to draw cards that total as close to 21 points as')
    print('possible without going over. All face cards count as 10 points,')
    print('aces count as 1 or 11, and all other cards count their numeric')
    print('value. The game is played against a dealer. The player tries to')
    print('get closer to 21 (without going over) than the dealer. If the')
    print('dealer busts (goes over 21), the player automatically wins')
    print('(provided the player had not already busted).')


def get_inputs():
    n = int(input('\nPlease! Enter the number of games to simulate: '))
    return n


def simulate_n_games(n):
    busted = 0
    for i in range(n):
        hand = 0

        while hand < 17:
            card = get_card()

            if card < 10:
                hand += card
            else:
                hand += 10

            if (17 <= hand + 10 <= 21) and has_ace(card):
                hand += 10

            if hand > 21:
                busted += 1
                break

    return busted


def get_card():
    return randrange(1, 14)


def has_ace(card):
    return card == 1


def print_summary(busted, n):
    print('\nThe dealer is busted {0} times out of {1} with a {2:0.1%}.'.format(busted, n, busted / n))


if __name__ == '__main__':
    main()

# 9.
def main():
    print_intro()
    n, starting_value = get_inputs()
    dealer_busted = simulate_n_games(n, starting_value)
    print_summary(dealer_busted, n)


def print_intro():
    print('This program simulates a game of blackjack. The goal of the')
    print('game is to draw cards that total as close to 21 points as')
    print('possible without going over. All face cards count as 10 points,')
    print('aces count as 1 or 11, and all other cards count their numeric')
    print('value. The game is played against a dealer. The player tries to')
    print('get closer to 21 (without going over) than the dealer. If the')
    print('dealer busts (goes over 21), the player automatically wins')
    print('(provided the player had not already busted).')


def get_inputs():
    n = int(input('\nPlease! Enter the number of games to simulate: '))
    starting_value = int(input('Please! Enter the a starting value (1-10, inclusive): '))
    return n, starting_value


def simulate_n_games(n, starting_value):
    busted = 0
    for i in range(n):
        if bust_single_game(starting_value):
            busted += 1
    return busted


def bust_single_game(starting_value):
    hand = 0
    hand += starting_value

    while hand < 17:
        card = get_card()

        if card < 10:
            hand += card
        else:
            hand += 10

        if (17 <= hand + 10 <= 21) and (has_ace(card) or has_ace(starting_value)):
            hand += 10

        if hand > 21:
            return True
    return False


def get_card():
    return randrange(1, 14)


def has_ace(card):
    return card == 1


def print_summary(busted, n):
    print('\nThe dealer is busted {0} times out of {1} with a {2:0.1%}.'.format(busted, n, busted / n))


if __name__ == '__main__':
    main()

# 10.
def main():
    print_intro()
    number_of_darts = get_input()
    h = get_parameters(number_of_darts)
    pi = calculate_pi(h, number_of_darts)
    print_summary(pi)


def print_intro():
    print('This program calculates the approximate value of')
    print('using Monte Carlo simulation and a 2x2 square. The')
    print('square has an inscribed circle. The pi value is')
    print('calculated by the formula 4 * (h / n) where h is')
    print('the number of hits to the inscribed circle and n')
    print('is the number of hits to the corners of the square,')
    print('the areas not covered by the circle.')


def get_input():
    n = int(input('\nPlease! Enter the number of darts for simulation: '))
    return n


def get_parameters(number_of_darts):
    h = 0
    for i in range(number_of_darts):
        x_coordinate = 2 * random() - 1
        y_coordinate = 2 * random() - 1

        if (x_coordinate ** 2 + y_coordinate ** 2) <= 1:
            h += 1

    return h


def calculate_pi(h, number_of_darts):
    return 4 * (h / number_of_darts)


def print_summary(pi):
    print('The approximate value of pi is {0:0.2f}.'.format(pi))


if __name__ == '__main__':
    main()

# 11.
def main():
    print_intro()
    n = get_input()
    wins = roll_dices_n_times(n)
    print_summary(wins, n)


def print_intro():
    print('This program performs a simulation to estimate the')
    print('probability of rolling five of a kind in a single')
    print('roll of five six-sided dice.')


def get_input():
    n = int(input('\nPlease! Enter the number of times to roll the dice: '))
    return n


def roll_dices_n_times(n):
    wins = 0
    for i in range(n):
        rolls = roll_all_dices()
        if is_all_same_kind(rolls):
            wins += 1

    return wins


def roll_all_dices():
    t = [1, 2, 3, 4, 5, 6]
    return choices(t, k=5)


def is_all_same_kind(rolls):
    return rolls[0] == rolls[1] == rolls[2] == rolls[3] == rolls[4]


def print_summary(wins, n):
    print('\nThe probability of rolling five of a kind in a single')
    print('roll ({0} times - all of a kind) with {1:,} trials is {2:0.1%}.'.format(wins, n, wins / n))


if __name__ == '__main__':
    main()

# 12.
def main():
    print_intro()
    n = get_input()
    forward, backward = simulate_random_walk(n)
    print_summary(forward, backward)


def print_intro():
    print('This program simulate a random walk of n steps.')


def get_input():
    n = int(input('\nPlease! Enter the number of steps to take: '))
    return n


def simulate_random_walk(n):
    forward = backward = 0
    for i in range(n):
        toss = flip_coin()
        if toss == 'head':
            forward += 1
        else:
            backward += 1
    return forward, backward


def flip_coin():
    toss = choice(['head', 'tail'])
    return toss


def print_summary(forward, backward):
    if forward > backward:
        print('You are {0} steps forward than the starting point.'.format(forward-backward))
    elif backward > forward:
        print('You are {0} steps backward than the starting point.'.format(backward-forward))
    else:
        print('You are at the starting point.')


if __name__ == '__main__':
    main()

# 13.
def main():
    print_intro()
    n = get_input()
    north, east = simulate_random_walk(n)
    print_summary(north, east)


def print_intro():
    print('This program simulates a random walk. In each step,')
    print('it randomly walk one block either north, south, east,')
    print('or west. Finally, it tells the final position relative')
    print('to the starting position.')


def get_input():
    n = int(input('\nPlease! Enter the number of steps to take: '))
    return n


def simulate_random_walk(n):
    north = east = 0
    for i in range(n):
        direction = get_direction()
        if direction == 'north':
            north += 1
        elif direction == 'east':
            east += 1
        elif direction == 'south':
            north -= 1
        else:
            east -= 1
    return north, east


def get_direction():
    t = ['north', 'east', 'south', 'west']
    return choice(t)


def print_summary(north, east):
    if north > 0:
        if east > 0:
            print('\nYou are {0} steps north and {1} steps east of the starting point.'.format(north, east))
        else:
            print('\nYou are {0} steps north and {1} steps west of the starting point.'.format(north, abs(east)))
    elif north < 0:
        if east > 0:
            print('\nYou are {0} steps south and {1} steps east of the starting point.'.format(abs(north), east))
        if east < 0:
            print('\nYou are {0} steps south and {1} steps west of the starting point.'.format(abs(north), abs(east)))
    elif north == 0 and east == 0:
        print('\nYou are at the starting point.')


if __name__ == '__main__':
    main()

# 14.
def main():
    simulate_random_walk()


def simulate_random_walk():
    width = 640
    height = 480
    coordinates = [-100, -100, 100, 100]
    win = generate_canvas(width, height, coordinates)

    # draw start button
    start_location = [-100, -100, -80, -90]
    text = 'Start!'
    start_button, start_text = draw_button(win, start_location, text)
    # draw welcome message
    welcome_location = [-60, -10, 60, 10]
    text = 'This program simulates random walk on 2D.'
    welcome_background, welcome_text = draw_button(win, welcome_location, text)
    # handle clicks and keyboard entries
    while True:
        key = win.checkKey()
        if key == 'Escape':
            win.close()
            return

        click = win.checkMouse()
        if click:
            if is_button(click, start_location):
                remove_objects([start_button, start_text, welcome_background, welcome_text])
                break

    # draw welcome box
    location = [-55, -10, 50, 10]
    text = 'Enter the number of steps: '
    background, welcome_text = draw_button(win, location, text, text_location='left_aligned')
    # draw entry box
    entry = Entry(Point(20, 0), 7)
    entry.setText(1000)
    entry.draw(win)
    # draw confirmation box
    ok_button_location = [35, -5, 45, 5]
    text = 'OK'
    ok_button, ok_text = draw_button(win, ok_button_location, text)

    # handle clicks and keyboard entries
    while True:
        key = win.checkKey()
        if key == 'Escape':
            win.close()
            return

        click = win.checkMouse()
        if click:
            if is_button(click, ok_button_location):
                remove_objects([background, welcome_text, ok_button, ok_text, entry])
                break

    n = int(entry.getText())

    current_position = Point(0, 0)
    for i in range(n):
        new_position = simulate_one_step(current_position)
        draw_line(current_position, new_position, win)
        current_position = new_position
        time.sleep(0.1)

    win.getMouse()


def generate_canvas(width, height, coordinates):
    title = 'Random Walk!'
    x1, y1, x2, y2 = unpack_coordinates(coordinates)
    win = GraphWin(title, width, height)
    win.setCoords(x1, y1, x2, y2)
    return win


def unpack_coordinates(coordinates):
    x1, y1, x2, y2 = coordinates[0], coordinates[1], coordinates[2], coordinates[3]
    return x1, y1, x2, y2


def draw_button(win, location, text, text_location='center'):
    x1, y1, x2, y2 = unpack_coordinates(location)

    # set button rectangle and background color
    button = Rectangle(Point(x1, y1), Point(x2, y2))
    button.setFill('gray')
    button.draw(win)

    # set text to display
    if text_location == 'center':
        p = Point((x1 + x2) / 2, (y1 + y2) / 2)
    elif text_location == 'left_aligned':
        p = Point(x1 * 2 / 3 + x2 * 1 / 3, (y1 + y2) / 2)
    message = Text(p, text)
    message.setTextColor('white')
    message.draw(win)

    return button, message


def is_button(click, location):
    x, y = click.getX(), click.getY()
    x1, y1, x2, y2 = unpack_coordinates(location)

    if (x1 <= x <= x2) and (y1 <= y <= y2):
        return True
    return False


def remove_objects(t):
    for item in t:
        item.undraw()


def is_start(p):
    x, y = p.getX(), p.getY()
    if (-100 <= x <= -80) and (-100 <= y <= -90):
        return True
    return False


def is_ok(p):
    x, y = p.getX(), p.getY()
    if (55 <= x <= 65) and (-5 <= y <= 5):
        return True
    return False


def simulate_one_step(p):
    x = p.getX()
    y = p.getY()

    angle = random() * 2 * pi

    x = x + cos(angle) * 5
    y = y + sin(angle) * 5

    return Point(x, y)


def draw_line(p1, p2, win):
    line = Line(p1, p2)
    line.setArrow('last')
    line.draw(win)


if __name__ == '__main__':
    main()

# 15.
# the question is done based on the answer here:
# (https://math.stackexchange.com/questions/1066981/standing-at-the-center-of-a-cube-and-walking-halfway-to-a-wall-field-of-vision)
def main():
    print_intro()
    n = get_inputs()
    probability = calculate_vision_fraction(n)
    print_summary(probability)

def print_intro():
    print('Suppose you are located at the exact center of a cube.')
    print('If you could look all around you in every direction, each')
    print('wall of the cube would occupy 1/6 of your field of vision.')
    print('Suppose you move toward one of the walls so that you are')
    print('now halfway between it and the center of the cube. What')
    print('fraction of your field of vision is now taken up by the')
    print('closest wall?')


def get_inputs():
    n = int(input('Enter the number of simulations: '))
    return n

def calculate_vision_fraction(n):
    hits = 0
    for i in range(n):
        u = random()
        v = random()
        w = random()

        if (u > 0) and (abs(v) <= 2 * u) and (abs(w) <= 2 * u):
            hits += 1

    return hits / n


def print_summary(prob):
    print('The wall takes up {0:0.1%} of your field of vision.'.format(prob))


if __name__ == '__main__':
    main()

