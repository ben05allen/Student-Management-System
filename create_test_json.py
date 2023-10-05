import json

FILE_NAME = "stud.json"

test_data = {
    1: {"roll_number": "1", "name": "jane smith", "percentage": "90.5"},
    2: {"roll_number": "2", "name": "john smith", "percentage": "80.5"},
    3: {"roll_number": "3", "name": "jane doe", "percentage": "70.5"},
    4: {"roll_number": "4", "name": "john doe", "percentage": "70.5"},
}

json.dump(test_data, open(FILE_NAME, "w"))
print("File created successfully")
