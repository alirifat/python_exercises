# Chapter 2 Exercises

# Review Questions (True/False)
# 1. False. Writing a program requires a systematic approach with the following steps: problem analysis (defining the
# problem), problem specification (deciding what the program will do), design (writing a pseudocode for the algorithm),
# implementation (writing the program using a programming language), testing/debugging (fixing the errors in the
# program), and maintanence (keeping the program up to date).

# 2. True. An algorithm can be written without using a programming language; however, implementing that algorithm
# will require a programming language.

# 3. False. Programs often require modification or maintenance after they are written; however, there may be some
# programs that may not require any maintanence. Nevertheless, most of the real-world programs will have maintenance
# after they are written and debugged.

# 4. True. Python identifiers cannot start with numbers or symbols other than underscore.

# 5. False. Identifiers cannot be reserved Python keywords, such as True, False, for, while, etc.

# 6. True. Expressions are a part of statement that produce data. Besides, data can be produced by using literals, such
# as numbers, strings, etc., and variables and operators.

# 7. True. It is a legal statement that updates the value of variable `x`.

# 8. False. It allows the input of multiple values; however, it may require special attention. For example, having a
# number and a string simultaneously may not be the best practise. Moreover, it may be vulnerable for security issues.

# 9. True. A counted loop can be structured with using a for loop with a range.

# 10. False. Diamonds represent decision points and rectangles represent statement sequences.


# Multiple Choice
# 1. C (fee setting)
# 2. A (F = 9/5(C) + 32)
# 3. D (specification)
# 4. C (2spam)
# 5. B (statements)
# 6. B (expressions)
# 7. B (program)
# 8. D (a counted loop)
# 9. A (sticky-note)
# 10. D (input)


# Discussion
# 1. The software development process consists of six steps: program analysis, program specification, design,
# implementation, testing/debugging, maintenance.

# 2. The chaos program has steps as follows:
# def chaos():
#     print('This program illustrates a chaotic function.') # output
#     x = eval(input('Enter a number between 0 and 1: ')) # input
#     for i in range(10): # loop
#         x = 3.9 * x * (1 - x) # process
#         print(x) # output

# 2. Identifiers: x, i
# 2. Expressions: eval(input()), 3.9, x, (1 - x), 3.9 * x * (1-x), range(10)

# 3. Definite loop indicates that a statement will be run a definite number of times. For loops is used to run a
# statement repeatedly. A counted loop is a special version of for loop that runs a statement for a specific number of
# times. While counted loop is a subset of for loop, a for loop is a subset of definite loop.

# 4. Show the output from the following fragments:
# a.)
for i in range(5):
    print(i * i)

# b.)
for d in [3, 1, 4, 1, 5]:
    print(d, end=' ')

# c.)
for i in range(4):
    print('Hello')

# d.)
for i in range(5):
    print(i, 2 ** i)

# 5. Writing an algorithm with a programming language is a challenging task which requires checking for syntax and
# semantic errors. However, using a pseudocode will let us focus on the problem rather than technical issues of the
# programming language. Thus, it is a good practice to write a pseudocode before implementation stage.

# 6. It separates the expression that are passed to the print function. The default argument for the sep keyword is
# a single character whitespace.

# 7. It will only prints "start" and "end". The for loop doesn't run since it doesn't have a set of number to follow.


# Programming Exercises
# 1.
def main():
    print('This program converts temperature from Celsius to Fahrenheit.')
    celsius = eval(input('What is the Celsius temperature? '))
    fahrenheit = 9 / 5 * celsius + 32
    print('The temperature is', fahrenheit, 'degrees Fahrenheit.')


main()

# 2.
def main():
    print('This program converts temperature from Celsius to Fahrenheit.')
    celsius = eval(input('What is the Celsius temperature? '))
    fahrenheit = 9 / 5 * celsius + 32
    print('The temperature is', fahrenheit, 'degrees Fahrenheit.')
    input('Press the <Enter> key to quit.')


main()

# 3.
def main():
    print('This program computes the average of three exam scores.')
    score1, score2, score3 = eval(input('Enter three scores separated by a comma i.e (1,2,3): '))
    average = (score1 + score2 + score3) / 3
    print('The average of the scores is:', average)


main()

# 4.
def main():
    print('This program converts temperature from Celsius to Fahrenheit.')

    for i in range(5):
        celsius = eval(input('What is the Celsius temperature? '))
        fahrenheit = 9 / 5 * celsius + 32
        print('The temperature is', fahrenheit, 'degrees Fahrenheit.')
        input('Press the <Enter> key to continue.')


main()

# 5.
def main():
    print('This program display a conversion table for temperature from Celsius to Fahrenheit.')
    print('Celsius', 'Fahrenheit')
    print('-'*20)
    for i in range(1, 11):
        celsius = i * 10
        fahrenheit = 9 / 5 * celsius + 32
        print('\t{}\t{}'.format(celsius, fahrenheit))


main()

# 6.
def main():
    print('This program calculates the future value')
    print('over a given number of years.')

    principal = eval(input('Enter the initial principal: '))
    apr = eval(input('Enter the annual interest rate: '))
    years = eval(input('Enter the number of years: '))

    for i in range(years):
        principal = principal * (1 + apr)

    print('The value in {} years is: {}'.format(years, principal))


main()

# 7.
def main():
    print('This program calculates the future value of a fixed investment')
    print('over a given number of years.')

    fixed_investment = eval(input('Enter the yearly investment amount: '))
    apr = eval(input('Enter the annual interest rate: '))
    years = eval(input('Enter the number of years: '))

    for i in range(years):
        accumulated_investment = fixed_investment * (1 + apr)
        accumulated_investment = accumulated_investment + fixed_investment

    print('The accumulated value in {} years is: {}'.format(years, accumulated_investment))


main()

# 8.
def main():
    print('This program calculates the future value of')
    print('of a 10-year investment.')

    principal = eval(input('Enter the initial principal: '))
    rate = eval(input('Enter the yearly interest rate: '))
    periods = eval(input('Enter the number of compounding periods: '))

    for i in range(10 * periods):
        principal = principal * (1 + rate / periods)

    print('The value in 10 years, compounding {} times, is: {}'.format(periods, principal))


main()

# 9.
def main():
    print('This program converts temperature from Fahrenheit to Celsius.')

    fahrenheit = eval(input('Enter the temperature in Fahrenheit degrees: '))
    celsius = (fahrenheit - 32) * 5 / 9

    print('{} Fahrenheit is {} in Celsius degrees.'.format(fahrenheit, celsius))


main()

# 10.
def main():
    print('This program converts distance in kilometers to miles.')

    kilometers = eval(input('Enter the distance in kilometers: '))
    miles = kilometers * 0.62

    print('{} kilometers is {} in miles.'.format(kilometers, miles))


main()

# 11.
def main():
    print('This program converts fluids in oz to liters.')

    oz = eval(input('Enter the amount of fluids in oz: '))
    liters = oz * 0.0295735

    print('{} oz fluids is {} in liters.'.format(oz, liters))


main()

# 12.
def main():

    print('This program is an interactive calculator.')

    for i in range(100):
        value = eval(input('Enter the expression: '))
        print('The value of the expression is', value)


main()