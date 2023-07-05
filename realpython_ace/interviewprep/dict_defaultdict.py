from collections import defaultdict
from re import L
from tkinter import N

student_grades = {
    "jack": [80, 90],
    "jill": [85, 20],
}

def get_student_grades(name):
    if name in student_grades:
        return student_grades[name]
    return []

def get_grades_better(name):
    return student_grades.get(name, [])

def get_grades_with_assignment(name):
    if name not in student_grades:
        student_grades[name] = []
    return student_grades[name]

def get_grades_with_assignment_better(name):
    """
    This method will set the default value for
    a given name if it dosen't exist.
    """
    return student_grades.setdefault(name, [])


print(get_grades_with_assignment_better("lol"))
print(student_grades)


def set_grades_naive(name, score):
    """
    Setting a new value in the dictionary, 1
    1. Check to see if the value already exists, update the value
    2. If the value does not exist, use 
    """
    if name in student_grades:
        grades = student_grades[name]
    else:
        student_grades[name] = []
        grades = student_grades[name]
    grades.append(score)
    

def set_grades_better(name, score):
    grades = get_grades_with_assignment_better(name)
    grades.append(score)


# default dict will take one argument with the
# default type to be returned, when nothing is present.
# default dict params - 
# :param default value
# :param initial value - which is a dictionary
student_grades = defaultdict(list, student_grades)

def set_grades_better(name, score):
    student_grades[name].append(score)
