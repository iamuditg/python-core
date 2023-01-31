# Data types
# strings
print("Hello"[0])
# Integer
print(123 + 432)
# Float
print(3.14)
# Boolean
print(True | False)

# Type Error , Type Checking and Type Conversion
# num_char = len(input("What is your name"))
# print(type(num_char))
# print("your name has" + str(num_char) + " characters")

# mathematical operation
print(6/3)
print(2**2)
print(4+2)

# exercise
# height = input("enter your height in m:")
# weight = input("enter your weight in kg:")
# bmi = int(weight) / float(height) ** 2
# bmi_as_int = int(bmi)
# print(bmi_as_int)

# number manipulation and f string in python
print(8/3)
print(round(8/3,2))

score = 0
height = 1.8
isWinning = True
print(f"your score is {score}, your height {height}, you are  winning {isWinning}")

# exercise
print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give ? 10,12, or 15 ?"))
people = int(input("How many people to split the bill?"))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill/people
final_amount = "{:2f}".format(bill_per_person)
print(f"Each person should pay :${final_amount}")

