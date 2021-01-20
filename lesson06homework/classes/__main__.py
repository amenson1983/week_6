from lesson06homework.classes.student_class import Student

if __name__ == '__main__':
 filename = 'students.csv'
 students = Student()
 list_ = students.get_list_from_file_in_one_row_CSV()
 for i in range(0,len(list_)):
    print(list_[i])
