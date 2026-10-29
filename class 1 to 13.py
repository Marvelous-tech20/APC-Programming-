```python
# 1. Student Class

class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def percentage(self):
        return sum(self.marks) / len(self.marks)

    def display(self):
        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Percentage:", self.percentage(), "%")
        print()


students = [
    Student(1, "Rahul", [80, 75, 90, 85, 88]),
    Student(2, "Priya", [92, 89, 95, 90, 94]),
    Student(3, "Amit", [70, 78, 75, 80, 72])
]

for student in students:
    student.display()


# 2. Employee Class

class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

    def calculate_hra(self):
        return self.basic_salary * 0.20

    def calculate_da(self):
        return self.basic_salary * 0.10

    def gross_salary(self):
        return self.basic_salary + self.calculate_hra() + self.calculate_da()

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Basic Salary:", self.basic_salary)
        print("HRA:", self.calculate_hra())
        print("DA:", self.calculate_da())
        print("Gross Salary:", self.gross_salary())


emp = Employee(101, "Yash", 50000)
emp.display()


# 3. Rectangle Class

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

    def display(self):
        print("Length:", self.length)
        print("Breadth:", self.breadth)
        print("Area:", self.area())
        print("Perimeter:", self.perimeter())


rectangle = Rectangle(10, 5)
rectangle.display()


# 4. Circle Class

import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def circumference(self):
        return 2 * math.pi * self.radius

    def display(self):
        print("Radius:", self.radius)
        print("Area:", self.area())
        print("Circumference:", self.circumference())


circle = Circle(7)
circle.display()


# 5. Book Class

class Book:
    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print()


book1 = Book(1, "Python Programming", "John Smith", 450)
book2 = Book(2, "Data Structures", "Robert Brown", 550)
book3 = Book(3, "Object Oriented Programming", "James Lee", 600)

book1.display()
book2.display()
book3.display()


# 6. Electricity Bill Class

class ElectricityBill:
    def __init__(self, consumer_no, consumer_name, units):
        self.consumer_no = consumer_no
        self.consumer_name = consumer_name
        self.units = units

    def calculate_bill(self):
        if self.units <= 100:
            bill = self.units * 1.50

        elif self.units <= 200:
            bill = (100 * 1.50) + ((self.units - 100) * 2.50)

        elif self.units <= 500:
            bill = (100 * 1.50) + (100 * 2.50) + \
                   ((self.units - 200) * 4.00)

        else:
            bill = (100 * 1.50) + (100 * 2.50) + \
                   (300 * 4.00) + ((self.units - 500) * 6.00)

        return bill

    def display(self):
        print("Consumer Number:", self.consumer_no)
        print("Consumer Name:", self.consumer_name)
        print("Units Consumed:", self.units)
        print("Electricity Bill:", self.calculate_bill())


bill = ElectricityBill(1001, "Yash", 350)
bill.display()


# 7. MobilePhone Class

class MobilePhone:
    def __init__(self, brand, model, storage, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.price = price

    def display_specifications(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Storage:", self.storage)
        print("Price:", self.price)

    def discounted_price(self, discount):
        return self.price - (self.price * discount / 100)

    def display(self):
        self.display_specifications()
        print("Price after 10% discount:", self.discounted_price(10))


phone = MobilePhone("Samsung", "Galaxy A55", "256 GB", 40000)
phone.display()


# 8. Patient Class

class Patient:
    def __init__(self, patient_id, name, age, disease, consultation_fee):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease
        self.consultation_fee = consultation_fee

    def total_bill(self, medicine_charges, test_charges):
        return self.consultation_fee + medicine_charges + test_charges

    def display(self):
        print("Patient ID:", self.patient_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Disease:", self.disease)
        print("Consultation Fee:", self.consultation_fee)
        print("Total Bill:", self.total_bill(800, 1200))


patient = Patient(101, "Neha", 25, "Fever", 500)
patient.display()


# 9. ATM Class

class ATM:
    def __init__(self, account_no, name, balance):
        self.account_no = account_no
        self.name = name
        self.balance = balance

    def check_balance(self):
        print("Current Balance:", self.balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            print("Amount deposited:", amount)
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount")

        elif amount > self.balance:
            print("Insufficient balance")

        else:
            self.balance = self.balance - amount
            print("Amount withdrawn:", amount)

    def display_account(self):
        print("Account Number:", self.account_no)
        print("Account Holder:", self.name)
        print("Balance:", self.balance)


atm = ATM("AC101", "Yash", 50000)

while True:
    print()
    print("ATM MENU")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Display Account Details")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        atm.check_balance()

    elif choice == 2:
        amount = float(input("Enter amount to deposit: "))
        atm.deposit(amount)

    elif choice == 3:
        amount = float(input("Enter amount to withdraw: "))
        atm.withdraw(amount)

    elif choice == 4:
        atm.display_account()

    elif choice == 5:
        print("Thank you for using ATM")
        break

    else:
        print("Invalid choice")


# 10. Vehicle Class

class Vehicle:
    def __init__(self, vehicle_no, model, rental_rate, availability):
        self.vehicle_no = vehicle_no
        self.model = model
        self.rental_rate = rental_rate
        self.availability = availability

    def rent(self):
        if self.availability:
            self.availability = False
            print("Vehicle rented successfully")
        else:
            print("Vehicle is not available")

    def return_vehicle(self):
        self.availability = True
        print("Vehicle returned successfully")

    def rental_charges(self, days):
        return self.rental_rate * days

    def display(self):
        print("Vehicle Number:", self.vehicle_no)
        print("Model:", self.model)
        print("Rental Rate:", self.rental_rate)
        print("Availability:", self.availability)


vehicle = Vehicle("MH12AB1234", "Honda City", 2000, True)

vehicle.display()
vehicle.rent()

days = int(input("Enter number of days: "))

print("Rental Charges:", vehicle.rental_charges(days))

vehicle.return_vehicle()


# 11. ShoppingCart Class

class ShoppingCart:
    def __init__(self, customer_name, cart_id):
        self.customer_name = customer_name
        self.cart_id = cart_id
        self.products = []

    def add_product(self, name, price, quantity):
        product = [name, price, quantity]
        self.products.append(product)
        print("Product added:", name)

    def remove_product(self, name):
        for product in self.products:
            if product[0] == name:
                self.products.remove(product)
                print("Product removed:", name)
                return

        print("Product not found")

    def total_bill(self):
        total = 0

        for product in self.products:
            total = total + product[1] * product[2]

        return total

    def display(self):
        print("Customer Name:", self.customer_name)
        print("Cart ID:", self.cart_id)

        print("Products:")

        for product in self.products:
            print(product[0], product[1], product[2])

        print("Total Bill:", self.total_bill())

    def __del__(self):
        print("Shopping cart object destroyed")


cart = ShoppingCart("Yash", "C101")

cart.add_product("Laptop", 50000, 1)
cart.add_product("Mouse", 1000, 2)
cart.add_product("Keyboard", 2000, 1)

cart.remove_product("Mouse")

cart.display()


# 12. FoodOrder Class

class FoodOrder:
    def __init__(self, order_id, customer_name, food_item, quantity, price):
        self.order_id = order_id
        self.customer_name = customer_name
        self.food_item = food_item
        self.quantity = quantity
        self.price = price

    def total_bill(self):
        subtotal = self.quantity * self.price
        tax = subtotal * 0.05
        return subtotal + tax

    def display(self):
        print("Order ID:", self.order_id)
        print("Customer Name:", self.customer_name)
        print("Food Item:", self.food_item)
        print("Quantity:", self.quantity)
        print("Price:", self.price)
        print("Total Bill:", self.total_bill())

    def __del__(self):
        print("Order completed")


order = FoodOrder(101, "Yash", "Pizza", 2, 300)

order.display()


# 13. StudentResult Class

class StudentResult:
    def __init__(self, student_name, marks):
        self.student_name = student_name
        self.marks = marks

    def total(self):
        return sum(self.marks)

    def percentage(self):
        return self.total() / 5

    def grade(self):
        percentage = self.percentage()

        if percentage >= 90:
            return "A+"

        elif percentage >= 80:
            return "A"

        elif percentage >= 70:
            return "B"

        elif percentage >= 60:
            return "C"

        elif percentage >= 50:
            return "D"

        else:
            return "F"

    def display(self):
        print("Student Name:", self.student_name)
        print("Marks:", self.marks)
        print("Total:", self.total())
        print("Percentage:", self.percentage(), "%")
        print("Grade:", self.grade())

    def __del__(self):
        print("StudentResult object destroyed")


result = StudentResult("Yash", [85, 90, 78, 88, 92])

result.display()
```
