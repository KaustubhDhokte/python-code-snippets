def check_for_palindrome(i):
    return str(i) == str(i)[::-1]

print check_for_palindrome(121)
print check_for_palindrome(222)
print check_for_palindrome(123)

'''
True
True
False
'''