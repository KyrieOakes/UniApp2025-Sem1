import random
from uuid import uuid4

class Subject:
    """
    A class to represent a subject.

    Each subject has:
    - id: a 3-digit string
    - mark: an integer between 1 and 100
    - grade: based on mark
    """

    def __init__(self, id: str = None, mark: int = None):
        # Generate subject ID: 3-digit string (e.g., '001', '298')
        if id is None:
            random_number = uuid4().int % 1000
            self.id = f"{random_number:03d}"
        else:
            self.id = id

        # Generate or assign mark between 1 and 100
        if mark is None:
            random_mark = random.randint(1, 100)
            self.mark = random_mark
        else:
            self.mark = mark

        # Calculate grade based on the mark
        self.grade = self._calculate_grade(self.mark)

    @staticmethod
    def _calculate_grade(mark: int) -> str:
        """
        Return a grade string based on the given mark.
        HD: High Distinction (85+)
        D:  Distinction (75–84)
        C:  Credit (65–74)
        P:  Pass (50–64)
        F:  Fail (<50)
        """
        if mark >= 85:
            return 'HD'
        elif mark >= 75:
            return 'D'
        elif mark >= 65:
            return 'C'
        elif mark >= 50:
            return 'P'
        else:
            return 'F'

    def to_dict(self) -> dict:
        """
        Convert the subject to dictionary format for saving.
        """
        return {
            'id': self.id,
            'mark': self.mark,
            'grade': self.grade
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Subject':
        """
        Create a Subject object from dictionary data.
        """
        return cls(id=data['id'], mark=data['mark'])
