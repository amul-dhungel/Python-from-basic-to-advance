
# __init__ is like constructor in python
# if you declare parameters in __init__ , then in later code
# classes can take the parameters too like constructors.

class Computer:
    def __init__(self,cpu,ram):
        # assigning of seperate local variables and evaluating
        # with parameters, so that it can be used in other embedded
        # functions with in this class.
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print(self.cpu)
        print(self.ram)

        

obj = Computer("9df","dfk")
obj.config()

# you can also acess the variable defined inside init
# it is nothing but like class 