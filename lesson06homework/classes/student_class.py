import logging

from lesson06homework.classes.exceptions_class import StudentException


class Student:
    def __init__(self, id = None, fio = None, birthdate = None, adress = None, phone = None, marks = None):
        self.__marks = marks
        self.__phone = phone
        self.__adress = adress
        self.__birthdate = birthdate
        self.__fio = fio
        self.__id = id
    def set_marks(self, value):
        if value > 0 and value < 5:
            self.__marks = value
            logging.info("Marks input" + str(value))
        else:
            self.__marks = None
            str_err = "Error price, value < 0 or bigger than 5"
            print(str_err)
            raise StudentException(str_err)
    def set_phone(self,phone):
        if phone > 0 and len(phone) == 13:
            self.__marks = phone
            logging.info("Marks input" + "+" + str(phone))
        else:
            self.__marks = None
            str_err = "Phone is not in 380_________ format"
            print(str_err)
            raise StudentException(str_err)
    def set_adress(self, adress):
        self.__adress = adress
    def set_birthdate(self,birthdate):
        self.__birthdate = birthdate
    def set_fio(self, fio):
        self.__fio = fio
    def set_id(self, id):
        if id > 0 and len(id) == 8:
            self.__id = id
            logging.info("Marks input" + "+" + str(id))
        else:
            self.__id = None
            str_err = "ID is not in 8 digit format"
            print(str_err)
            raise StudentException(str_err)
    def get_marks:
    def get_phone:
    def get_adress:
    def get_birthdate:
    def get_fio:
    def get_id: