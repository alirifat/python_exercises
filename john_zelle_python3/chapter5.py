# Chapter 5 Exercises

# Review Questions (True/False)
# 1. False. It can be enclosed by singe and double quotes.

# 2. True.

# 3. False. Files are treated as string and can contains multi-lines.

# 4. True.

# 5. True.

# 6. True.

# 7. True.

# 8. False. It is a very weak form of encryption.

# 9. False. It is append method.

# 10. False. It is called 'opening' the file.


# Multiple Choice
# 1. D (indexing)
# 2. C (s[:len(s)-1])
# 3. A (ord)
# 4. C (str)
# 5. C (Unicode)
# 6. D (upper)
# 7. D ({})
# 8. C (readall)
# 9. C (batch)
# 10. A (open)


# Discussion
s1 = 'spam'
s2 = 'ni!'
# 1. a)
print('The Knights who say, ' + s2)
# 1. b)
print(3 * s1 + 2 * s2)
# 1. c)
print(s1[1])
# 1. d)
print(s1[1:3])
# 1. e)
print(s1[2] + s2[:2])
# 1. f)
print(s1 + s2[-1])
# 1. g)
print(s1.upper())
# 1. h)
print(s2.upper().ljust(4) * 3)

# 2. a)
print(s1.upper()[:2])
# 2. b)
print('{1}{0}{1}'.format(s1, s2))
# 2. c)
print('{0}  {0}  {0}'.format(s1.title().ljust(5) + s2.title()))
# 2. d)
print(s1.lower())
# 2. e)
print(s1.split('a'))
# 2. f)
print(s1[:2] + s1[-1])

# 3. a)
for ch in 'aardvark':
    print(ch)
# 3. b)
for w in 'Now is the winter of our discontent...'.split():
    print(w)
# 3. c)
for w in 'Mississippi'.split('i'):
    print(w, end=' ')
# 3. d)
msg = ''
for s in 'secret'.split('e'):
    msg = msg + s
print(msg)
# 3. e)
msg = ''
for ch in 'secret':
    msg = msg + chr(ord(ch) + 1)
print(msg)

# 4. a)
print('Looks like {1} and {0} for breakfast'.format('eggs', 'spam'))
# 4. b)
print('There is {0} {1} {2} {3}'.format(1, 'spam', 4, 'you'))
# 4. c)
print('Hello {0}'.format('Susan', 'Computewell'))
# 4. d)
print('{0:0.2f} {0:0.2f}'.format(2.3, 2.3468))
# 4. e) This is an not a legal string operation. It should use ':' instead of '.'. Since using '.' let Python think
# the value as an index value and throws an IndexError.
# print('{7.5f} {7.5f}'.format(2.3, 2.3468))
# 4. f)
print('Time left {0:02}:{1:05.2f}'.format(1, 37.374))
# 4. g) It throws an IndexError since there is only one string inside the format method. The indexing starts from 0;
# thus, it doesn't have any item with index of 1.
# print('{1:3}'.format('14'))

# 5.


# Programming Exercises
# 1.
def main():
    # get the date
    dateStr = input("Enter a date (mm/dd/yyyy) : ")

    # split into components
    monthStr, dayStr, yearStr = dateStr.split("/")

    # convert monthStr to the month name
    months = ["January", "February", "March", "April",
              "May", "June ", "July", "August ",
              "September", "October", "November", "December"]
    monthStr = months[int(monthStr) - 1]

    # output result in month day , year format
    print('The converted date is {} {}, {}'.format(monthStr, dayStr, yearStr))


main()

# 2.
def main():
    point_grade = int(input('Enter the point grade (0-5): '))

    grades = ['F', 'F', 'D', 'C', 'B', 'A']

    print('The corresponding grade of {} is {}.'.format(point_grade, grades[point_grade]))


main()

# 3.
def main():
    exam_score = int(input('Please enter the exam score: '))

    grade_table = ['F'] * 60 + ['D'] * 10 + ['C'] * 10 + ['B'] * 10 + ['A'] * 10

    print('The grade for the exam score {} is {}'.format(exam_score, grade_table[exam_score]))


main()

# 4.
def main():

    word_to_abbreviate = input('Please enter the phrase: ')

    abbreviation = ''
    for word in word_to_abbreviate.split():
        abbreviation += word[0].upper()

    print('The abbreviation for {} is {}'.format(word_to_abbreviate, abbreviation))


main()

# 5.
def main():

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    name = input('Please enter the name: ')

    numeric_value = 0
    for chr in name.lower():
        numeric_value += alphabet.find(chr) + 1

    print('The numeric value of {} is {}.'.format(word, numeric_value))


main()

# 6.
def main():

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    name = input('Please enter the full name: ')

    numeric_value = 0
    for char in name.replace(' ', '').lower():
        numeric_value += alphabet.find(char) + 1

    print('The numeric value of {} is {}.'.format(name, numeric_value))


main()

# 7.
def main():
    message = input('Please enter the message: ')
    key = int(input('Please enter the key for cipher: '))

    cipher = ''
    for char in message:
        cipher += chr(ord(char) + key)

    print(cipher)


main()

# 8.
def main():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    message = input('Please enter the message: ')
    key = int(input('Please enter the key: '))

    cipher = ''
    for word in message.split():
        for char in word:
            index = alphabet.find(char.lower())
            new_index = (index + key) % 26
            cipher += alphabet[new_index]
        cipher += ' '

    print(cipher)


main()

# 9.
def main():
    text = input('Please enter a sentence: ')

    n = len(text.split())

    print('The number of words is {}.'.format(n))


main()

# 10.
def main():
    text = input('Please enter a sentence: ')

    n = len(text.split())

    word_length = 0
    for word in text.split():
        word_length += len(word)

    average_word_length = word_length / n

    print('The average word length is {}.'.format(average_word_length))


main()

# 11.
def main():
    values = input('Enter two values separated by a comma (i.e. 0.1, 0.2): ').split(',')
    n = int(input('Please enter the number of iterations: '))

    x, y = float(values[0]), float(values[1])

    print('{} {:^8}     {:^8}'.format('index', x, y))
    print('-' * 27)

    for i in range(n):
        x = 3.9 * x * (1 - x)
        y = 3.9 * y * (1 - y)

        print('{:^5} {:^0.6f}     {:^0.6f}'.format(i + 1, x, y))


main()

# 12.
def main():
    investment = float(input('Please enter the amount of investment: '))
    apr = float(input('Please enter the annual interest rate: '))
    years = int(input('Please enter the number of years: '))

    print('{}   {:^8}'.format('Year', 'Value'))
    print('-' * 15)

    for i in range(years):
        print('{:^4}   ${:0.2f}'.format(i, investment))
        investment = investment * (1 + apr)


main()

# 13.
def main():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    infileName = input('What file are the names in? ')
    outfileName = input('What file should the usernames go in? ')

    infile = open(infileName, 'r')
    outfile = open(outfileName, 'w')

    for line in infile:
        total = 0
        name = ''.join(line.lower().split())
        for letter in name:
            total += alphabet.find(letter) + 1
            print('Numeric value of {} is {}'.format(line.strip(), total), file=outfile)

    infile.close()
    outfile.close()


main()

# 14.
def main():
    infileName = input('Please enter the file name: ')

    infile = open(infileName, 'r')

    number_of_lines = 0
    number_of_words = 0
    number_of_letters = 0
    for line in infile:
        number_of_lines += 1
        number_of_words += len(line.split())
        number_of_letters += len(''.join(line.split()))

    print("""
    Number of lines: {}
    Number of words: {}
    Number of letters: {}
    """.format(number_of_lines, number_of_words, number_of_letters))

    infile.close()


main()

# 15.
from graphics import *
def main():
    infileName = input('Please enter the file name: ')
    infile = open(infileName, 'r')

    number_of_students = int(infile.readline().strip())

    # generate the canvas
    height = (number_of_students + 1) * 50
    win = GraphWin('Student Scores', 640, height)
    win.setCoords(-2, number_of_students + 1, 11, 0)
    win.setBackground("white")

    i = 0
    for line in infile:
        name_and_score = line.split()
        name, score = name_and_score[0], int(name_and_score[1])
        Text(Point(-0.5, (i + 1)), '{}'.format(name)).draw(win)
        bar = Rectangle(Point(1, i + 1 + 0.2), Point(score/10, i + 1 - 0.2))
        bar.draw(win)
        i += 1

    win.getMouse()
    infile.close()

main()
        
# 16.
def main():
    infileName = input('Please enter the file name: ')

    infile = open(infileName, 'r')

    scores = []
    for line in infile:
        score = int(line.strip())
        scores.append(score)

    counts = []
    for i in range(11):
        count = scores.count(i)
        counts.append(count)

    max_height = max(counts)

    win = GraphWin('Score Histogram', '640', (max_height + 1) * 50)
    win.setBackground('white')
    win.setCoords(-2, 0, 12, max_height + 1)

    for i in range(11):
        Text(Point(i, 0.5), '{}'.format(i)).draw(win)
        bar = Rectangle(Point(i - 0.2, 1), Point(i + 0.2, counts[i] + 1))
        bar.draw(win)

    win.getMouse()
    infile.close()


main()