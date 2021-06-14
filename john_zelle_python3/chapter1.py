# Chapter 1 Exercises

# Review Questions (True/False)
# 1. False. Computer science is the study of computation. Computer scientists use tools, such as design, analysis and
# experiment to answer the question of "what can be computed?". However, computers are the main object in this process.

# 2. True. CPU (Central Processing Unit) is the brain of the computer. It reads the instructions and does them one by
# one by fetching the required things from the main memory (RAM).

# 3. False. The secondary memory stores the information permanently. However, the main memory RAM (Random Access Memory)
# only keeps the information when a computer works. After it turned on, everything on the RAM will be vanished. On the
# other hand, the secondary memory, which can be a HDD, SDD, USB or a DVD, will keep the information without any damage
# to the data.

# 4. True. CPU access the information from the main memory. Even though, the information are contained on the secondary
# memory, they have to be transferred to the main memory to make them accessible for the CPU.

# 5. False. The syntax of a language, whether it is a human language or a programming language, is consists of the
# rules or the notions on its form. On the other hand, the semantics of a language is its meaning.

# 6. True. A function takes a bunch of statements and call them with a single call. It is possible to run the statements
# without putting them into a function; however, it would require to rewrite each statement again and again to run.
# Thus, a function stores the statements and calls them at once when it is called.

# 7. False. A programming environment is a more general term than an IDE. It consists of IDE and the operating system to
# run the program. Thus, a programming environment is a place whene the program runs, not the programmer.

# 8. True. A variable can be considered as container for a value. It gives the value a name so that we can refer the
# value later by calling the variable.

# 9. False. A loop is used to do a single task repeatedly. It help us to run the taks without calling it expilicitly.

# 10. False. A chaotic function can be computed by the computer but it cannot be predicted.


# Multiple Choice
# 1. B (What can be computed?)
# 2. D (recipe)
# 3. D (it is not practical to solve)
# 4. A (RAM)
# 5. B (high-level computer languages)
# 6. B (a complete computer command)
# 7. C (a compiler is no longer needed after a program is translated)
# 8. B (main)
# 9. A (They make a program more efficient.)
# 10. B (parameters)


# Discussion
# 1. a) Hardware vs. Software
# While the hardware consists of the phycial parts of a computer, the software consists of the programs that rule over
# hardware. Without software, a computer is just a piece of metal that cannot perform any single transaction.
# 1. b) Algorithm vs. Program
# An algorithm is a recipe for a specific problem. It gives the steps to take to solve it. However, a program is a step-
# by-step instruction for the computer to follow. An algorithm can be transformed into a program. Nevertheless, it can
# only solve a specific type of a problem. On the other hand, a program can be changed so that the computer performs a
# different task.
# 1. c) Programming Language vs. Natural Language
# A programming language is meant to communicate with computers. However, natural language is for human interaction.
# Even though natural language can get vague time-to-time, a programming language is always frank to understood by
# humans and computers. If a programming language can be understood and manipulated by humans, then it is called as a
# high-level language.
# 1. d) High-Level Language vs. Machine Language
# High-level languages can be understood by humans; however, machine language consists of bytes and can only be under-
# stood by machines. Besides, high-level languages are portable, they can work any computer which has the right hardware
# and the program to convert it into the machine language. Nevertheless, each computer may have a different machine
# language depending on the hardware configuration.
# 1. e) Interpreter vs. Compiler
# A compiler transforms a high-level language into a machine language. It can be run multiple times without any further
# need of compiling when it is compiled once. On the other hand, interpreter also transforms a high-level language into
# a machine language but it does it simultaneously. In other words, as the language goes each line, the interpreter
# converts that line into machine language. Moreover, interpreter has to interpret a high-level language whenever it is
# executed. Thus, interpreted languages are much slower than compiled languages.
# 1. f) Syntax vs Semantic
# While syntax is the form of a language, the semantic is its meaning.

# 2. * CPU (Central Processing Unit): the brain of the computer. It orchestrates all transactions in the computer.
# * Main Memory (RAM): the place where CPU reads the information. Whenever a transaction is run, the information are
# copied from secondary memory to main memory. Thus, the CPU can access it. However, it is very volatile.
# * Secondary Memory: the place where the information stored permanently. It transfer the information to RAM to make
# it accessible to CPU.
# * Input Devices: the devices that enables user to interact with computer.
# * Output Devices: the devices that displays the result of a transaction to users.

# 3. The pseudo-code for making a peanut butter and jelly sandwich:
# * If you are not near to the refrigerator, go near to it
# * Stand in front of the refrigerator and open its door
# * Find the peanut butter and put it on the countertop
# * Find the jelly and put it on the countertop
# * Find the cutting board and place it on the countertop
# * Relocate the items on the countertop if necessary to work with them comfortably
# * Find the bread and put it on the cutting board
# * Find the knife and cut two slices of bread with finger thickness
# * Find the spreader and take about 15 grams of peanut butter
# * Spread it on one side of the one of the slices
# * Take about 15 grams of jelly
# * Spread it on top of peanut butter
# * Finally, put the slices on top of each other where the spread stays between the layers.

# 4. It would be a problem if we need 100% accuarcy over the results. In such a case, having approximations may not
# be the best interest of the problem-solver.

# 5. Trace through the chaos program with input of 0.15.

def chaos():
    print('This program illustrates a chaotic function.')
    x = eval(input('Enter a number between 0 and 1: '))
    for i in range(10):
        x = 3.9 * x * (1 - x)
        print(x)


chaos()


# Programming Exercises
# 1.a)
print('Hello, world!')

# 1.b)
print('Hello', 'world!')

# 1.c)
print(3)

# 1.d)
print(3.0)

# 1.e)
print(2 + 3)

# 1.f)
print(2.0 + 3.0)

# 1.g)
print('2' + '3')

# 1.h)
print('2 + 3 =', 2 + 3)

# 1.i)
print(2 * 3)

# 1.j)
print(2 ** 3)

# 1.k)
print(7 / 3)

# 1.l)
print(7 // 3)

# 2. Enter and run the chaos program with various values to verify its chaotic behavior
for i in range(3):
    chaos()

# 3. Modify the chaos function and replace the constant of 3.9 with 2.0
def chaos_modified():
    print('This program illustrates a chaotic function.')
    x = eval(input('Enter a number between 0 and 1: '))
    for i in range(10):
        x = 2.0 * x * (1 - x)
        print(x)


for i in range(3):
    chaos_modified()

# The modified version of the chaos function starts to behave deterministically after a few iterations.

# 4. Modify the chaos function to print out 20 values.
def chaos_modified_20():
    print('This function illustrates a chaotic function.')
    x = eval(input('Enter a number between 0 and 1: '))
    for i in range(20):
        x = 3.9 * x * (1 - x)
        print(x)

# 5. Modify the chaos program so that the user decides the number of values to be printed out.
def chaos_modified_user():
    print('This function illustrates a chaotic function.')
    n = eval(input('How many numbers shoud I print? '))
    x = eval(input('Enter a number between 0 and 1: '))
    for i in range(n):
        x = 3.9 * x * (1 - x)
        print(x)

# Perform the chaos function with respect to different equations.
def chaos_modified_eq1():
    print('This function illustrates a chaotic function.')
    x = eval(input('Enter a number between 0 and 1: '))
    for i in range (100):
        x = 3.9 * x * (1 - x)
        print(x)


def chaos_modified_eq2():
    print('This function illustrates a chaotic function.')
    x = eval(input('Enter a number between 0 and 1: '))
    for i in range(100):
        x = 3.9 * x * (x - x * x)
        print(x)


def chaos_modified_eq3():
    print('This function illustrates a chaotic function.')
    x = eval(input('Enter a number between 0 and 1: '))
    for i in range(100):
        x = 3.9 * x - 3.9 * x * x
        print(x)

for i in range(3):
    chaos_modified_eq1()
    chaos_modified_eq2()
    chaos_modified_eq3()

# The second function (x = 3.9 * x - 3.9 * x * x) losts its chaotic behavior. It turns to a deterministic function.

# 7. Modify the chaos function to take two numbers and prints the results as a neat table.
def chaos_modified_2params():
    print('This function illustrates a chaotic function.')
    x = eval(input('Enter a number between 0 and 1 for the first value: '))
    y = eval(input('Enter a number between 0 and 1 for the second value: '))
    print('{:<10}{:^6}\t{:^6}'.format('input', x, y))
    print('-'*30)
    for i in range(10):
        x = 3.9 * x * (1 - x)
        y = 3.9 * y * (1 - y)
        print('{:<10}{:.6f}\t{:.6f}'.format('', x, y))
        

chaos_modified_2params()