"""
Created by 復讐者 on 2/15/19
"""
__author__ = '復讐者'

import datetime

from CourseZero.Errors import UnsetValue

# class classproperty(object):
#
#     def __init__(self, fget):
#         self.fget = fget
#
#     def __get__(self, owner_self, owner_cls):
#         return self.fget(owner_cls)


def prop_inspector_dec( func ):
    """When class properties are retrieved, this
    checks whether they are empty and raises an exception if so"""

    def func_wrapper( *args, **kwargs ):
        print(func.__name__)
        cls_prop_name = "_{}".format( func.__name__ )
        if getattr( args[ 0 ], cls_prop_name ) is None:
            raise UnsetValue( func.__name__ )
        return func( *args, **kwargs )

    return func_wrapper


class DataStore( object ):
    _professor_first_name = None
    _professor_last_name = None
    _campus_name = None
    _campus_id = None
    departments = [ ]
    course_ids = [ ]

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

    @prop_inspector_dec
    @property
    def campus_id( cls ):
        return cls._campus_id

    @campus_id.setter
    def campus_id( cls, campus_id ):
        cls._campus_id = campus_id

    @classmethod
    def add_course( cls, course ):
        cls.course_ids.append( course )
        cls.course_ids = list( set( cls.course_ids ) )
        # cls.departments = list( set( cls.departments.append( dept ) ) )

    @classmethod
    def remove_course( cls, course ):
        el = list( filter( lambda x: x == course, cls.course_ids ) )[ 0 ]
        idx = cls.course_ids.index( el )
        return cls.course_ids.pop( idx )

    @classmethod
    def add_department( cls, dept ):
        cls.departments.append( dept )
        # cls.departments = list( set( cls.departments.append( dept ) ) )

    @classmethod
    def remove_department( cls, dept ):
        el = list( filter( lambda x: x == dept, cls.departments ) )[ 0 ]
        idx = cls.departments.index( el )
        return cls.departments.pop( idx )


class TakedownStore( object ):
    """Stores data for creating takedown request letter"""
    infringing_docs = [ ]
    name = None
    address = None
    email = None

    input_fields = [
        { 'label' : 'Your full name', 'prop': 'prof_name'},
        {'label' : 'Your institution', 'prop': 'institution'},
        {'label' : 'Department', 'prop': 'department'},
        {'label': 'Street address', 'prop': 'street_address' },
        {'label' : 'City', 'prop': 'city'},
        {'label':'Zipcode', 'prop': 'zip'},
        {'label':'Email address', 'prop': 'email'},
        #  {'label':'', 'prop': ''}
    ]

    @classmethod
    def event_handler(cls, event):
        if event[ 'type' ] == 'change' and event[ 'name' ] == 'value':
            v = event[ 'new' ]
            # lookup the property from the label
            label = getattr(event['owner'], 'description')
            update_prop = list(filter( lambda x: x['label'] == label, cls.input_fields ) )[0]['prop']
            setattr(cls, update_prop, v)

    @classmethod
    def add_doc( cls, url ):
        cls.infringing_docs.append( url )

    @classmethod
    def remove_doc( cls, url ):
        idx = cls.infringing_docs.index( url )
        return cls.infringing_docs.pop( idx )

    @property
    def doc_urls( cls ):
        """Creates a html list of the infringing urls"""
        temp = "<li>{}</li>"
        u = "<ul>"
        for url in cls.infringing_docs:
            u += temp.format( url )
        u += '</ul>'
        return u

    @classmethod
    def format_args( cls ):
        return {
            'letter_date': datetime.date.isoformat( datetime.date.today() ),
            'name': cls.name,
            'email': cls.email,
            'address': cls.address,
            'doc_urls': cls.doc_urls
        }


if __name__ == '__main__':
    pass
