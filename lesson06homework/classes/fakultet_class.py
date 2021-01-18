


class Facultet():
      def __init__(self, economy = [],it = []):
          self.__economy = economy
          self.__it = it

      def add_to_economy(self, group):
          self.__economy.append(group)

      def add_to_it(self, group):
          self.__it.append(group)

      def get_economy(self):
          return self.__economy

      def get_it(self):
          return self.__it

      def __str__(self):
          return f" {self.get_economy()}, {self.get_it()}"