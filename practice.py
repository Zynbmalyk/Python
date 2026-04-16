# # Task:

# # A customer buys:

# # Quantity of item (input from user)
# # Price of one item (input from user)

# #👉 Calculate the total bill amount and print it.

# Quantity= input("enter the quantity  ")
# price = input("enter the price of one item   ")
# bill = print(int(Quantity)*int(price))


# # Take user input for a number and print its square.

# number =input("Enter the number :")
# b = int(number)*int(number )
# print(f"the square of {number} is {b}")


# # Take a number and print its factorial (basic loop allowed)
# number = int(input("Enter the number :"))
# count = 1
# for i in range(1, number + 1):
#     count = count * i     
# print(f"The factorial of {number} is {count}")
# count = 0
# letter = input("Write a letter :")
# for i in range(1,len(letter)+1):
#     if letter[i-1] == "a" or letter[i-1] == "e" or letter[i-1] == "i" or letter[i-1] == "o" or letter[i-1] == "u":
#         print(f"{letter[i-1]} is a vowel")
#         count += 1


# print(f"The number of vowels in '{letter}' is {count}")



# word = input("Enter a word :")
# reverse = ""
# for i in range(len(word)-1, -1, -1):
#     reverse = reverse + word[i]



# print(f"The reverse of '{word}' is '{reverse}'")


# for i in range(0,10):
#     i = i+1
#     print(i)



# for i in range(9, -1, -1):
#     i = i+1
#     print(i)



# # for i in range(0,21,2):r
# #     print(i)

# # for i in range(1,21):
# #     if i%2 == 0:
# #         print(i)    

# number = (input("Enter a number :"))
# total = 0
# for i in range(1, number + 1):
#       total = total + i

# print(total)



# for i in range(1,11):
#     table = number * i
#     print(number, "x", i, "=", table)


# count = 0
# for i in range(1, len(number)+1):
#     count +=1

    

# print(count)

# word = input("Enter a word :")
# reverse = ""
# for i in range(len(word)-1, -1, -1):
#     reverse = reverse + word[i]

# if word == reverse:
#     print(f"{word} is a palindrome")

# for i in range(0,7):
#     for j in range(0, i+1):
#         print("*", end="")
#     print("\n")




# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade

#     def display_info(self):
#         print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

# student1 = Student("Alice", 20, "A")
# student1.display_info()

# class rectangle:
#     def __init__(self, length, width):
#         # self.lenght =length
#         # self.width = width 
#         input_length = input("Enter the length of the rectangle :")
#         input_width = input("Enter the width of the rectangle :")
#         self.lenght = int(input_length)
#         self.width = int(input_width)

#     def area(self):
#         print(f"Area = {self.lenght * self.width}")
#     def perimeter(self):
#         print(f"Perimeter = {2*(self.lenght + self.width)}")
    
# rectangle1 = rectangle(5, 3)
# rectangle1.area()
# rectangle1.perimeter()


# class ShoppingCart:
#     def __init__(self):
#         self.items = []

#     def add_item(self, item):
#         self.items.append(item)

#     def remove_item(self, item):
#         if item in self.items:
#             self.items.remove(item)

#     def view_cart(self):
#         print("Items in the shopping cart:")
#         for item in self.items:
#             print(item)


# add_item1 = input("Enter the item you want to add to the cart :")
# cart = ShoppingCart()
# cart.add_item(add_item1)
# cart.view_cart()
# cart.add_item(input("Enter the item you want to add to the cart :"))
# cart.view_cart()




# Year = input("Enter the year :")

# if int(Year) % 4 == 0 and  int(Year) % 100 != 0 or int(Year) % 400 == 0:
#             print(f"{Year} is a leap year")
# else:
#             print(f"{Year} is not a leap year")


# list1 = [1, 2, 3, 4, 2]
# list2 = [6, 5, 8, 7, 6]

# list = list1 + list2
# print(list)






# list1 = [1, 2, 1, 4, 2]
# for i in range(0, len(list)):
#     for j in range(i + 1, len(list)-1):
#         if list[i] == list[j]:
#             list.remove(list[j])


# print(list)
# sorted_list = sorted(list)
# print(sorted_list)



# def count_alphabet(alphabet):
#     # alphabet = input("Enter a word:")
#     count = 0
#     for i in range(0,len(alphabet)+1):
#        count += 1
#     print(f"The number of alphabet in '{alphabet}' is {count}")


# count_alphabet("Pakistan")




# class Student:
#     def __init__(self,name,age):
#         self.name = name 
#         self.age = age 
#     def display(self):
#         print(f"I am {self.name} and my age is {self.age}")
        


# one = Student("Ali", 20)
# two = Student("Ahmed", 22)
# one.display()
# two.display()


# class Rectangle:
#     def __init__(self,lenght,width): 
#         self.lenght =lenght 
#         self.width = width 
#     def Area(self): 
#             print(f"Area = {self.lenght*self.width}")
        
# one = Rectangle(12,5)
# one.Area()


# class BankAccount:
#     def __init__(self,account_number,balance):
#         self.account_number = account_number
#         self.balance = balance
#     def deposit(self,amount):
#         self.amount = amount
#         self.balance = self.balance + self.amount
#     def withdraw(self,amount):
#              self.amount = amount
#              if self.amount > self.balance:
#                  print("Insufficient balance")
#              else:
#                   self.balance = self.balance - self.amount
#     def check_balance(self):
#          print(f"Your balance is {self.balance}")
    
# account_1 = BankAccount("123456789", 1000)
# account_1.deposit(500)
# account_1.check_balance()
# account_1.withdraw(200)
# account_1.check_balance()
# account_1.withdraw(1500)
        

# class Employee:
#     def __init__(self,name,salary):
#           self.name =name
#           self.salary = salary
#     def increase_salary(self,percent):
#          self.percent = percent
#          decimal_percent = self.percent / 100
#          self.increase_salary = self.salary * decimal_percent
#          self.salary = self.salary + self.increase_salary
#     def display_info(self):
#           print(f"Name: {self.name}, Salary: {self.salary}")


# emp = Employee("Ali", 50000)
# emp.increase_salary(10)
# emp.display_info()

# class MathUtils:
#      @staticmethod
#      def addd(a,b):
#        print(a + b)
#      @staticmethod
#      def multiplyy(c , d):
#          print(c * d)

# MathUtils.addd(2,6)
# MathUtils.multiplyy(4,8)

# class Person:
#     def display(self,name):
#         print(f"My name is {name}")
# class Student(Person):
#     def display(self,name,age):
#         super().display(name)
#         print(f"My age is {age}")
# student1 = Student()
# student1.display("Ali", 20)

# class vehicle:
#     def start(self):
#         print("Vehicle is starting")
# class car(vehicle):
#     def start(self):
#         print("Car is starting")

# o = car()
# o.start()



# class Teacher:
#     def teach(self):
#         print("Teaching...")
# class Researcher:
#     def research(self):
#         print("Researching...")
# class Professor(Teacher, Researcher):
#     def display(self):
#         self.teach()
#         self.research()
#         print("I am a professor.")


# p = Professor()
# p.display()



# class Person:
#     def display(self,name):
#         print(f"My name is {name}")
# class Student(Person):
#     def display_marks(self,marks):
#         self.marks = marks
#         print(f"My marks are {marks}") 
# student1 = Student()
# student1.display("Ali")
# student1.display_marks(85)

# class Animal:
#     def eat(self):
#         print("Eating...")
# class Dog(Animal):
#     def bark(self):
#         print("Barking...")
# d = Dog()
# d.eat()
# d.bark()

# class Animal:
#     def sound(self):
#         print("Some sound...")
# class Dog:
#     def sound(self):
#         print("Barking...")
# d = Dog()
# d.sound()


# class Person:
#     def name(self):
#       input_name = input("Enter the name of the student :")
#       self.name = input_name

# class Student(Person):
#     def marks(self):
#         super().name()
#         input_marks = input("Enter the marks of the student :")
#         self.marks = input_marks
#         print(f"Name: {self.name}, Marks: {self.marks}")


# s1 = Student()
# s1.marks()


# class A:
#     def show(self):
#         print("Class A")
# class B:
#     def show(self):
#         print("Class B")
# class C(A, B):
#     def show(self):
#         # A.show(self)
#         # B.show(self)
#         super().show()
#         print("Class C")


# c = C()
# c.show()


# class Vehicle:
#     def  doc(self):
#         name = input("Enter the name of the vehicle :")
#         owner = input("Enter the name of the owner :")
#         price = input("Enter the price of the vehicle :")
#         model = input("Enter the model of the vehicle :")
#         Vehicle_list = []
#         Vehicle_list.append(f"Name: {name}, Owner: {owner}, Price: {price}, Model: {model}")
#         print("This is the vehicle report.")
#         return Vehicle_list
        

# class report(Vehicle):
#     def display(self):
#       print(self.doc())

# r1 = report()
# r1.display()

# class Vehicle:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def get_info(self):
#         return f"{self.brand} {self.model}"

# class Car(Vehicle):
#     def __init__(self, brand, model, doors):
#         super().__init__(brand, model)  # Calls parent constructor
#         self.doors = doors

#     def display(self):
#         print(f"Car: {self.get_info()} with {self.doors} doors")

# class Truck(Vehicle):
#     def __init__(self, brand, model, capacity):
#         super().__init__(brand, model)
#         self.capacity = capacity

#     def display(self):
#         print(f"Truck: {self.get_info()} with {self.capacity} ton capacity")

# # Usage
# my_car = Car("Toyota", "Corolla", 4)
# my_truck = Truck("Isuzu", "NPR", 5)

# my_car.display()   
# my_truck.display() 


# class Student:
#     def __init__(self,marks):
#         self.__marks =marks
#     def get_marks(self):
#       print(f"Marks: {self.__marks}")
# s1 = Student(85)
# s1.get_marks()


# class BankAccount:
#     __balance = 0
#     def deposit(self, amount):
#          if amount < 0:
#              print("Invalid amount")
#          self.__balance += amount
#     def withdraw(self, amount):
#          if amount > self.__balance:
#              print("Insufficient balance")
#          else:
#               self.__balance -= amount
#     def check_balance(self):
#          print(f"Your balance is {self.__balance}")
# account_1 = BankAccount()
# account_1.deposit(-100)
# account_1.check_balance()
# account_1.withdraw(200)
# account_1.check_balance()
    
# class Test:
#     def __init__(self):
#         self.__x = 10


# t1 = Test()
# print(t1.__x)



# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
    
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2
# class Square(Shape):
#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return self.side ** 2
    

# circle = Circle(5)
# square = Square(4)
# print(f"Area of the circle: {circle.area()}")
# print(f"Area of the square: {square.area()}")


# from abc import ABC ,abstractmethod
# class Employee(ABC):
#     @abstractmethod
#     def salary(self):
#         pass
# class Manager(Employee):
#     def salary(self):
#         print("Manager's salary is $5000")
# class Developer(Employee):
#     def salary(self):
#         print("Developer's salary is $4000")
# manager = Manager()
# developer = Developer()
# manager.salary()
# developer.salary()

# num = int(input("Enter a number :"))
# try: 
#     result = 10 / num
#     print(f"Result: {result}")
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero.")

# with open("data.txt", "w") as f:
#     f.write("Hello, this is a sample text file.\n")
#     f.write("This file is used for practicing file handling in Python.\n")
#     f.write("Have a great day!")
# with open("data.txt", "r") as f:
#     content=  f.read()
#     print(content)


# try: 
#     with open("data1.txt", "r") as f:
#         content = f.read()
#         print(content)
# except FileNotFoundError:
#     print("Error: The file 'data1.txt' was not found.")

# try: 
#     with open("file.csv", "w") as f:
#         f.write("Name, Age, City\n")
#         f.write("Alice, 30, New York\n")
#         f.write("Bob, 25, Los Angeles\n")
#         f.write("Charlie, 35, Chicago\n")
  
#     with open("file.csv", "r") as f:
#         data = f.read()
#         print(data)

# except Exception as e:
#     print(f"An error occurred: {e}")

# try: 
#     with open("file.json", "w") as f:
#         f.write('{"name": "Alice", "age": 30, "city": "New York"}\n')
#         f.write('{"name": "Bob", "age": 25, "city": "Los Angeles"}\n')
#         f.write('{"name": "Charlie", "age": 35, "city": "Chicago"}\n')
#     with open("file.json", "r") as f:
#         data = f.read()
#         print(data)

# except Exception as e:
#     print(f"An error occurred: {e}")

# class MyNumbers:
#   def __iter__(self):
#     self.a = 1
#     return self

#   def __next__(self):
#     x = self.a
#     self.a += 1
#     return x

# myclass = MyNumbers()
# myiter = iter(myclass)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))


# tuple1 = ("apple", "banana", "cherry")
# myit = iter(tuple1)
# print(next(myit))
# print(next(myit))
# print(next(myit))

# number = [1, 2, 3, 4, 5]
# myit = iter(number)
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))


# def read_file(file):
#  with open(file, "r") as f:
#    for line in f:
#         print(line.strip())
    

# read_file("file.json")


# def gen():
#    for i in range(1, 6):
#          yield i


# g = gen()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# def number():
#    for i in range(1, 11):
#        if i % 2 == 0:
#             yield i


# n = number()
# print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))
# def func():
#     print("This is a function.")
# def decorator(func):
#     def wrapper():
#         print("Before the function is called.")
#         func()
#         print("After the function is called.")
#     return wrapper

# f1 = decorator(func)
# f1()

# def greet():
#     print("Hello")

# greet = decorator(greet)
# greet()

# class iterable:
#     def __init__(self, no):
#         self.no = no
#     def iter (self):
#        for i in range(1, self.no + 1):
#            yield i


# n = iterable(9)
# print(list(n.iter()))
        
# number = int(input("Enter a number :"))
# def func():
#     if number % 2 == 0:
#         print(f"{number} is an even number")
# def decorator(func):
#     def wrapper():
#         print("Checking if the number is even or odd...")
#         func() 
#     return wrapper

# f1 = decorator(func)
# f1()




# def gen():
#     for i in range(10000000):
#             yield i
            

# g = gen()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# import time
# def decorator(func):
#  def wrapper():
#         start_time = time.time()
#         func()
#         end_time = time.time()
#         print(f"Execution time: {end_time - start_time} seconds")
#  return wrapper

# @decorator
# def func():
#   pass


# f1 = decorator(func)
# f1 ()


import time

def func():
    print("This is a function that does nothing.")
    for i in range(10):
        print(i)
    for j in range(1,10):
        if j < 0:
            print(f"{j} is a negative number")
        else:
            print(f"{j} is a positive number")

def decorator(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
    return wrapper

f1 = decorator(func)
f1()



















