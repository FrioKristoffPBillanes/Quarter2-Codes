age = int(input("Hi there! What's your age?\n"))
sum = 0
for i in range(age + 1):
    sum += i
print(f"The sum of all numbers from 1 to {age} is: {sum}")