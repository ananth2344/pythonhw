filename = "students.txt"
count = int(input("How many student names do you want to add? "))
print("\n--- Existing Students ---")
existing_students = []

try:
    with open(filename, "r") as file:
        existing_students = [line.strip() for line in file.readlines()]
        if existing_students:
            for name in existing_students:
                print(name)
        else:
            print("No existing names.")
except FileNotFoundError:
    print("File not found. It will be created now.")
new_students = []
print("\nEnter the student names:")
for _ in range(count):
    name = input("> ").strip()
    new_students.append(name)

with open(filename, "a") as file:
    for name in new_students:
        file.write(name + "\n")

print("\n--- Updated Student List ---")
with open(filename, "r") as file:
    all_students = [line.strip() for line in file.readlines()]
    for name in all_students:
        print(name)
