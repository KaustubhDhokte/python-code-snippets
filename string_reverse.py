#Method1:
def reverse(s):
    s2 = ""
    for i in s:
        s2 = i+s2
    return s2

print (reverse('hello'))


#Method2:
def reverse2(s):
    if len(s) == 0:
        return s
    return reverse2(s[1:]) + s[0]

print (reverse2("kamal"))

#Method3:
def reverse3(s):
    return s[::-1]

print (reverse3('reverse3'))


a = reversed('pqr')
print ''.join(reversed('pqr'))


'''
olleh
lamak
3esrever
rqp
'''