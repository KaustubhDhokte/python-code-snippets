word_count = {}
with open("druva_code.py", "r") as f:
    for word in f.read().split():
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

for k, v in word_count.items():
    print k, v