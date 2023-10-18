
def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

# Define the Student class
class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

# Example usage:

# Create a list of student objects
students = [
    Student("Alice", "S123", 3.8),
    Student("Bob", "S456", 3.6),
    Student("Charlie", "S789", 3.9),
    Student("David", "S101", 3.7),
]

# Sort the list of students by CGPA
sorted_students = sort_students(students)

# Print the sorted list of students
for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
