class Student:
    def __init__(self, name, student_id, age):
        self.name = name
        self.student_id = student_id
        self.age = age
        self.__grades = []  

    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grades.append(grade)
        else:
            print("Invalid grade. Please enter a value between 0 and 100.")

    def calculate_average(self):
        if self.__grades:
            return sum(self.__grades) / len(self.__grades)
        else:
            return 0

    def get_student_info(self):
        return f"Name: {self.name}, ID: {self.student_id}, Age: {self.age}, Average Grade: {self.calculate_average():.2f}"

#Example:
stud1 = Student("Alice", "S001", 20)
stud2 = Student("Bob", "S002", 22)
stud1.add_grade(85)
stud2.add_grade(88)
print(stud1.get_student_info())
print(stud2.get_student_info())