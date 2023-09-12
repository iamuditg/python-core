import math


def greet():
    print("Hello")
    print("how do yo do?")
    print("Isnt the weather nice today?")


greet()


# function that allow for input
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Udit")



# exercise
test_h = int(input("Height of Wall:"))
test_w = int(input("Width of wall:"))
coverage = 5

def paint_calc(height,width,cover):
    area = height * width
    num_of_cans = math.ceil(area / cover)
    print(f"{num_of_cans}")

paint_calc(test_h,test_w,coverage)