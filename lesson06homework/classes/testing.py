#Создать классы, спецификации которых приведены ниже.

#Определить конструкторы и методы(свойства) set(), get(), __str__().

#Определить дополнительно методы в классе, создающем массив объектов.

#Задать критерий выбора данных и вывести эти данные на консоль, прочитать и записать результат из файла

#В каждом классе, обладающем информацией, должно быть объявлено несколько конструкторов.

#1. 4Student: id, ФИО, Дата рождения, Адрес, Телефон, Оценки (5)  1Факультет, 2Курс, 3Группа.
#Создать массив объектов. Вывести:
#a) список студентов заданного факультета;
#b) списки студентов для каждого факультета и курса;
#c) список студентов, родившихся после заданного года;
#d) список учебной группы средний бал выше 4.5 .
from lesson06homework.classes.fakultet_class import Facultet
from lesson06homework.classes.group_class import Group
from lesson06homework.classes.student_class import Student

if __name__ == '__main__':
    student1 = Student('123', 'Turchyn Andrey', 16,5,1983, '1, Zamkova str, Zhytomir, 4, fl', '+380989922947', 5.0)
    student2 = Student('321', 'Turchyna Natali', 10, 8, 1982, '1, Zamkova str, Zhytomir, 4 fl', '+380989922947',4.9)
    group1 = Group()
    group2 = Group()
    group2.add_to_group2(student1)
    group2.add_to_group2(student2)
    group2.get_2()
    print(group2.__str__())




