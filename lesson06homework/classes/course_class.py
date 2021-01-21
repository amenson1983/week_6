class Course():
    def __init__(self, course_1=[], course_2=[], course_3=[]):
        self.__course_1 = course_1
        self.__course_2 = course_2
        self.__course_3 = course_3

    def add_to_course_1(self, student):
        self.__course_1.append(student.get_fio())

    def add_to_course_2(self, student):
        self.__course_2.append(student.get_fio())

    def add_to_course_3(self, student):
        self.__course_3.append(student.get_fio())



    def get_course_1(self):
        return self.__course_1

    def get_course_2(self):
        return self.__course_2

    def get_course_3(self):
        return self.__course_3