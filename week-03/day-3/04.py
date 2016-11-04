# Create a student Class
# that has a method `add_grade`, that takes a grade from 1 to 5
# an other method `get_average`, that returns the average of the
# grades

class Student():
    grades = []
    def add_grade(self, grade):
        if grade >= 1 and grade <= 5:
            self.grades.append(grade)
        else:
            print("Hibás jegyet adott meg")

    def get_average(self):
        summ = 0
        for i in self.grades:
            summ += i
        return summ / len(self.grades)

tanulo = Student()
tanulo.add_grade(5)
tanulo.add_grade(5)
tanulo.add_grade(5)
tanulo.add_grade(4)

print('a tanulo atlaga: ', tanulo.get_average())
