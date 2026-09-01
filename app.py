students = [
    {"name": "Ravi", "marks": [85, 78, 92]},
    {"name": "Basha", "marks": [75, 88, 81]},
    {"name": "Kiran", "marks": [65, 72, 69]},
    {"name": "Arjun", "marks": [92, 95, 90]},
    {"name": "Suresh", "marks": [55, 60, 58]}
]


def calculate_total(marks):
    return sum(marks)


def calculate_average(marks):
    return sum(marks) / len(marks)


def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "Fail"


print("=" * 50)
print("       STUDENT RESULT MANAGEMENT SYSTEM")
print("=" * 50)

for student in students:

    name = student["name"]
    marks = student["marks"]

    total = calculate_total(marks)
    average = calculate_average(marks)
    grade = calculate_grade(average)

    print("\nStudent Name :", name)
    print("Subject 1    :", marks[0])
    print("Subject 2    :", marks[1])
    print("Subject 3    :", marks[2])
    print("Total Marks  :", total)
    print("Average      :", round(average, 2))
    print("Grade        :", grade)

print("\n" + "=" * 50)
print("           RESULT SUMMARY")
print("=" * 50)

passed = 0
failed = 0

for student in students:

    average = calculate_average(student["marks"])

    if average >= 50:
        passed += 1
    else:
        failed += 1

print("Total Students :", len(students))
print("Passed Students:", passed)
print("Failed Students:", failed)

print("\nJenkins Python Build Completed Successfully!")
print("=" * 50)
