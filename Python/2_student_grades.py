students = {}

while True:
    print("\n1. Add student")
    print("2. Update grade")
    print("3. Print all grades")
    print("4. Quit")
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        name = input("Enter student name: ")
        if name in students:
            print(name, "already exists. Use update instead.")
        else:
            grade = input("Enter grade: ")
            students[name] = grade
            print("Added", name, "with grade", grade)

    elif choice == "2":
        name = input("Enter student name to update: ")
        if name in students:
            grade = input("Enter new grade: ")
            students[name] = grade
            print("Updated", name, "to grade", grade)
        else:
            print(name, "not found.")

    elif choice == "3":
        if students:
            print("\nAll student grades:")
            for name, grade in students.items():
                print(name, ":", grade)
        else:
            print("No students yet.")

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid option. Try again.")
