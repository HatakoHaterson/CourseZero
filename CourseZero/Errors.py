"""
Created by  on 7/11/19
"""
__author__ = ''


class UnsetValue(Exception):

    def __init__(self, value_name):
        self.message = "You need to set {}. Please use the dialog above".format(value_name)
        super().__init__()


if __name__ == '__main__':
    pass