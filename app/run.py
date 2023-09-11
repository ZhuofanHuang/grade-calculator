

from grades import Grades
from grade_weights import GradeWeights
from grade_calculator import GradeCalculator

# This runs the grade calculation.

# Instatiate Grade and Weights objects
my_grades = Grades()
weights = GradeWeights()

# Set grades achieved so far
"""test 1"""
my_grades.quiz_1 = 0.78 # the first quiz
"""test 2"""
# my_grades.quiz_1 = 0 # the first quiz
# my_grades.quiz_2 = 1 # the second quiz
# my_grades.midterm = 1 # the midterm
# my_grades.project = 1 # in the project
# my_grades.final = 1 # in the final
"""test 3"""
# my_grades.quiz_1 = 1 # the first quiz
# my_grades.quiz_2 = 1 # the second quiz
# my_grades.midterm = 1 # the midterm
# my_grades.final = 1 # in the final



# Print out the grades to console
print(my_grades)

# Calculate course grade based on the grades set above
percentage_grade = GradeCalculator.calculate_course_percentage(my_grades, weights)
if percentage_grade is None:
    print("Can't calculate overall course grade without all individual grades.")
else:
    letter_grade = GradeCalculator.calculate_letter_grade(percentage_grade)
    print(f'The letter grade with an overall {percentage_grade*100}% is {letter_grade}')

# Calculate the grade assuming that all assignmets not turned in yet, will be 100%
optimistic_percentage_grade = GradeCalculator.calculate_optimistic_course_percentage(my_grades, weights)
optimistic_letter_grade = GradeCalculator.calculate_letter_grade(optimistic_percentage_grade)
print(f'If all other assignments are 100%, the overall course would be {optimistic_percentage_grade*100}%, which is a {optimistic_letter_grade}')

# Calculates the minimum average points for all yet ungraded assignments to still get an A in class
minimum_average_for_grade_a = GradeCalculator.calculate_minimum_average_for_grade_a(my_grades, weights)
if minimum_average_for_grade_a ==-1:
    print('It is impossible for you to get an A in this class')
elif minimum_average_for_grade_a == 0:
    print('You can definitely get an A grade in this course')
else:
    print(f'With current individual assignment grades, the minimum average points for all yet ungraded assignments to '
      f'still get an A in class is {minimum_average_for_grade_a*100}')
