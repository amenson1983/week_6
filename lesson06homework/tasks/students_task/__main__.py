from lesson06homework.tasks.students_task.studentS_class import Student1
from lesson06homework.tasks.students_task.student_with_average_class import Student_AV

def get_menu_choice_():
    print('_____________________________')
    print('1. Show IT students')
    print('2. Show Management students')
    print('3. Show IT faculty students by course ')
    print('4. Clear bin')
    print('5. Quit')
    choice = int(input('Please make a choice: '))
    while choice < 1 or choice > 5:
        choice = int(input('Please make a choice: '))
    return choice

show_it_ = 1
show_management = 2
facul_course = 3
clear_ = 4
quit_ = 5
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
        elif choice == facul_course:
            for i in range(0, len(stud_list)):
                student.get_student_data(students_list[i])
                student.print_it_course_stud()
        #elif choice == :
            #sum = load_sum(filename_sum)
           # print('Amount to pay: ',sum, "UAH")
      #  elif choice == clear_:
        #    clear()
        #    save_items_to_bin(my_items)
   # save_items_to_bin(my_items)

if __name__ == '__main__':
    main()






