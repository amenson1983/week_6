class Student1():
    def __init__(self, id=None, fio=None, birthday=None, birthmonth=None, birthyear=None, adress=None, phone=None, faculty=None, course=None, group=None,
                 german=None, english=None, management=None, programming=None, math=None):
        self.__group = group
        self.__course = course
        self.__faculty = faculty
        self.__birthyear = birthyear
        self.__birthmonth = birthmonth
        self.__phone = phone
        self.__adress = adress
        self.__birthday = birthday
        self.__fio = fio
        self.__id = id
        self.__german = german
        self.__english = english
        self.__management = management
        self.__programming = programming
        self.__math = math

    def set_phone(self, phone):
        self.__phone = phone


    def set_adress(self, adress):
        self.__adress = adress

    def set_birthmonth(self, birthmonth):
        self.__birthmonth = birthmonth

    def set_birthyear(self, birthyear):
        self.__birthyear = birthyear

    def set_birthday(self, birthday):
        self.__birthday = birthday

    def set_fio(self, fio):
        self.__fio = fio

    def set_faculty(self, faculty):
        self.__faculty = faculty

    def set_course(self, course):
        self.__course = course

    def set_group(self, group):
        self.__group = group

    def set_id(self, id):
        self.__id = id
    def set_german(self,value):
            self.__german = value

    def set_english(self,value):
            self.__english = value

    def set_management(self,value):
            self.__management = value

    def set_programming(self,value):
            self.__programming = value
    def set_math(self,value):
            self.__math = value

    def get_phone(self):
        return self.__phone

    def get_adress(self):
        return self.__adress

    def get_birthday(self):
        return self.__birthday

    def get_birthmonth(self):
        return self.__birthmonth

    def get_birthyear(self):
        return self.__birthyear

    def get_fio(self):
        return self.__fio

    def get_id(self):
        return self.__id

    def get_faculty(self):
        return self.__faculty

    def get_course(self):
        return self.__course

    def get_group(self):
        return self.__group
    def get_math(self):
        return self.__math

    def get_programming(self):
        return self.__programming

    def get_german(self):
        return self.__german

    def get_english(self):
        return self.__english

    def get_management(self):
        return self.__english

    def get_student_data(self, student):
        i = 0
        self.set_id(student[i])
        self.set_fio(student[i+1])
        self.set_birthday(student[i+2])
        self.set_birthmonth(student[i + 3])
        self.set_birthyear(student[i + 4])
        self.set_adress(student[i + 5])
        self.set_phone(student[i + 6])
        self.set_faculty(student[i + 7])
        self.set_course(student[i+8])
        self.set_group(student[i + 9])
        self.set_german(student[i + 10])
        self.set_english(student[i + 11])
        self.set_management(student[i + 12])
        self.set_programming(student[i + 13])
        self.set_math(student[i + 14])

    def show(self):
        print('Student`s Id: ', self.get_id())
        print('Student`s FIO: ', self.get_fio())
        print('Student`s birthday: ', self.get_birthday())
        print('Student`s birthmonth: ', self.get_birthmonth())
        print('Student`s birthyear: ', self.get_birthyear())
        print('Student`s adress: ', self.get_adress())
        print('Student`s phone: ', self.get_phone())
        print('Student`s faculty: ', self.get_faculty())
        print('Student`s course: ', self.get_course())
        print('Student`s group: ', self.get_group())
        print('Student`s german mark: ', self.get_german())
        print('Student`s english mark: ', self.get_english())
        print('Student`s programming mark: ', self.get_programming())
        print('Student`s management mark: ', self.get_management())
        print('Student`s math mark: ', self.get_math())
        print('Student`s average mark: ', self.aver_mark())
    def aver_mark(self):
        average = float((int(self.get_german()) + int(self.get_english()) + int(self.get_programming()) + int(
            self.get_management()) + int(self.get_math()))/5)
        return average

    def get_list_from_file_in_one_row_CSV(filename="students.csv"):
        list_stud = []
        with open("students.csv", "r") as myfile:
            for line in myfile:
                entry = line.rstrip().split(";")
                list_stud.append(entry)
        return list_stud
    def print_it_students(self):
        if self.get_faculty() == 'it':
            print('Student`s FIO: ', self.get_fio())
    def print_management_students(self):
        if self.get_faculty() == 'management':
            print('Student`s FIO: ', self.get_fio())

    def print_it_course_stud(self):
        if self.get_faculty() == 'it' and int(self.get_course()) == 1:
            print('Course 1 student`s FIO: ', self.get_fio())
        elif self.get_faculty() == 'it' and int(self.get_course()) == 2:
            print('Course 2 student`s FIO: ', self.get_fio())
        elif self.get_faculty() == 'it' and int(self.get_course()) == 3:
            print('Course 3 student`s FIO: ', self.get_fio())
        elif self.get_faculty() == 'it' and int(self.get_course()) == 4:
            print('Course 4 student`s FIO: ', self.get_fio())
        elif self.get_faculty() == 'it' and int(self.get_course()) == 5:
            print('Course 5 student`s FIO: ', self.get_fio())


