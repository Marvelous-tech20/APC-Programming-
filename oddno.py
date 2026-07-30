# Program to print odd numbers up to n

n = int(input("Enter the value of n: "))

print("Odd numbers up to", n, "are:")

for i in range(1, n + 1, 2):
    print(i)
