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

    def set_german(self):
        value = int(input('Input mark for German:'))
        if value > 0 and value <= 5:
            self.__german = value
            logging.info("Marks input" + str(value))
        else:
            self.__german = None
            str_err = "Error price, value < 0 or bigger than 5"
            print(str_err)
            raise StudentException(str_err)

    def set_english(self):
        value = int(input('Input mark for English:'))
        if value > 0 and value <= 5:
            self.__english = value
            logging.info("Marks input" + str(value))
        else:
            self.__english = None
            str_err = "Error price, value < 0 or bigger than 5"
            print(str_err)
            raise StudentException(str_err)
    def set_management(self):
        value = int(input('Input mark for Management:'))
        if value > 0 and value <= 5:
            self.__management = value
            logging.info("Marks input" + str(value))
        else:
            self.__management = None
            str_err = "Error price, value < 0 or bigger than 5"
            print(str_err)
            raise StudentException(str_err)

    def set_programming(self):
        value = int(input('Input mark for Programming:'))
        if value > 0 and value <= 5:
            self.__programming = value
            logging.info("Marks input" + str(value))
        else:
            self.__programming = None
            str_err = "Error price, value < 0 or bigger than 5"
            print(str_err)
            raise StudentException(str_err)
    def set_math(self):
        value = int(input('Input mark for Math:'))
        if value > 0 and value <= 5:
            self.__math = value
            logging.info("Marks input" + str(value))
        else:
            self.__math = None
            str_err = "Error price, value < 0 or bigger than 5"
            print(str_err)
            raise StudentException(str_err)

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

