with open('input.txt') as f:
    content = f.readlines()

content = [line.strip() for line in content]

print content[22]