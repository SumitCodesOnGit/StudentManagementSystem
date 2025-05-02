from student import StudentDatabase

def main():
    db = StudentDatabase()

    while True:
        print("---Student Management System------")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student by Name")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Name: ")
            age = input("Age: ")
            grade = input("Grade: ")
            db.add_student(name, int(age), grade)

        elif choice == '2':
            students =db.view_students()
            for s in students:
                print(f"ID: {s[0]}, Name: {s[1]}, Age: {s[2]}, Grade: {s[3]}")


        elif choice == '3':
            keyword = input("Enter name to search: ")
            results = db.search_student(keyword)
            if results:
                for s in results:
                    print(f" ID: {s[0]}, Name: {s[1]}, Age: {s[2]}, Grade: {s[3]}")
            else:
                print("No matching student found.")



        elif choice == '4':
            student_id = input("Enter student ID to update: ")
            name = input("New Name: ")
            age = input("New Age: ")
            grade =  input("New Grade: ")
            db.update_student(student_id, name, age, grade)

        
        elif choice == '5':
            student_id = input("Enter student ID to delete: ")
            db.delete_student(student_id)


        elif choice == '6':
            db.close()
            print("Exiting system.")
            break

        else:
            print("Invalid Option. Try again.")



if __name__ == '__main__':
    main()




