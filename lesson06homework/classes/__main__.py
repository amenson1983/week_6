from lesson06homework.classes.course_class import Course
from lesson06homework.classes.group_class import Group
from lesson06homework.classes.marks_class import Marks
from lesson06homework.classes.student_class import Student

if __name__ == '__main__':
 filename = 'students.csv'
 students = Student()
 group_it = Group()
 group_management = Group()
 list_ = students.get_list_from_file_in_one_row_CSV()
 student1 = Student(list_[0][0], list_[0][1], list_[0][2], list_[0][3], list_[0][4], list_[0][5])
 student2 = Student(list_[1][0], list_[1][1], list_[1][2], list_[1][3], list_[1][4], list_[1][5])
 student3 = Student(list_[2][0], list_[2][1], list_[2][2], list_[2][3], list_[2][4], list_[2][5])

 group_it.add_to_it(student1)
 group_it.add_to_it(student3)
 group_management.add_to_management(student2)
 print('List of IT faculty students: ', group_it.get_it(),'\nList of Management faculty students: ', group_management.get_management())

 course = Course()
 course.add_to_course_1(student1)
 course.add_to_course_2(student2)
 course.add_to_course_3(student3)
 print('List of 1 course students: ', course.get_course_1(),'\nList of 2 course students: ',  course.get_course_2(),'\nList of 3 course students: ',  course.get_course_3())




