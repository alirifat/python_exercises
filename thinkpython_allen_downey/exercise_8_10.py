def is_palindrome(string):
    return string == string[::-1]

print(is_palindrome('noon'))
print(is_palindrome('away'))
