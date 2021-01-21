


class Facultet():
      def __init__(self, management = [],it = []):
          self.__management = management
          self.__it = it

      def add_to_management(self, student):
          self.__management.append(student.get_fio())

      def add_to_it(self, student):
          self.__it.append(student.get_fio())

      def get_management(self):
          return self.__management

      def get_it(self):
          return self.__it

      def __str__(self):
          return f" {self.get_management()}, {self.get_it()}"