import logging
logging.basicConfig(filename='product.log', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
class StudentException(Exception):
    def __init__(self, str_err):
        Exception.__init__(self,str_err)