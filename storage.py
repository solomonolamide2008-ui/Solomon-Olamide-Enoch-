import json
import os
from student import Student

DATA_FILE = os.path.join('data', 'student.json')

def ensure_data_directory():
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

def load():
    ensure_data_directory()
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, 'r') as f:
            student_dict = json.load(f)
            return [Student.from_dict(item) for item in student_dict]
    except ( json.JSONDecodeError, FileNotFoundError ) as e:
        print(f'Error reading data from {DATA_FILE}: {e}:')
        return []
def save(student):
    ensure_data_directory()
    try:

        with open(DATA_FILE, 'w') as f:
            json.dump([s.to_dict()for s in student], f, indent=4)
        print('Data is saved to', DATA_FILE)
    except  FileNotFoundError  as e:
        print(f'Error saving data to {DATA_FILE}: {e}:')

