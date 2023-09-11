# Python module for copying objects
import copy

# Importing application internal classes
from grades import Grades
from grade_weights import GradeWeights


class GradeCalculator:
    """
    Calculates the overall course grade for ENPM611.
    """

    @staticmethod
    def calculate_course_percentage(grades: Grades, weights: GradeWeights) -> float:
        """"
        Calculates the percentace of the overall course
        grade. If not all grades have been set yet, this
        function returns None.
        """
        if grades.quiz_1 is None or grades.quiz_2 is None or grades.midterm is None or grades.project is None or grades.final is None:
            print("Can't calculate final grade without all assignments graded")
            return None
        else:
            quizzes_part = ((grades.quiz_1 + grades.quiz_2) / 2) * weights.quizzes
            midterm_part = grades.midterm * weights.midterm
            project_part = grades.project * weights.project
            final_part = grades.final * weights.final
            course_grade = quizzes_part + midterm_part + project_part + final_part
            return course_grade

    @staticmethod
    def calculate_optimistic_course_percentage(grades: Grades, weights: GradeWeights) -> float:
        """
        Calculates the course percentage grade assuming that
        all assignments that have not been completed receive 100%. 
        """

        # Need to create a copy so that we don't overwrite
        # the values of the Grades object that was passed in
        optimistic_grades: Grades = copy.copy(grades)

        # Now we are setting all grades that have not been set
        # to the maximum percentage of 100%
        if optimistic_grades.quiz_1 is None:
            optimistic_grades.quiz_1 = 1
        if optimistic_grades.quiz_2 is None:
            optimistic_grades.quiz_2 = 1
        if optimistic_grades.midterm is None:
            optimistic_grades.midterm = 1
        if optimistic_grades.project is None:
            optimistic_grades.project = 1
        if optimistic_grades.final is None:
            optimistic_grades.final = 1

        # Let the basic calculation function take care of actually
        # calculating the percentage grade
        return GradeCalculator.calculate_course_percentage(optimistic_grades, weights)

    @staticmethod
    def calculate_minimum_average_for_grade_a(grades=Grades, weights=GradeWeights) -> float:
        """
        Calculates the minimum average points for all yet ungraded assignments to still get an A in class 
        """
        # Need to create a copy so that we don't overwrite
        # the values of the Grades object that was passed in
        current_grades: Grades = copy.copy(grades)

        # The total weight percentage of the ungraded assignments
        ungraded_weight = 0

        # Setting all grades that have not been set to zero and 
        # add the weights of all the ungraded assignments
        if current_grades.quiz_1 is None:
            ungraded_weight += weights.quizzes
            current_grades.quiz_1 = 0
        if current_grades.quiz_2 is None:
            ungraded_weight += weights.quizzes
            current_grades.quiz_2 = 0
        if current_grades.midterm is None:
            ungraded_weight += weights.midterm
            current_grades.midterm = 0
        if current_grades.project is None:
            ungraded_weight += weights.project
            current_grades.project = 0
        if current_grades.final is None:
            ungraded_weight += weights.final
            current_grades.final = 0

        temporary_grade = GradeCalculator.calculate_course_percentage(current_grades, weights)
        # The minimum average points for all yet ungraded
        # assignments to still get an A in class

        # Current grade is enough to get an A
        if temporary_grade >= 0.91:
            return 0
        # Impossible to get an A according to the current grade
        elif (0.91 - temporary_grade) / ungraded_weight > 1:
            return -1
        # Sill have the possibility to get an A
        else:
            return (0.91 - temporary_grade) / ungraded_weight


    @staticmethod
    def calculate_letter_grade(percentage_grade: float) -> str:
        """
        Calculate the letter grade giving a percentage grade.
        The cutoffs for letter grades can be found in the introductory slides
        and in the syllabus.
        """

        # Avoid exception due to missing value
        if percentage_grade is None:
            return None

        # Return the letter that corresponds to
        # the percentage cutoff
        if percentage_grade >= 0.91:
            return 'A'
        elif percentage_grade >= 0.8:
            return 'B'
        elif percentage_grade >= 0.74:
            return 'C'
        elif percentage_grade >= 0.6:
            return 'D'
        else:
            return 'F'
