# Program to find sum of natural numbers up to n

n = int(input("Enter the value of n: "))

sum = 0

for i in range(1, n + 1):
    sum = sum + i

print("Sum of natural numbers up to", n, "is:", sum)
