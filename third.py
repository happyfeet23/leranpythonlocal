import json

# Define your JSON data as a Python dictionary
data = {
    "name": "John",
    "age": 30,
    "city": "Bengaluru",
    "is_student": False,
    "hobbies": ["reading", "coding", "gaming"]
}

# Create and write to the file
with open("test.json", "a") as testoutput:
    json.dump(data, testoutput, indent=4)  # indent=4 for pretty formatting

print("File 'test.json' \n created successfully!")