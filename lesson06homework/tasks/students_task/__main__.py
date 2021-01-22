from lesson06homework.tasks.students_task.studentS_class import Student1
from lesson06homework.tasks.students_task.student_with_average_class import Student_AV

def get_menu_choice_():
    print('_____________________________')
    print('1. Show IT students')
    print('2. Show Management students')
    print('3. Show IT faculty students by course ')
    print('4. Show Management faculty students by course')
    print('5. Students younger than pointed year')
    print('6. List of group with mark higher than 4.5')
    print('7. Quit')
    choice = int(input('Please make a choice: '))
    while choice < 1 or choice > 7:
        choice = int(input('Please make a choice: '))
    return choice

show_it_ = 1
show_management = 2
it_by_course = 3
manag_by_course = 4
stud_year = 5
group_mark = 6
quit_ = 7
filename = 'bin1.dat'



def main():
    student = Student1()
    stud_list = student.get_list_from_file_in_one_row_CSV()
    students_list = []
    for i in range(0,len(stud_list)):
        students_list.append(stud_list[i])

    choice = 0
    while choice != quit_:
        choice = get_menu_choice_()
        if choice == show_it_:
            for i in range(0, len(stud_list)):
                student.get_student_data(students_list[i])
                student.print_it_students()
        elif choice == show_management:
            for i in range(0, len(stud_list)):
                student.get_student_data(students_list[i])
                student.print_management_students()
        elif choice == it_by_course:
            for i in range(0, len(stud_list)):
                student.get_student_data(students_list[i])
                student.print_it_course_stud()
        elif choice == manag_by_course:
            for i in range(0, len(stud_list)):
                student.get_student_data(students_list[i])
                student.print_management_course_stud()
        elif choice == stud_year:
            year_tar = int(input("Put the target year: "))
            for i in range(0, len(stud_list)):
                student.get_student_data(students_list[i])
                student.print_birthyear_students(year_tar)
        elif choice == group_mark:
            for i in range(0, len(stud_list)):
                student.get_student_data(students_list[i])
                student.group_list_aver_mark()
        #    save_items_to_bin(my_items)
   # save_items_to_bin(my_items)

if __name__ == '__main__':
    main()






