class Teacher:
    def __init__(self, name, education, experience):
        self.__name = name
        self.__education = education
        self.__experience = experience

    def get_name(self):
        return self.__name

    def get_education(self):
        return self.__education

    def get_experience(self):
        return self.__experience

    def set_experience(self, experience):
        self.__experience = experience
        return True

    def get_teacher_data(self):
        return f"{self.__name}, образование {self.__education}, опыт работы {self.__experience}"

    def add_mark(self, name, mark):
        return f"{self.__name} поставил оценку {mark} студенту {name}"

    def remove_mark(self, name, mark):
        return f"{self.__name} удалил оценку {mark} студенту {name}"

    def give_a_consultation(self, ed_class):
        return f"{self.__name} провел консультацию в классе {ed_class}"