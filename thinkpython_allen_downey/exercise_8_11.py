def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False

# any_lowercase1 aims to check each character in the string by using a for loop.
# However, it is not the case. It only evaluates the first character in the
# string and returns True if the first character is a lowercase; otherwise
# returns False.
# The function does not work properly

def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

# any_lowercase2 aims to iterate over all characters in the string. However, the
# if condition has not constructed properly. The if condition checks if 'c' is a
# lowercase character and return True if so; otherwise returns False. The problem
# is that 'c' is a lowercase character and the function will return True regarless
# of the input string.
# The function does not work properly.

def any_lowercase3(s):
    for c in s:
        flag = c.islower()
        return flag

# any_lowercase3 aims to iterate all characters in the string. However, it fails
# to do so because of the return statement. The function, as in any_lowercase1,
# only checks if the first character of the string is a lowercase character. If
# so it returns True; otherwise returns False.
# The function does not work properly.

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

# any_lowercase4 works properly and returns True if there is any lowercase in the
# string. It works because of the `or` statement which is always True if one of
# the components is True. If there is any lowercase letter in the string than
# it turns to be True.

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True

# any_lowercase5 aims to iterate through all characters in the string. However, it
# fails to the so because of return statement. It only checks the first character
# in the string and returns True if the first character is a lowercase character.
# Otherwise returns False.
# The function does not work properly.
