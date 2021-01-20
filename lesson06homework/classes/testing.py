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
from lesson06homework.classes.marks_class import Marks
from lesson06homework.classes.student_class import Student

if __name__ == '__main__':
    student1 = Student('123', 'Turchyn Andrey', 16,5,1983, '1, Zamkova str, Zhytomir, 4, fl', '+380989922947')
    student2 = Student('321', 'Turchyna Natali', 10, 8, 1982, '1, Zamkova str, Zhytomir, 4 fl', '+380989922947')
    group1 = Group()
    group2 = Group()

    group2.add_to_group2(student1)
    group1.add_to_group1(student2)
    x = group2.get_2()
    z = group1.get_1()
    faculty_economy = Facultet()
    faculty_it = Facultet()
    faculty_economy.add_to_economy(student1)
    faculty_it.add_to_it(student2)
    it = faculty_it.get_it()
    print(it)

    marks1 = Marks()
    marks2 = Marks()
    fio = student1.get_fio()
    marks1.set_german()
    marks1.set_english()
    marks1.set_programming()
    marks1.set_management()
    marks1.set_math()
    german = marks1.get_german()
    english = marks1.get_english()
    programming = marks1.get_programming()
    management = marks1.get_management()
    math = marks1.get_math()
    fio_ = student1.get_fio()
    average = marks1.find_average()
    marks1.add(fio_,average)
    markslist = marks1.get_markslist()
    print(markslist)





