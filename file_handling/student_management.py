from pathlib import Path
def read_files_and_folders():
    p = Path("")
    files = list(p.rglob("*"))
    for i,v in enumerate(files):
        print(i+1,v)

def create_file(file_name):
    try:
        open(file_name,"x")
    except Exception as err:
        print(f"error occured as {err}")

def add_student(file_name,name,course,age):
    try:
        with open(file_name,"a") as fs:
            fs.write(f"\n{name} {course} {age}")
    except Exception as err:
        print(f"error occure as {err}")
def read_file(file_name):
    
    try:
        with open(file_name) as fs:
            print(fs.read())
    except Exception as err:
        print(f"error occured as {err}")

while True:
    print("Press 1 for create file : ")
    print("press 2 for add student : ")
    print("press 3 for read file : ")
    print("Press 4 for exit : ")
    choice = input("Enter you choice")
    if choice == "1":
        read_files_and_folders()
        file_name = input("Enter a file name : ")
        create_file(file_name)
    if choice =="2":
        read_files_and_folders()
        file_name = input("Enter a file name : ")
        name = input("Enter student name : ")
        course = input("Enter student course : ")
        age = input("Enter student age : ")
        add_student(file_name,name,course,age)
    if choice == "3":
        read_files_and_folders()
        file_name = input("Enter a file name : ")
        read_file(file_name)
    if choice == "4":
        break

