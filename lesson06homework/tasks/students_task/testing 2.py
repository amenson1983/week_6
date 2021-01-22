from lesson06homework.tasks.students_task.studentS_class import Student1

if __name__ == '__main__':
    student = Student1()
    stud_list = student.get_list_from_file_in_one_row_CSV()
    students_list = []
    for i in range(0,len(stud_list)):
        students_list.append(stud_list[i])

    for i in range(0, len(stud_list)):
        print('________________')
        student.get_student_data(students_list[i])
        x = student.aver_mark()
        print('________________')
        student.show()

    tar_faculty = int(input('Put target faculty number:'))
    if tar_faculty == 1:
        for i in range(0, len(stud_list)):
            student.get_student_data(students_list[i])
            student.print_it_students()
    elif tar_faculty == 2:
        for i in range(0, len(stud_list)):
            student.get_student_data(students_list[i])
            student.print_management_students()