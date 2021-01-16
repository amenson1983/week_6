import logging

from lesson06homework.classes.exceptions_class import StudentException


class Student:
    def __init__(self, id = None, fio = None, birthday = None, birthmonth = None, birthyear = None, adress = None, phone = None, marks = None):
        self.__birthyear = birthyear
        self.__birthmonth = birthmonth
        self.__marks = marks
        self.__phone = phone
        self.__adress = adress
        self.__birthday = birthday
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
    def set_birthmonth(self,birthmonth):
        self.__birthmonth = birthmonth
    def set_birthyear(self, birthyear):
        self.__birthyear = birthyear
    def set_birthday(self, birthday):
        self.__birthday = birthday
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
    def get_marks(self):
        return self.__marks
    def get_phone(self):
        return self.__phone
    def get_adress(self):
        return self.__adress
    def get_birthday(self):
        return self.__birthday
    def get_birthmonth(self):
        return self.__birthmonth
    def get_birthyear(self):
        return self.__birthyear
    def get_fio(self):
        return self.__fio
    def get_id(self):
        return self.__id
    def __str__(self):
        return f" {self.get_id()}, {self.get_fio()}, {self.get_marks()}, {self.get_phone()}, {self.get_adress()}, {self.get_birthday()}, {self.get_birthmonth()}, {self.get_birthyear()}"
    def __repr__(self):
        return f"Student: {self.get_id()}, {self.get_fio()}, {self.get_marks()}, {self.get_phone()}, {self.get_adress()}, , {self.get_birthday()}, {self.get_birthmonth()}, {self.get_birthyear()}"
    def show(self):
        print(self.get_id())
        print(self.get_fio())
        print(self.get_birthday())
        print(self.get_birthmonth())
        print(self.get_birthyear())
        print(self.get_adress())
        print(self.get_phone())
        print(self.get_marks())
