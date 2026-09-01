class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student_id, name, course):
        for student in self.students:
            if student["id"] == student_id:
                raise ValueError("Student ID already exists")

        student = {
            "id": student_id,
            "name": name,
            "course": course,
        }
        self.students.append(student)
        return student

    def get_all_students(self):
        return self.students

    def search_student(self, key):
        key = str(key).lower()
        result = []
        for student in self.students:
            if key in str(student["id"]).lower() or key in student["name"].lower() or key in student["course"].lower():
                result.append(student)
        return result

    def delete_student(self, student_id):
        for i, student in enumerate(self.students):
            if student["id"] == student_id:
                return self.students.pop(i)
        raise ValueError("Student not found")
