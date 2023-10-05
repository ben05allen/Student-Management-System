from dataclasses import dataclass
import json
import os
import time


JSON_FILE = "stud.json"


def load_json() -> dict:
    try:
        with open(JSON_FILE, "r") as file:
            return json.load(file)

    except IOError:
        print("File could not be opened!!")


def write_json(student_data: dict):
    try:
        with open(JSON_FILE, "w") as file:
            json.dump(student_data, file)
    except IOError:
        print("File could not be opened!!")


@dataclass
class Student:
    """
    to maintain student details
    roll number
    name
    percentage
    """

    roll_number: int | None = None
    name: str | None = None
    percentage: float | None = None

    def __post_init__(self):
        if self.name:
            self.name = self.name.upper()

    def modify_rec(self):
        self.roll_number = int(input("Enter new roll number: "))
        self.name = input("Enter new name: ").upper()
        self.percentage = float(input("Enter new percentage: "))


def search_for_roll_number(students_data: dict, roll_number: str) -> Student:
    if (student_dict := students_data.get(roll_number)) is None:
        return None
    return Student(**student_dict)


def add_record():
    student_data = load_json()

    new_record = Student()
    new_record.modify_rec()
    student_data[new_record.roll_number] = new_record.__dict__

    write_json(student_data)
    print("Record added in file!")


def display_all():
    print(40 * "=")
    print("\n\tStudent Records\n")
    print(40 * "=")

    students_data = load_json()
    if students_data and isinstance(students_data, dict):
        for student_data in students_data.values():
            print(Student(**student_data))
    else:
        print("No records found!!")


def search_roll():
    print(40 * "=")
    print("Record searching by roll number...")
    print(40 * "=")

    roll_number = input("Enter roll number to search: ")
    student_data = load_json()

    if not (student_record := search_for_roll_number(student_data, roll_number)):
        print("Record is not present!!")
    else:
        print("\nRecord found and details are:\n")
        print(student_record)


def search_name():
    print(40 * "=")
    print("Record searching by name...")
    print(40 * "=")
    name = input("Enter name to search: ").upper()
    student_data = load_json()
    for student_dict in student_data.values():
        if student_dict.get("name") == name:
            student_record = Student(**student_dict)
            print("\nRecord found and details are:\n")
            print(student_record)
            break

    else:
        print("Record is not present!!")


def modify_roll():
    roll_number = input("Enter roll number to modify: ")
    student_data = load_json()

    if not (record_to_modify := search_for_roll_number(student_data, roll_number)):
        print("Record not found!!")
    else:
        print("\nRecord found and details are:\n")
        print(record_to_modify)

        print("\nEnter new data...")
        record_to_modify.modify_rec()

        student_data[roll_number] = record_to_modify.__dict__
        write_json(student_data)

        print("Record updated!")


def delete_roll_number():
    roll_number = input("Enter roll number to delete: ")
    student_data = load_json()
    if not (record_to_delete := search_for_roll_number(student_data, roll_number)):
        print("Record not found!!")
    else:
        print("\nRecord to delete found and details are:\n")
        print(record_to_delete)

        if input("Confirm deletion (y/N)? ").upper()[0] == "Y":
            del student_data[roll_number]
            write_json(student_data)
            print("Record updated!")


def main():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(40 * "=")
        print(
            """               Main Menu 
                --------- 
            1. Add record 
            2. Display all records 
            3. Search by roll number 
            4. Search by name 
            5. Modify by roll number 
            6. Delete by roll number 
            7. Exit 
        """
        )

        print(40 * "=")
        choice = int(input("Enter your choice: "))
        print(40 * "=")

        if choice == 1:
            add_record()
        elif choice == 2:
            display_all()
        elif choice == 3:
            search_roll()
        elif choice == 4:
            search_name()
        elif choice == 5:
            modify_roll()
        elif choice == 6:
            delete_roll_number()
        elif choice == 7:
            print("\n\t      !!!End!!!\n")
            time.sleep(2)
            break
        else:
            print("Invalid choice!!")
            time.sleep(1)

        input("\n[Enter] to continue....")


if __name__ == "__main__":
    main()
