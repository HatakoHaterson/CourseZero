"""
Created by 復讐者 on 7/11/19
"""
from CourseZero.DataStorageTools import load_campus_id_data

__author__ = '復讐者'


import os
import sys

############################ Locations  ############################
ROOT = os.getenv( "HOME" )

# The folder containing environment.py
PROJ_BASE = os.path.abspath(os.path.dirname(__file__))

DATA_FOLDER = "{}/data".format(PROJ_BASE)
STORAGE_FOLDER = "{}/storage".format(PROJ_BASE)
TEMPLATE_FOLDER = "{}/templates".format(PROJ_BASE)

DEFAULT_CSU_ID_FILE = '{}/csu_ids.json'.format(DATA_FOLDER)

# Which fields from requests to use
# For now: Control which columns are kept by commenting out below
JSON_FIELDS = [
    #         '@timestamp',
    'canonical_course_id',
    #         'country',
    'course_id',
    'course_info',
    'course_name',
    'course_num',
    #         'course_pk',
    'dept_acro',
    'dept_id',
    'dept_name',
    'doc_counts', # if this isn't removed, can't dedupe
    #         'location',
    'prof_id',
    'prof_name',
    #         'school_aliases',
    #         'school_id',
    'school_name',
    #        'subdivision',
    'term',
    'title',
    'total_doc_count',
    'type',
    'url',
    'verified',
    'year'
]

CH_BASE_URL = "https://www.coursehero.com{}"

from CourseZero.Store import DataStore as DS

DataStore = DS()
DataStore.campus_ids = load_campus_id_data(DEFAULT_CSU_ID_FILE)

if __name__ == '__main__':
    pass

