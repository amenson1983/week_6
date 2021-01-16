class StudentException(Exception):
    def __init__(self, str_err):
        Exception.__init__(self,str_err)