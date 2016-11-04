# Create a new class called `Person` that has a first_name and a last_name (takes it in it's constructor)
# It should have a `greet` method that prints it's full name

# Create a `Student` class that is the child class of `Person`
# it should have a method to add grades
# it should have a `salute` method that prints it's full name and the average of it's grades as well

class Person():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = first_name + " " + last_name

    def greet(self):
        return self.first_name + self.last_name

class Student(Person):
    grades = []

    def add_grades(self, grade):
        if grade >= 1 and grade <= 5:
            self.grades += [grade]
        return self.grades

    def salute(self):
        summ = 0
        for i in self.grades:
            summ += i
        print(summ, self.grades)
        summ = summ / len(self.grades)
        print('Nev:', self.full_name,' Jegyek: ', summ)

tanulo = Student("Mekk","Elek")
tanulo.add_grades(5)
tanulo.add_grades(5)
tanulo.add_grades(4)
tanulo.add_grades(4)
tanulo.add_grades(3)
tanulo.add_grades(2)
tanulo.salute()
