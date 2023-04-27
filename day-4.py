import random

random_integer = random.randint(1,10)
print(random_integer)

random_float = random.random() * 5
print(random_float)

love_score = random.randint(1,100)
print(f"your love score is {love_score}")

state_of_america = ["delaware", "pennsylvania", "New Jersey"]
print(state_of_america[0])
state_of_america[1] = "penchivilnaaa"
print(state_of_america)
state_of_america.append("Angelivia")
print(state_of_america)

name_string = input("Give some name")
names = name_string.split(",")
print(names)
print(f"first name is {names[0]}")

first = ["organe", "forge"]
second = ["first","second"]

third = [first,second]
print(third)

