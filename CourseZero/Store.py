"""
Created by 復讐者 on 2/15/19
"""
from CourseZero.RequestTools import get_file_links_from_course_page

__author__ = '復讐者'

from CourseZero.DataHandlingTools import get_by_course_id, get_urls

# from CourseZero.DataHandlingTools import get_departments
# from CourseZero.DataStorageTools import load_campus_id_data
import datetime

from CourseZero.Errors import UnsetValue

# class classproperty(object):
#
#     def __init__(self, fget):
#         self.fget = fget
#
#     def __get__(self, owner_self, owner_cls):
#         return self.fget(owner_cls)

def warn_if_empty( func ):
    """When class properties are retrieved, this
    checks whether they are empty and raises an exception if so"""

    def func_wrapper( *args, **kwargs ):
        result = func( *args, **kwargs )
        if result is None or len(result) == 0:
            raise UnsetValue( func.__name__ )
        return result
    return func_wrapper


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


class DStore( object ):
    _professor_first_name = None
    _professor_last_name = None
    campus_name = None
    campus_id = None
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
            cls.campus_name = v

    # @property
    # @prop_inspector_dec
    # def campus_name( cls ):
    #     return cls._campus_name

    # @prop_inspector_dec
    # @property
    # def campus_id( cls ):
    #     return cls._campus_id
    #
    # @campus_id.setter
    # def campus_id( cls, campus_id ):
    #     cls._campus_id = campus_id

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


class DataStore( object ):


    def __init__(self):
        # Load the campus ids from a file
        # if id_file is not None:
            # self.campus_ids = load_campus_id_data(id_file)
        self.data = None
        """DataFrame with query results """

        self.campus_ids = []
        self.campus_name = None
        self.campus_id = None
        self.course_ids = [ ]
        self._professor_first_name = None
        self._professor_last_name = None
        self.selected_departments = []

    @property
    def csu_names(self):
        return [c['name'] for c in self.campus_ids]

    @property
    def departments( self ):
        """All departments for the campus  from the results frame"""
        depts = list( set( self.data.dept_acro.tolist() ) )
        depts.sort()
        return depts

    # return get_departments(self.data)

    def _parse_event( self, event ):
        if event[ 'type' ] == 'change' and event[ 'name' ] == 'value':
            v = event[ 'new' ]
            return v

    def set_professor_fname( self, event ):
        v = self._parse_event( event )
        if v is not None:
            self._professor_first_name = v

    @property
    @prop_inspector_dec
    def professor_first_name( self ):
        return self._professor_first_name

    def set_professor_lname( self, event ):
        v = self._parse_event( event )
        if v is not None:
            self._professor_last_name = v

    @property
    @prop_inspector_dec
    def professor_last_name( cls ):
        return cls._professor_last_name

    # def set_campus_name( self, event ):
    #     v = self._parse_event( event )
    #     if v is not None:
    #         self.campus_name = v

    # @property
    # @prop_inspector_dec
    # def campus_name( cls ):
    #     return cls._campus_name

    # @prop_inspector_dec
    # @property
    # def campus_id( cls ):
    #     return cls._campus_id
    #
    # @campus_id.setter
    # def campus_id( cls, campus_id ):
    #     cls._campus_id = campus_id

    def add_course( self, course ):
        self.course_ids.append( course )
        self.course_ids = list( set( self.course_ids ) )
        # cls.departments = list( set( cls.departments.append( dept ) ) )

    def remove_course( self, course ):
        el = list( filter( lambda x: x == course, self.course_ids ) )[ 0 ]
        idx = self.course_ids.index( el )
        return self.course_ids.pop( idx )

    def add_department( self, dept ):
        """Adds a department to the list of departments the user wants to view"""
        self.selected_departments.append( dept )
        # cls.departments = list( set( cls.departments.append( dept ) ) )

    def remove_department( self, dept ):
        """Removes a department from the list of departments that the user wants to view"""
        el = list( filter( lambda x: x == dept, self.selected_departments ) )[ 0 ]
        idx = self.selected_departments.index( el )
        return self.selected_departments.pop( idx )

    @property
    def selected_departments_data( self ):
        """Uses the list of departments selected by the user to
        return those departments from the results frame
        returns DataFrame
        """
        return self.data[ self.data[ 'dept_acro' ].isin( self.selected_departments) ]

    @property
    def selected_courses_documents( self ):
        """Returns dataframe with the documents """
        return get_by_course_id( self.data, self.course_ids )

    @property
    def selected_courses_documents_urls( self ):
        return get_urls(self.data, self.course_ids)
        # for i, r in self.selected_courses_documents.iterrows():
        #     files = get_file_links_from_course_page( r[ 'url' ] )
        # return files


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
