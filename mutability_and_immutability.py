a=b=4
b=5
print a # 4
print b # 5

a = [1,2]; b = a; b[0] = 4;
print a # [4, 2]
print b # [4, 2]

# Shallow copy
a = [1,2,3]; b = a[:]; b[0] = 8;
print a
print b

c = [4,5,6]; d = list(c); d[0] = 8;
print c
print d

p = [1,2,[3,4]]; 
q = p[:]; 
q[2][1] = 99
print p
print q