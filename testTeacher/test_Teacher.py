import unittest
from main import Teacher


class MyTestCase(unittest.TestCase):
    teacher = Teacher("test_name", "test_education", "test_experience")

    def test_1_init(self):
        self.assertEqual(len(Teacher.teachers_dict), 1)
        self.assertEqual(Teacher.teachers_dict, {'test_name': ['test_education', 'test_experience']})
