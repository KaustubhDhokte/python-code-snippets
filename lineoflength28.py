with open('input.txt') as f:
    content = f.readlines()

content = [line.strip() for line in content]

for line in content:
    if len(line) == 28:
        print line
        break;
