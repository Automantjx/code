# import package 
# __init__.py中 import module
# import package.module

# from package import *
# __init__.py中 from .module import *
# from package.module import *


# self  类的实例化对象
class Animal(object):
    def eat(self, food):
        print(f"eating {food}")
    
    def play(self):
        print(f"playing")
    
    def sleep(self, food):
        self.eat(food)   #
        print(f"sleeping")

dog = Animal()
# dog.play()
Animal.play(dog)

pig = Animal()
pig.sleep("h")

