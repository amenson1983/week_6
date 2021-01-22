import logging

from lesson06homework.classes.exceptions_class import StudentException


class Marks:
    def __init__(self, student_fio=None, math = None, programming = None, management = None, english = None, german = None,
                 marks_list=[]):
        self.__student_fio = student_fio
        self.__german = german
        self.__english = english
        self.__management = management
        self.__programming = programming
        self.__math = math
        self.__markslist = marks_list

    def add(self,student_fio,average=None):
        self.__markslist.append(student_fio)
        self.__markslist.append(average)


    def get_markslist(self):
        return self.__markslist

    def set_german(self,value):
            self.__german = value

    def set_english(self,value):
            self.__english = value

    def set_management(self,value):
            self.__management = value

    def set_programming(self,value):
            self.__programming = value
    def set_math(self,value):
            self.__math = value


    def get_math(self):
        return self.__math

    def get_programming(self):
        return self.__programming

    def get_german(self):
        return self.__german

    def get_english(self):
        return self.__english

    def get_management(self):
        return self.__english

    def find_average(self):
        total_sum = float(self.get_math() + self.get_management() + self.get_programming() + self.get_english() +self.get_german())
        count = 5
        average = float(total_sum/count)
        return average

