import unittest
from main import DisciplineTeacher


class MyTestCase(unittest.TestCase):
    dis_teacher = DisciplineTeacher("test_name", "test_education", "test_experience",
                                    "test_discipline", "test_job_tittle")

    def test_1_init(self):
        self.assertEqual(len(DisciplineTeacher.teachers_dict), 1)

    def test_2_get_discipline(self):
        self.assertEqual(self.dis_teacher.get_discipline(), 'test_discipline')

    def test_3_get_job_title(self):
        self.assertEqual(self.dis_teacher.get_job_title(), 'test_job_tittle')

    def test_4_set_job_title(self):
        self.assertEqual(self.dis_teacher.set_job_title('test_job'), True)
        self.assertEqual(self.dis_teacher.get_job_title(), 'test_job')

    def test_5_get_teacher_data(self):
        self.assertEqual(self.dis_teacher.get_teacher_data(), ('test_name, образование test_education, '
                                                               'опыт работы test_experience.\n'
                                                               'Предмет test_discipline, должность test_job'))

    def test_6_add_mark(self):
        self.assertEqual(self.dis_teacher.add_mark("test", "5"), 'test_name поставил оценку 5 '
                                                                 'студенту test.\nПредмет test_discipline')

    def test_7_remove_mark(self):
        self.assertEqual(self.dis_teacher.remove_mark("test", "5"), 'test_name удалил оценку 5 '
                                                                    'студенту test.\nПредмет test_discipline')

    def test_8_give_a_consultation(self):
        self.assertEqual(self.dis_teacher.give_a_consultation('test_ed_class'),
                         ('test_name провел консультацию в классе test_ed_class.\n'
                          'По предмету test_discipline как test_job'))
