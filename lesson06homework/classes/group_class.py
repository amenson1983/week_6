from lesson06homework.classes.fakultet_class import Facultet



class Group():
    def __init__(self, group1=[], group2=[]):
        self.__1 = group1
        self.__2 = group2

    def add_to_group1(self, student):
        self.__1.append(student)

    def add_to_group2(self, student):
        self.__2.append(student)

    def get_1(self):
        return self.__1

    def get_2(self):
        return self.__2

    def __str__(self):
        return f" {self.get_1()}, {self.get_2()}"

# тут будут операции с листом и вычислениями по группе