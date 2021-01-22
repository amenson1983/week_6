from lesson06homework.tasks.students_task.studentS_class import Student1


class Student_AV(Student1):
    def __init__(self, average=None):
        self.__average = average

    def get_average(self):
        return self.__average


    def show1(self):
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
        print('Student`s average mark: ', self.get_average())
