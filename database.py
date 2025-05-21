import os
import json
from student import Student

FILE_PATH = 'students.data'

class Database:
    """
    This class is used to manage student records using a file-based system.
    It supports basic CRUD operations and some grouping functions.
    """

    def __init__(self, path: str = None):
        # Set file path; use default if not provided
        self.path = path if path is not None else FILE_PATH
        self._make_sure_file_exists()

    def _make_sure_file_exists(self):
        # Create the file if it does not exist
        if not os.path.exists(self.path):
            with open(self.path, 'w') as file_object:
                json.dump([], file_object)

    def _read_all_students(self) -> list:
        # Read and convert all student records from file
        with open(self.path, 'r') as file_object:
            raw_data = json.load(file_object)

        student_list = []

        for single_data in raw_data:
            student_object = Student.from_dict(single_data)
            student_list.append(student_object)

        return student_list

    def _write_all_students(self, student_list: list):
        # Write all student objects to the file
        with open(self.path, 'w') as file_object:
            json.dump([student_object.to_dict() for student_object in student_list], file_object, indent=2)

    def add_student(self, student: Student):
        """
        Add a student to the file.
        Raise error if a student with the same email already exists.
        """
        student_list = self._read_all_students()

        for existing_student in student_list:
            if existing_student.email == student.email:
                raise RuntimeError("Student with this email already exists.")
            
        student_list.append(student)
        self._write_all_students(student_list)


    def get_student_by_email(self, email: str) -> Student:
        """
        Return student with matching email.
        Raise error if not found.
        """
        student_list = self._read_all_students()
        for student_object in student_list:
            if student_object.email == email:
                return student_object
        raise KeyError("Student with the provided email was not found.")


    def get_student_by_id(self, student_id: str) -> Student:
        # Search for student by ID
        student_list = self._read_all_students()
        for student_object in student_list:
            if student_object.id == student_id:
                return student_object
        raise KeyError("Student with the given ID was not found.")

    def update_student(self, student: Student):
        """
        Replace student with same ID.
        Raise error if ID does not exist.
        """
        student_list = self._read_all_students()
        student_updated = False
        for index, existing_student in enumerate(student_list):
            if existing_student.id == student.id:
                student_list[index] = student
                student_updated = True
                break
        if not student_updated:
            raise KeyError("Student with the given ID does not exist.")
        self._write_all_students(student_list)

    def remove_student_by_id(self, student_id: str):
        """
        Remove student by ID.
        Raise error if no student is removed.
        """
        student_list = self._read_all_students()
        new_student_list = []
        for student_object in student_list:
            if student_object.id != student_id:
                new_student_list.append(student_object)
        if len(new_student_list) == len(student_list):
            raise KeyError("Student with the given ID does not exist.")
        self._write_all_students(new_student_list)

    def clear_all(self):
        """
        Delete all students.
        """
        self._write_all_students([])

    def partition_students(self) -> dict:
        """
        Separate students into 'pass' and 'fail' based on passed() result.
        """
        passed_students = []
        failed_students = []
        student_list = self._read_all_students()
        for student_object in student_list:
            if student_object.passed():
                passed_students.append(student_object)
            else:
                failed_students.append(student_object)
        return {
            'pass': passed_students,
            'fail': failed_students
        }

    def group_students_by_grade(self) -> dict:
        """
        Group students by their rounded average grade.
        """
        grouped_students = {}
        student_list = self._read_all_students()
        for student_object in student_list:
            average_score = round(student_object.average_mark())
            average_score_string = str(average_score)
            if average_score_string not in grouped_students:
                grouped_students[average_score_string] = []
            grouped_students[average_score_string].append(student_object)
        return grouped_students

    def list_all(self) -> list:
        """
        Return list of all students.
        """
        return self._read_all_students()
