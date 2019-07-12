"""
Created by 復讐者 on 2/15/19
"""
__author__ = '復讐者'

from CourseZero.Errors import UnsetValue


def prop_inspector_dec(func):
    """When class properties are retrieved, this
    checks whether they are empty and raises an exception if so"""
    def func_wrapper(*args, **kwargs):
        cls_prop_name = "_{}".format(func.__name__)
        if getattr(args[0], cls_prop_name) is None:
            raise UnsetValue(func.__name__)
        return func(*args, **kwargs)
    return func_wrapper


class DataStore( object ):
    _professor_first_name = None
    _professor_last_name = None
    _campus_name = None
    _campus_id = None
    departments = [ ]
    course_ids = []

    @classmethod
    def _parse_event( cls, event ):
        if event[ 'type' ] == 'change' and event[ 'name' ] == 'value':
            v = event[ 'new' ]
            return v

    @classmethod
    def set_professor_fname( cls, event ):
        v = cls._parse_event( event )
        if v is not None:
            cls._professor_first_name = v

    @property
    @prop_inspector_dec
    def professor_first_name( cls ):
        return cls._professor_first_name

    @classmethod
    def set_professor_lname( cls, event ):
        v = cls._parse_event( event )
        if v is not None:
            cls._professor_last_name = v

    @property
    @prop_inspector_dec
    def professor_last_name( cls ):
        return cls._professor_last_name

    @classmethod
    def set_campus_name( cls, event ):
        v = cls._parse_event( event )
        if v is not None:
            cls._campus_name = v

    @property
    @prop_inspector_dec
    def campus_name( cls ):
        return cls._campus_name


    @classmethod
    def add_course( cls, course ):
        cls.course_ids.append( course )
        cls.course_ids = list(set(cls.course_ids))
        # cls.departments = list( set( cls.departments.append( dept ) ) )

    @classmethod
    def remove_course( cls, course ):
        el = list(filter(lambda x: x == course, cls.course_ids))[0]
        idx = cls.course_ids.index(el)
        return cls.course_ids.pop(idx)

    @classmethod
    def add_department( cls, dept ):
        cls.departments.append( dept )
        # cls.departments = list( set( cls.departments.append( dept ) ) )

    @classmethod
    def remove_department( cls, dept ):
        el = list(filter(lambda x: x == dept, cls.departments))[0]
        idx = cls.departments.index(el)
        return cls.departments.pop(idx)


class TakedownStore( DataStore ):
    agreed_w_reqd_statements = False

    @classmethod
    def toggle_statement_agreement( cls ):
        cls.agreed_w_reqd_statements = not cls.agreed_w_reqd_statements


if __name__ == '__main__':
    pass
