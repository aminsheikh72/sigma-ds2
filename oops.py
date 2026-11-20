# a = 30
# b = 40
# print(a + b)


# def add(a,b):
#     print(a + b)

# add(10,20)
# add(80,100)


# student1 = {
#     "name" : "madhav",
#     "age" : 22,
#     "class" : "11th",
#     "fees" : 20000,
#     "collect" : 10000
# }

# def calculate_fees():
#     return f"{student1["fees"] - student1["collect"]}"

# pending = calculate_fees()
# print(pending)



# class Thar:
#     brand = "Mahindra" #attribute
#     color = "Red"
#     model = "Thar"
#     def show(self): #method
#         print(f"{self.brand} , {self.color}")

# class Car:
#     def __init__(self,color,brand,model):
#         self.color = color
#         self.brand = brand
#         self.model = model

#     def start(self):
#         print(f"{self.model} starts")
#     def stop(self):
#         print(f"{self.model} stop")
#     def details(self):
#         print(f"The Car name is {self.model} and it has {self.color} color")

# thar = Car("Red","Mahindra","Thar")
# seltos = Car("Black","Kia","Seltos advanture")
# hector = Car("Red","MG","Hector")
# harrier = Car("Green","TATA","harrier")
# alto = Car("white","suzuki","alto 800")


# alto.details()
# hector.details()


# class Student:

#     def __init__(self,name,age,id):
#         self.name = name 
#         self.age = age
#         self.id = id
#     def show_details(self):
#         print(f"student name is {self.name}, age is {self.age} years and id is {self.id}")
#     print("hey I am intialized")

        


# madhav = Student("madhav",21,101)
# kartik = Student("kartik",20,105)
# sneh = Student("sneh",24,108)
# kartik.show_details()
# print(sneh.name)


# class MyClass:
#     @classmethod
#     def show(cls):
#         print("hey I am class method")

# MyClass.show()


# class School:
#     school = "Eskills"

#     @classmethod
#     def change_school(cls,new_school):
#         cls.school = new_school
       

# School.change_school("Eskills barwani")
# print(School.school)


# class Car:
#     name = "amin"
#     @staticmethod
#     def sound():
#         print("Hey I am static method")
# Car.sound()


# class Animal:
#     a = "animal"
#     def sound():
#         print("Hello I am animal")

# class Dog(Animal):
#     pass

# Dog.a

# single level
# class Employee:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def show_details(self):
#         print(f"name : {self.name}\nage : {self.age}")


# class Developer(Employee):
#     def __init__(self,name,age,salary):
#         super().__init__(name,age)
#         self.salary = salary
        
# a = Employee("amin",20)
# amin = Developer("amin",20,2000)
# amin.show_details()


# multiple
# class Father:
#     a = "father"
#     def work(self):
#         print("Coding")

# class Mother:
#     b = "mother"
#     def work(self):
#         print("Cooking")

# class Child(Father,Mother):
#     pass

# father = Father()
# mother = Mother()
# child = Child()
# print(child.a)


# multi level

# class GrandFather:
#     def house(self):
#         print("GrandFather has a house")


# class Father(GrandFather):
#     def car(self):
#         print("father has a car")

# class Son(Father):
#     def bike(self):
#         print("Son has a bike")

# son = Son()

# class Dog:
#     def sound(self):
#         print("Dog Barks")

# class Cat:
#     def sound(self):
#         print("Cat meowss")

# class Cow:
#     def sound(self):
#         print("Coww sound")

# dog = Dog()
# cat = Cat()
# cow = Cow()
# cow.sound()


# class Animal:
#     def sound(self):
#         print("Animal makes sound")

# class Dog(Animal):
#     def sound(self):
#         print("Dog barksss")

# class Cat(Animal):
#     def sound(self):
#         print("Cat meowss")


# animal = Animal()
# dog = Dog()
# cat = Cat()

# animal.sound()
# dog.sound()

# def add(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum

# sum = add(10,20,30,40,50,50)
# print(sum)

# def student(**agrs):
#     return agrs

# s = student(name="amin",age=20,course="hindi")
# print(s)

# 3. Multilevel Inheritance: Create three classes: Grandfather, Father, and Son. Add one method to each class.
# Call all three methods using an object of Son

# class GrandFather:
#     def a(self):
#         print("I am grand father")

# class Father(GrandFather):
#     def b(self):
#         print("I am father")

# class Son(Father):
#         def c(self):
#             print("I am father")

# grand_father = GrandFather()
# father = Father()
# son = Son()
# son.a()



# class Bank:
#     balance = 1000


# bank = Bank()
# print(bank.balance)


# class Student:

#     def __init__(self):
#         self.name = "Rahul"
#         self.age = 22

#     def show(self):
#         print(self.name)
#         print(self.age)


# s1 = Student()

# print(s1.name)
# print(s1.age)

# s1.show()

# class Student:
#     _name = "amin"
#     def _show(self):
#         print(f"Student name : {self._name}")

# amin = Student()
# amin._show()

# class Student:
#     __name = "amin"

# class Child(Student):
#     def __init__(self,name):
#         super().__init__(__name__)

# amin = Student()
# child = Child()
# print(child.__name)

# class BankAccount:
#     def __init__(self,balance,pin):
#         self.__balance = balance
#         self.__pin = pin

#     def check_balance(self):
#         print(f"Your balance : {self.__balance}")

#     def deposit(self,amount):
#         if amount > 0 :
#             self.__balance += amount
#             print("Money deposited successfully")
#         else:
#             print("Invalid amount")

#     def withdraw(self,pin,amount):
#         if self.__pin != pin:
#                 print("Invalid pin")
#         elif amount <= self.__balance:
#                 self.__balance -= amount
#                 print("Money withdrawn succesfully")
#         else:
#                 print("Insufficient Balance")

# account = BankAccount(10000,1010)
# account.check_balance()
# account.deposit(5000)
# account.check_balance()
# account.withdraw(1010,5000)
# account.check_balance()
