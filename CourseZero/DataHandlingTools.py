"""
Created by 復讐者 on 7/13/19
"""
__author__ = '復讐者'

import pandas as pd

import environment as env
from CourseZero.Store import DataStore


def parse_counts( row ):
    """The server returns a field with a list of
    the various kinds of documents that have been uploaded.
    This parses those counts out and adds them as columns to the frame
    """
    for c in row[ 'doc_counts' ]:
        row[ c[ 'category' ] ] = c[ 'count' ]
    return row


def parse_json_into_df( json_data ):
    """Parse json data into a usable dataframe
    For now: Control which columns are kept by commenting out in to_keep
    """
    #     to_keep = [
    # #         '@timestamp',
    #      'canonical_course_id',
    # #         'country',
    #         'course_id',
    #        'course_info',
    #         'course_name',
    #         'course_num',
    # #         'course_pk',
    #         'dept_acro',
    #        'dept_id',
    #         'dept_name',
    #         'doc_counts', # if this isn't removed, can't dedupe
    # #         'location',
    #         'prof_id',
    #        'prof_name',
    # #         'school_aliases',
    # #         'school_id',
    #         'school_name',
    # #        'subdivision',
    #         'term',
    #         'title',
    #         'total_doc_count',
    #         'type',
    #         'url',
    #        'verified',
    #         'year'
    #     ]

    data = [ ]

    for r in json_data:
        try:
            if r[ 'total' ] > 0:
                for row in r[ 'results' ]:
                    data.append( row )

        except Exception as e:
            pass

    data = pd.DataFrame( data )
    # Filter out unneeded columns
    data = data[ env.JSON_FIELDS ]
    # Add the counts of each kind of document to the frame as a column
    data = data.apply( lambda r: parse_counts( r ), axis=1 )
    # Drop the counts column so can de-dupe (list isn't hashable)
    data.drop( [ 'doc_counts' ], axis=1, inplace=True )
    data.drop_duplicates( inplace=True )
    return data


# Data frame operations
def get_departments( frame ):
    """Extract list of departments from the results frame"""
    depts = list( set( frame.dept_acro.tolist() ) )
    depts.sort()
    return depts


def normalize_prof_name( prof_name ):
    return prof_name.strip().upper()


# Frame filtration operations
def filter_by_dept_abbrevs( frame ):
    """Uses the list of departments defined by the user to
    return those departments from the results frame"""
    return frame[ frame[ 'dept_acro' ].isin( DataStore.departments ) ]


def get_by_course_id( frame, course_ids ):
    """Finds and reeturns a course or list of courses from the results
    frame"""
    if type( course_ids ) is not list:
        course_ids = list( course_ids )
    return frame[ frame[ 'course_id' ].isin( course_ids ) ]


if __name__ == '__main__':
    pass