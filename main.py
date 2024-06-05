class Teacher:
    teachers_dict = {}

    def __init__(self, name, education, experience):
        self.__name = name
        self.__education = education
        self.__experience = experience
        Teacher.teachers_dict[self.__name] = [self.__education, self.__experience]

    def get_name(self):
        return self.__name

    def get_education(self):
        return self.__education

    def get_experience(self):
        return self.__experience

    def set_experience(self, experience):
        self.__experience = experience
        Teacher.teachers_dict[self.__name][1] = experience
        return True

    def get_teacher_data(self):
        return f"{self.__name}, образование {self.__education}, опыт работы {self.__experience}"

    def add_mark(self, name, mark):
        return f"{self.__name} поставил оценку {mark} студенту {name}"

    def remove_mark(self, name, mark):
        return f"{self.__name} удалил оценку {mark} студенту {name}"

    def give_a_consultation(self, ed_class):
        return f"{self.__name} провел консультацию в классе {ed_class}"

    def fire_teacher(self):
        if self.__name in Teacher.teachers_dict.keys():
            self.teachers_dict.pop(self.__name)
            return f"Учитель {self.__name} был уволен!"
        else:
            return f"Учителя {self.__name} уже уволили!"


class DisciplineTeacher(Teacher):
    def __init__(self, name, education, experience, discipline, job_title):
        super().__init__(name, education, experience)
        self.__discipline = discipline
        self.__job_title = job_title

    def get_discipline(self):
        return self.__discipline

    def get_job_title(self):
        return self.__job_title

    def set_job_title(self, job_title):
        self.__job_title = job_title
        return True

    def get_teacher_data(self):
        return (f"{super().get_name()}, образование {super().get_education()}, опыт работы {super().get_experience()}.\n"
                f"Предмет {self.__discipline}, должность {self.__job_title}")

    def add_mark(self, name, mark):
        return (f"{super().get_name()} поставил оценку {mark} студенту {name}.\n"
                f"Предмет {self.__discipline}")

    def remove_mark(self, name, mark):
        return (f"{super().get_name()} удалил оценку {mark} студенту {name}.\n"
                f"Предмет {self.__discipline}")

    def give_a_consultation(self, ed_class):
        return (f"{super().get_name()} провел консультацию в классе {ed_class}.\n"
                f"По предмету {self.__discipline} как {self.__job_title}")
