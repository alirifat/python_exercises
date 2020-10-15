# this one has a bug, if the user enters 'done' before any evaluation statement
# then it throws an error
def eval_loop():
    while True:
        statement = input('Please enter a statement:')
        if statement != 'done':
            result = eval(statement)
            print(result)
        else:
            return result

eval_loop()

# this one bug-free if the user enters 'done' before any statement, then the
# function prompts user to make another entry. If 'done' is entered after any 
# statement then it returns the last evalution result.
# def eval_loop():
#     results = []
#     while True:
#         statement = input('Please enter a statement:')
#         if statement != 'done':
#             results.append(eval(statement))
#             print(results[-1])
#         else:
#             if results:
#                 return results[-1]
#
# eval_loop()
