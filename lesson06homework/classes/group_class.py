class Group:
    def __init__(self, students=[]):
        self.__students = students
    def add(self, student):
        self.__students.append(student)
    def get_students(self):
        return self.__students

    def __str__(self):
        return f'{self.__students}'
# тут будут операции с листом и вычислениями по группе