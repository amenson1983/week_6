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
    student = Student()
    list_of_students = student.get_list_from_file_in_one_row_CSV()
    years = []
    for student in list_of_students:
        years.append(student[4])
    print(years)
    year_indicator = int(input('Put the year to find elder students: '))
    for i in range(0,len(years)):
        if int(years[i]) < year_indicator:
            print(list_of_students[i])




