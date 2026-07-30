# Program to print multiplication table

n = int(input("Enter a number: "))

print("Multiplication table of", n, "is:")

for i in range(1, 11):
    print(n, "x", i, "=", n * i)
