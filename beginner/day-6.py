def my_function():
    print("Hello")
    print("Bye")

for steps in range(5):
    my_function()

number_of_steps = 0
while number_of_steps < 5:
    my_function()
    number_of_steps += 1
