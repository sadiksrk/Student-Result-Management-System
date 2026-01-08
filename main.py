import json

FILE = "students.json"

def load_data():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_student():
    data = load_data()
    roll = input("Enter Roll Number: ")

    if roll in data:
        print("Roll number already exists!")
        return

    name = input("Enter Student Name: ")
    s1 = int(input("Marks in Subject 1: "))
    s2 = int(input("Marks in Subject 2: "))
    s3 = int(input("Marks in Subject 3: "))

    total = s1 + s2 + s3
    percentage = total / 3
    grade = "A" if percentage >= 75 else "B" if percentage >= 60 else "C"

    data[roll] = {
        "name": name,
        "marks": [s1, s2, s3],
        "total": total,
        "percentage": percentage,
        "grade": grade
    }

    save_data(data)
    print("Student added successfully!")

def view_student():
    data = load_data()
    roll = input("Enter Roll Number: ")

    if roll in data:
        print(json.dumps(data[roll], indent=4))
    else:
        print("Student not found!")

def view_all():
    data = load_data()
    for roll, info in data.items():
        print(f"\nRoll: {roll}")
        print(json.dumps(info, indent=4))

def delete_student():
    data = load_data()
    roll = input("Enter Roll Number: ")

    if roll in data:
        del data[roll]
        save_data(data)
        print("Record deleted!")
    else:
        print("Roll number not found")

def menu():
    while True:
        print("\n--- Student Result Management System ---")
        print("1. Add Student")
        print("2. View Student")
        print("3. View All Students")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_student()
        elif choice == "3":
            view_all()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            break
        else:
            print("Invalid choice!")

menu()
