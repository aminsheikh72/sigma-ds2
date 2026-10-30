from pathlib import Path

def read_all_files():
    p = Path("")
    files = list(p.rglob("*"))
    for index,value in enumerate(files):
        print(index + 1,value)

def read_file(file_name):
    try:
        with open(file_name) as fs:
            data = fs.read()
            print(data)
    except Exception as err:
        print(f"error occured as {err}")

def create_file(file_name):
    try:
        open(file_name,"x")
    except Exception as err:
        print(f"error occured as {err}")

def create_update_or_write(file_name,name,course,age):
    try:
        p = Path(file_name)
        if p.exists() and p.is_file():
            with open(file_name,"a") as fs:
                fs.write(f"\n{name} {course} {age}")
    except Exception as err:
        print(f"error occured as {err}")


while True:

    print("Press 1 for read file : ")
    print("Press 2 for createfile : ")
    print("Press 3 for create,upate and write file : ")
    print("Press 4 for exist : ")
    choose = input("Choose your response : ")
    if choose == "1":
        read_all_files()
        file_name = input("Enter a file name : ")
        read_file(file_name)
    if choose == "2":
        read_all_files()
        file_name = input("File name : ")
        create_file(file_name)
    if choose == "3":
        read_all_files()
        file_name = input("Enter file name : ")
        name = input("Enter student name : ")
        course = input("Enter student course : ")
        age = input("Enter student age : ")
        create_update_or_write(file_name,name,course,age)
    if choose == "4":
        break
        