# loops
fruits = ["Apple","Peach","Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")

print()
# Coding Exercise
student_height = [234,324,345,65,123,345,657]
sum = 0
for height in student_height:
    sum += height

print(sum)
num_of_student = 0
for student in student_height:
    num_of_student += 1

print(num_of_student)
print("average:",sum/num_of_student)

# Coding Exercise
student_scores = [23,45,76,25,78,74,47,90]

max = 0
for score in student_scores:
    if max < score:
        max = score

print(max)

# range
for number in range(1,10):
    print(number)

# Coding Exercise
total = 0
for num in range (1,101):
    if num%2 == 0:
        total += num

print(total)


