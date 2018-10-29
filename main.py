import sys
sys.path.append('classes')
sys.path.append('functions')
from robot import Robot
from person import Person
from functions import genre

r1 = Robot(name(), "white", 180)
r1.introduce_self()


p1 = Person(name(), genre())
p1.introduce_self()
