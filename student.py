class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        average = sum(self.marks) / len(self.marks)
        return average > 50

    if __name__ == "__main__":
        student_passed = Student("Anna", [60, 70, 80])
        student_failed = Student("Piotr", [30, 40, 50])

        print(student_passed.name, "passed:", student_passed.is_passed())
        print(student_failed.name, "passed:", student_failed.is_passed())