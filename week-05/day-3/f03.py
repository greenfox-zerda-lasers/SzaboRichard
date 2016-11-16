# Write a Person class that have a name and a birth_date property
# It should raise an error of the birthdate is less than 0 or more than 2016

class Person:

    def __init__(self, name, birthday):
        self.name = name

        if birthday > 0 and birthday < 2016:
            self.birthday = birthday
        else:
            raise ValueError

# ember = Person("name", 0)
# print(ember.birthday )
