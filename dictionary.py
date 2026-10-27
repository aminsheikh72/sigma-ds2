d = {}

d["name"] = "eskills"
d["brand"] = None
d["age"] = 18
d["name"] = "amin"
# d.update({"skills": ["python", "java", "c++"]})
# d.update({"name" : "amin"})
# print(d.get("name"))



# print(d.values())
# print(d.keys())
# print(d.items())
# d.pop("age")
# d.popitem()
# d.clear()
# a = d.copy()
# a.update({"name" : "indore"})
# print(a)
# s = {}
# print(s.fromkeys(["name", "age", "skills"], None))
# print(s)
# print(d)


# for i in d:
#     print(d[i])

# print(d["skills"][0])


# Q1. Dictionary banao
# Ek dictionary banao jisme student ka name, age aur city store ho.
#  Values: name = Amin, age = 20, city = Indore.
# Expected output:
# d = {}
# d["name"] = "Amin"
# d["age"] = 22
# d["city"] = "Barwani"
# print(d)

# Q2. Value access karo
# Di gayi dictionary se student ka naam aur marks print karo.
# Given code:
# student = {
# "name": "Rahul",
# "marks": 85,
# "class": 12
# }
# print(student["marks"],student["name"])

# Q3. Value update karo
# Dictionary mein price ki value 100 se 150 kar do.
# Given code:
# product = {"name": "Pen", "price": 100}
# product["price"] = 150
# product.update({"price" : 150})
# print(product)

# Q4. New key add karo
# Dictionary mein "color": "red" add karo.
# Given code:
# car = {"brand": "Tata", "model": "Nexon"}
# car.update({"color" : "Red"})
# print(car)

# Q5. Key delete karo
# Dictionary se "age" key delete karo.
# Given code:
# person = {"name": "Amin", "age": 20, "city": "Indore"}
# person.pop("age")
# del person["age"]
# print(person)


# Q6. Dictionary par loop lagao
# Har key aur value ko alag-alag print karo.
# Given code:
fruits = {"apple": 50, "banana": 30, "mango": 80}
# for i in fruits:
#     print(i,fruits[i])

# for k,v in fruits.items():
#     print(k,v)


# Q7. Values ka sum nikalo
# Sabhi students ke marks ka total calculate karo.
# Given code:
marks = {"Amit": 70, "Ravi": 80, "Amin": 90}
# sum = 0
# for i in marks.values():
#     sum += i

# print(sum)

# total = sum(marks.values())
# print(total)

# Q8. Key exist karti hai ya nahi?
# Check karo ki "email" key dictionary mein hai ya nahi.
# Given code:
# user = {"name": "Amin", "age": 20}
# if "email" not in user:
#     print("Email does not exist")
# else:
#     print("Email exist")

# Q9. Maximum value nikalo
# Sabse zyada marks kis student ke hain? Uska naam aur marks print karo.
# Given code:
# marks = {"Amit": 75, "Ravi": 92, "Amin": 88}
# name = ""
# max = 0
# for i in marks:
#     if max < marks[i]:
#         max = marks[i]
#         name = i

# print(name,max)

# Q10. keys(), values(), items()
# In teeno methods ka use karke dictionary ki
#  keys, values aur key-value pairs print karo.
# Given code:
# mobile = {"brand": "Samsung", "price": 20000, "ram": "8GB"}
# print(mobile.keys())
# print(mobile.values())
# print(mobile.items())

# Q11. Character frequency
# String ke har character ke aane ki frequency count karke dictionary banao.
# Given code:
# text = "banana"
# d = {}
# for i in text:
#     if i not in d:
#         d[i] = 1
#     else:
#         d[i] +=1

# print(d)

# Q13. Do dictionaries merge karo
# Dono dictionaries ko ek dictionary mein merge karo.
# Given code:
# a = {"name": "Amin", "age": 20}
# b = {"city": "Indore", "course": "Python"}

# print(a | b)