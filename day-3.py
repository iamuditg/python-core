print("Welcome to the rollercoaster!")
height = int(input("What is your height in sm?"))

if height > 120:
   print("You can ride the rollercoaster")
   age = int(input("what is your age"))
   if age <= 18:
       print("age below 18")
   else:
       print("age above 18")
else:
   print("Sorry, you have to grow taller before you can ride")


number = int(input("Which number do you want change?"))

if number % 2 == 0:
    print("number is even")
elif number % 3 == 0:
    print("number is divisible by 3")
else:
    print("this is odd number")

leapYear = int(input("Enter the year?"))

if leapYear % 4 == 0:
    if leapYear % 100 == 0:
        if leapYear % 400 == 0:
            print("leap year")
        else:
            print("not leap year")
    else:
        print("leap year")
else:
    print("Not leap year")

print("Welcome to python pizza deliveries!")
size = input("What size pizza do you want? S, M, or L")
add_pepperoni = input("Do you want pepperoni? Y or N")
extra_cheese = input("Do you want extra cheese? Y or N")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"You final bill is ${bill}")

print("Logical Operator: ")

print("welcome to the love calculator")
name1 = input("What is your name?")
name2 = input("What is their name?")

combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score > 90):
    print(f"your love score us {love_score}")
elif (love_score >= 40) or (love_score <= 50):
    print(f"your score is {love_score} alright")
else:
    print(f"love end {love_score}")
