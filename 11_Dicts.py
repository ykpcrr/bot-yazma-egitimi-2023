dict_e = {"elma": "apple", "kitap": "book", "kalem": "pencil"}

# Accessing elements of dictionaries

print(dict_e["elma"])
print(dict_e.get("elma"))
print(dict_e.get("siyah", "yok"))

# Adding elements to list
dict_e["masa"] = "table"
dict_e["kırmızı"] = "red"
print(dict_e)

# Remove elements in list
del dict_e["masa"]
print(dict_e)

# Dict methods
# keys()
print(dict_e.keys())

# values()
print(dict_e.values())

# items()
print(dict_e.items())

# nested dictionaries
students = {
    "10/A": {"name": "Yakup", "surname": "Acar", "birthday": 2007},
    "10/B": {"name": "Taha", "surname": "Acar", "birthday": 1998, "notes": [80, 95]}
}
for class_e, student in students.items():
    for key, value in students.items():
        print(f"Class: {class_e}, {key}: {value}")

print(students["10/A"]["name"])