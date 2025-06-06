class Student:
    def __init__(self, name, student_id, age):
        self.name = name
        self.student_id = student_id
        self.age = age
        self.__grades = []

    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grades.append(grade)

    def calculate_average(self):
        return sum(self.__grades) / len(self.__grades)

    def get_student_info(self):
        return {
            "Name": self.name,
            "ID": self.student_id,
            "Age": self.age,
            "Average Grade": self.calculate_average()
        }

student1 = Student("Ержан", "1", 20)
student2 = Student("Андрюха", "2", 22)

student1.add_grade(85)
student1.add_grade(90)
student2.add_grade(18)
student2.add_grade(82)
student1.add_grade(65)

print(student1.get_student_info())
print(student2.get_student_info())
