frontend_students = {"Alice", "Bob", "Charlie", "Diana"}
backend_students = {"Eve", "Frank", "Charlie", "Grace"}

backend_students.add("Helen")
frontend_students.remove("Bob")

both_courses = frontend_students.intersection(backend_students)
print("Students in both Frontend and Backend:", both_courses)

only_backend = backend_students.difference(frontend_students)
print("Students only in Backend:", only_backend)

unique_students = frontend_students.union(backend_students)
print("Total number of unique students:", len(unique_students))
print("List of all unique students:", unique_students)

courses = {
    "Frontend": len(frontend_students),
    "Backend": len(backend_students)
}

for course, count in courses.items():
    print(f"Course: {course}, Students: {count}")

updated_courses = {**courses, "Fullstack": courses["Frontend"] + courses["Backend"]}
print("Updated course list with 'Fullstack':", updated_courses)
