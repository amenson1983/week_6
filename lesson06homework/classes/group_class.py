from lesson06homework.classes.fakultet_class import Facultet



class Group():
    def __init__(self, it=[], management=[]):
        self.__it = it
        self.__management = management

    def add_to_it(self, student):
        self.__it.append(student.get_fio()) # здесь сформировать список (добавить признаки) с полями из задания, для дальнейшей обработки


    def add_to_management(self, student):
        self.__management.append(student.get_fio()) # здесь сформировать список (добавить признаки) с полями из задания, для дальнейшей обработки


    def get_it(self):
        return self.__it

    def get_management(self):
        return self.__management

    def __str__(self):
        return f" {self.get_it()}, {self.get_management()}"

# тут будут операции с листом и вычислениями по группе