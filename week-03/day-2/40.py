students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5}
]
# create a function that takes a list of students,
# then returns how many candies are own by students
# under 10

def students_count_funct (classmates):
    candie = 0
    for i in classmates:
        if i['age'] < 10:
            candie += i['candies']
    print(candie)
    # for k, n in classmates.items():
    #     print (k + V)

students_count_funct(students)
