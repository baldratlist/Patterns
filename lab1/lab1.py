"""Assignment1"""
from __future__ import annotations
from typing import List
from datetime import date, datetime


class Student:
    """This class represents student object
    Attributes:
        full_name (str): Full name of the student.
        address (str): Student's adress.
        phone_number (str): student's number.
    """

    def __init__(self,
                 full_name: str,
                 address: str,
                 phone_number: str,
                 email: str) -> None:
        """Student initializer"""
        self.full_name = full_name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.average_mark = 0.0
        self.courses: List[Course] = []

    def taken_courses(self) -> List[Course] | None:
        """Selected courses
        Args:
            courses (Course): Course to be enrolled.
        Returns:
            self.courses
        """

        return self.courses

    def enroll(self, course: Course) -> None:
        """Stands for enrolling current student into course
        Args:
            course (Course): Course to be enrolled.
        Returns:
            None.
        """

        if course in self.courses:
            print(self.full_name, " currently enroll this course")
        else:
            self.courses.append(course)
            print(self.full_name, " enrolled this course")

    def unenroll(self, course) -> None:
        """Stands for unenrolling current student into course
        Args:
            course (Course): Course to be unenrolled.
        Returns:
            None.
        """

        if course not in self.courses:
            print(self.full_name, " currently unenrolled this course")
        else:
            self.courses.remove(course)
            print(self.full_name, " unenrolled this course")


class CourseProgress:
    """This class represents course progress
    Attributes:
        received_marks (dict): Marks received by a student
    """

    def __init__(self,
                 received_marks: dict
                 ) -> None:
        """CourseProgress initializer"""
        self.received_marks = received_marks
        self.visited_lectures = 0
        self.completed_assigments = {}
        self.notes = {}

    def get_progress_to_date(self, date: date) -> float:
        """Progress to date
        Args:
            date (datetime): Current date by which to look for marks.
        Returns:
            The sum of points is divided by the number of grades before that date.
        """

        assignments = [value for key,
                       value in self.completed_assigments.items() if key <= date]
        marks = []
        for assignment in assignments:
            marks.append(assignment.get('mark'))
        return sum(marks) / len(marks)

    def get_final_mark(self) -> None:
        """Progress to final
        Args:
            None.
        Returns:
            The sum of points is divided by the final number of marks.
        """

        assignments = [value for key,
                       value in self.completed_assigments.items()]
        marks = []
        for assignment in assignments:
            marks.append(assignment.get('mark'))
        return sum(marks) / len(marks)

    def fill_notes(self, date: date, note: str) -> None:
        """A note for the date is attached
        Args:
            date (date): Date of adding the note
            note (str): Note that is attached
        Returns:
            None.
        """

        self.notes.update({date: note})

    def remove_note(self, date: date):
        """A note for the date is deleted
        Args:
            date (date): Date to delete the note
        Returns:
            None.
        """

        del self.notes[date]


class Course:
    """This class represents course object
    Attributes:
        title (str): Tittle of the course
        start_date (datetime): Start date of the course
        end_date (datetime): End date of the course
        description (str): Description of the course
    """
    LIMIT = 30

    def __init__(self,
                 title: str,
                 start_date: datetime,
                 end_date: datetime,
                 description: str
                 ) -> None:
        """Course initializer"""
        self.title = title
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.lectures = []
        self.assigments = []
        self.students: List[Student] = []

    def add_student(self, student: Student) -> None:
        """Stands for enrolling current student into course
        Args:
            student (Student): Student to be enrolled.
        Returns:
            None.
        """

        if len(self.students) < Course.LIMIT:
            self.students.append(student)
            student.enroll(course=self)
        else:
            print("Limit has been exeeded")

    def remove_student(self, student: Student) -> None:
        """Stands for enrolling uncurrent student into course
        Args:
            student (Student): Student to be unenrolled.
        Returns:
            None.
        """

        self.students.remove(student)
        student.unenroll(course=self)


class Professor:
    """This class represents course object
    Attributes:
        name (str): Name of the professor.
        address (str): Professor's address
        phone_number (str): Professor's phone number
        email (str): Professor's email
        salary (float): Professor's salary
    """

    def __init__(self,
                 name: str,
                 address: str,
                 phone_number: str,
                 email: str,
                 salary: float) -> None:
        """Professor initializer"""
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.salary = salary

    def check_assigment(self, assignment: dict):
        """Сhecking the task and assessment
        Args:
            assignment (dict): The task to be checked
        Returns:
            None.
        """

        if assignment.is_done:
            print("Assignment is done. You can get your mark: 5.")
        else:
            print("Assignment isn't done. You can't get your mark.")

def main():
    """main function"""
    professor1 = Professor("Bogdan", "Tarnavskogo",
                           "291-302-0543", "someProfessor@gmail.com", 5000)
    print(vars(professor1))
# create 2 students
    vstudent = Student(full_name="Maks Semenenko",
                       address="Zagrebelnogo 34",
                       phone_number="067644244",
                       email="makssem@gmail.com")
    vstudent2 = Student(full_name="Maks Semenenko2",
                        address="Zagrebelnogo 44",
                        phone_number="0971275232",
                        email="makssem2@gmail.com")
# create course
    design_patterns = Course("DesignPatterns",
                             date(2022, 10, 10),
                             date(2023, 10, 10),
                             "DesignPatterns")
    print(vars(design_patterns))
# create DesignPatterns Progress and check methods of it;
    design_patterns_progress = CourseProgress(received_marks={})
# create new note
    design_patterns_progress.fill_notes(date(2022, 10, 11), "1231")
    print(vars(design_patterns_progress))
# remove this note
    design_patterns_progress.remove_note(date(2022, 10, 11))
    print(vars(design_patterns_progress))
# check methods of Course class
# /add new student to course
    design_patterns.add_student(vstudent)
# add another one, but limit 1 stop adding;
    design_patterns.add_student(vstudent2)
# limit test
    #design_patterns.add_student(vstudent2)
# removing of student
# Student methods
    vstudent2.unenroll(design_patterns)
    vstudent2.enroll(design_patterns)

    #help(Student)

if __name__ == "__main__":
    main()