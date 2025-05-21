import re
from uuid import uuid4
from subject import Subject

# Email must be like name@university.com
EMAIL_REGEX = r'^[\w\.]+@university\.com$'

# Password must start with uppercase, then 4+ letters, then 3+ numbers
PASSWORD_REGEX = r'^[A-Z][A-Za-z]{4,}\d{3,}$'

class Student:
    """
    A class to represent a student.

    Each student has:
    - Unique ID
    - Name
    - Email
    - Password
    - List of enrolled subjects

    Supports:
    - Subject enrollment and removal
    - Password change
    - Mark calculation
    - Conversion to/from dictionary format
    """

    def __init__(self, name: str, email: str, password: str, id: str = None, subjects=None):
        # Check if email format is valid
        if not re.match(EMAIL_REGEX, email):
            raise ValueError("Email format is not valid. It must end with @university.com")

        # Check if password format is valid
        if not re.match(PASSWORD_REGEX, password):
            raise ValueError("Password format is not valid.")

        self.id = id if id is not None else self._generate_unique_id()
        self.name = name
        self.email = email
        self.password = password
        self.subjects = subjects if subjects is not None else []  # Empty list by default

    @staticmethod
    def _generate_unique_id() -> str:
        # Generate a random 6-digit number string
        return f"{uuid4().int % 1000000:06d}"

    def enroll(self) -> Subject:
        """
        Enroll the student in a new subject.

        Raises error if already enrolled in 4 subjects.
        """
        if len(self.subjects) >= 4:
            raise RuntimeError("Cannot enroll in more than 4 subjects.")

        new_subject = Subject()
        self.subjects.append(new_subject)
        return new_subject

    def remove_subject(self, subject_id: str):
        """
        Remove a subject by ID from the enrolled list.

        Raises error if the subject is not found.
        """
        new_subject_list = []
        found = False
        for subject_object in self.subjects:
            if subject_object.id != subject_id:
                new_subject_list.append(subject_object)
            else:
                found = True

        if not found:
            raise KeyError("Subject not found with given ID.")

        self.subjects = new_subject_list

    def change_password(self, new_password: str):
        """
        Change the student's password.

        Password must match required format.
        """
        if not re.match(PASSWORD_REGEX, new_password):
            raise ValueError("Password format is not valid.")
        self.password = new_password

    def average_mark(self) -> float:
        """
        Calculate and return the average mark.

        If no subjects, return 0.0.
        """
        if len(self.subjects) == 0:
            return 0.0

        total = 0.0
        for subject_object in self.subjects:
            total += subject_object.mark

        return total / len(self.subjects)

    def passed(self) -> bool:
        """
        Return True if average mark >= 50.
        """
        return self.average_mark() >= 50.0

    def to_dict(self) -> dict:
        """
        Convert student to a dictionary for saving.
        """
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'subjects': [subject_object.to_dict() for subject_object in self.subjects]
        }

    def __str__(self):
        """
        Return a readable string version of the student.
        """
        subject_id_list = [subject_object.id for subject_object in self.subjects]
        return (
            "ID: " + self.id + ", Name: " + self.name + ", Email: " + self.email +
            ", Subjects: " + str(subject_id_list) +
            ", Avg Mark: " + f"{self.average_mark():.2f}" +
            ", Status: " + ("PASS" if self.passed() else "FAIL")
        )

    @classmethod
    def from_dict(cls, data: dict) -> 'Student':
        """
        Create a Student object from dictionary data.
        """
        subject_data_list = data.get('subjects', [])
        subject_objects = []
        for subject_data in subject_data_list:
            subject_objects.append(Subject.from_dict(subject_data))

        return cls(
            name=data['name'],
            email=data['email'],
            password=data['password'],
            id=data['id'],
            subjects=subject_objects
        )
