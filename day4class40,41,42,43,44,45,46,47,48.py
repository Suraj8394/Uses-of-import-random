#class=41

import random
random_integer=random.randint(1,10)
print(random_integer)

random_float =random.random()*5
print(random_float)

love_score=random.randint(1,100)
print(f"Your Love Score is {love_score}")


#class=42

import random

random_side = random.randint(0, 1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")


#class=43

states_of_India = ["uttar pardesh", "Punjab", "goa", "Gujarat", "tamilnadu"]
states_of_India[4]="kerla"
states_of_India.append("himachal pardesh")
states_of_India.extend(["mumbai","hydeabad","sikkim "])
print(states_of_India)


#class=44

import random

name=["Suraj", "Shivam", "Rahul", "Madhav", "Ayush", "Parth", "Vansh", "Sujal", "Sushil"]
random_name=random.randint(0,len(name))
x=name[random_name]
print(f"{x} is going to buy today meal today!")

#or

import random

name_string=input("Give me everybody's name, seperated by a comma. ")
names=name_string.split(", ")
random_names=random.randint(0,len(names))
y=names[random_names]
print(f"{y} is going to buy today meal today!")


#class=45

fruits = ["apple", "cherry", "graphes", "mango"]
vegetable=["spinach", "tamato", "patato", "kale"]
dirty_dozen=[fruits, vegetable]
print(dirty_dozen)


#class=46