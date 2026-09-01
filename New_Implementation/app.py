from student_manager import StudentManager


def main():
    manager = StudentManager()
    print("Student Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    while True:
        choice = input("\nEnter choice: ")

        if choice == "1":
            student_id = input("Student ID: ")
            name = input("Name: ")
            course = input("Course: ")
            manager.add_student(student_id, name, course)
            print("Student added successfully.")

        elif choice == "2":
            students = manager.get_all_students()
            if not students:
                print("No students found.")
            else:
                for student in students:
                    print(student)

        elif choice == "3":
            keyword = input("Enter ID, name, or course to search: ")
            results = manager.search_student(keyword)
            if not results:
                print("No matching students found.")
            else:
                for student in results:
                    print(student)

        elif choice == "4":
            student_id = input("Student ID to delete: ")
            try:
                deleted = manager.delete_student(student_id)
                print(f"Deleted: {deleted}")
            except ValueError as e:
                print(e)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
