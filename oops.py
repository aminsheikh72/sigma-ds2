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