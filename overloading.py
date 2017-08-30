# https://stackoverflow.com/questions/10202938/how-do-i-use-method-overloading-in-python
class Animal(object):
    def __init__(self):
        print("Animal init!\n")
    def run(self):
        print("Animal running!\n")
    def run(self, walk):
        print("Animal run with walk!\n")
    def run(self, walk, arg):
        print("Animal multiparam run!\n")

a = Animal()
#a.run()  # TypeError: run() takes exactly 3 arguments (1 given)
#a.run(True) # TypeError: run() takes exactly 3 arguments (2 given)
a.run(1, 'g')

