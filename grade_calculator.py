def calculate_grade(marks):
    if 90 <= marks <= 100:
        return "A", "Excellent work! 🌟"
    elif marks >= 75:
        return "B", "Great job! 👍"
    elif marks >= 60:
        return "C", "Good effort! 🙂"
    elif marks >= 50:
        return "D", "Keep improving! 💪"
    else:
        return "F", "Don't give up, try again! 🚀"


def get_valid_marks():
    while True:
        try:
            marks = float(input("Enter marks (0-100): "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("❌ Marks must be between 0 and 100.")
        except ValueError:
            print("❌ Invalid input. Please enter a number.")


def get_student_name():
    while True:
        name = input("Enter student name: ").strip()
        if name:
            return name
        else:
            print("❌ Name cannot be empty.")


def main():
    print("🎓 Student Grade Calculator")

    name = get_student_name()
    marks = get_valid_marks()

    grade, message = calculate_grade(marks)

    print("\n----- Result -----")
    print(f"Student Name: {name}")
    print(f"Marks: {marks}")
    print(f"Grade: {grade}")
    print(f"Message: {message}")


# Run program
if __name__ == "__main__":
    main()