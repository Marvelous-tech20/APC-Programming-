s = input("Enter a string:")

upper = 0
lower = 0


for ch in s:
    if 'A' <=ch <='z':
        upper +=1
    elif 'a' <=ch <='z':
        lower +=1

        print("Uppercase letters:", upper)
        print("Lowercase letters:", lower)
