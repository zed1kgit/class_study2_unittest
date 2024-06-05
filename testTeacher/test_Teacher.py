import unittest
from main import Teacher


class MyTestCase(unittest.TestCase):
    teacher = Teacher("test_name", "test_education", "test_experience")

    def test_1_init(self):
        self.assertEqual(len(Teacher.teachers_dict), 1)
        self.assertEqual(Teacher.teachers_dict, {'test_name': ['test_education', 'test_experience']})

    def test_2_get_name(self):
        self.assertEqual(self.teacher.get_name(), 'test_name')

    def test_3_get_education(self):
        self.assertEqual(self.teacher.get_education(), 'test_education')

    def test_4_get_experience(self):
        self.assertEqual(self.teacher.get_experience(), 'test_experience')

    def test_5_set_experience(self):
        self.assertEqual(self.teacher.set_experience("test_exp1"), True)
        self.assertEqual(self.teacher.teachers_dict['test_name'][1], 'test_exp1')

    def test_6_get_teacher_data(self):
        self.assertEqual(self.teacher.get_teacher_data(),
                         'test_name, образование test_education, опыт работы test_exp1')

    def test_7_add_mark(self):
        self.assertEqual(self.teacher.add_mark("test", "5"), 'test_name поставил оценку 5 студенту test')

    def test_8_remove_mark(self):
        self.assertEqual(self.teacher.remove_mark("test", "5"), 'test_name удалил оценку 5 студенту test')

    def test_9_give_a_consultation(self):
        self.assertEqual(self.teacher.give_a_consultation('9В'), 'test_name провел консультацию в классе 9В')

    def test_fire_teacher(self):
        self.assertEqual(self.teacher.fire_teacher(), 'Учитель test_name был уволен!')
        self.assertEqual(self.teacher.fire_teacher(), 'Учителя test_name уже уволили!')
