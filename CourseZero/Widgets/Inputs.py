"""
Created by 復讐者 on 7/13/19
"""
__author__ = '復讐者'


from IPython.display import display
from ipywidgets import widgets

from CourseZero.Store import DataStore

# --------------------- Course selection
def make_selection_text(row):
    """Creates the text displayed in the course selection button"""
    t = "{prof_name} ---- {dept_acro} {course_num} ----  {course_name} ----  {course_info}"
    return t.format(**row.to_dict())

def make_course_b(row):
    """Creates a button for the course defined in the row.
    Sets a handler on the button to toggle whether the course is selected
    in the data store
    """
    layout = widgets.Layout(width='90%')
    b = widgets.Button(description=make_selection_text(row), button_style='primary', layout=layout)

    def handle(event):
        if row['course_id'] in DataStore.course_ids:
            DataStore.remove_course(row['course_id'])
            b.button_style='primary'
        else:
            DataStore.add_course(row['course_id'])
            b.button_style='success'
    b.on_click(handle)
    return b

# -------------------- Department selection

def make_dept_b(dept):
    b = widgets.Button(description=dept, button_style='primary')
    def handle(event):
        if dept in DataStore.departments:
            DataStore.remove_department(dept)
            b.button_style='primary'
        else:
            DataStore.add_department(dept)
            b.button_style='success'
    b.on_click(handle)
    return b


def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]

def dept_selection(depts):
    """Create and display the buttons for selecting which departments
    to query"""
    buttons = []
    for dept in depts:
        buttons.append(make_dept_b(dept))

    b1, b3 = split_list(buttons)
    b1, b2 = split_list(b1)
    b3, b4 = split_list(b3)

    display(widgets.HBox([widgets.VBox(b1), widgets.VBox(b2), widgets.VBox(b3), widgets.VBox(b4)]))


# -------------------- File selection
def make_link(url):
    return "<a href='{}' target='_blank'>{}</a>".format(url,url)

def make_infringement_b(doc, store):
    """Creates a button for the document.
    Sets a handler on the button to toggle whether the doc is selected
    in the data store
    """
    layout = widgets.Layout()
    b = widgets.Button(description='NOT Infringing', button_style='primary', layout=layout)

    def handle(event):
        if doc in store.infringing_docs:
            store.remove_doc(doc)
            b.button_style='primary'
            b.description='NOT Infringing'
        else:
            store.add_doc(doc)
            b.button_style='success'
            b.description='Infringing'
    b.on_click(handle)
    return b

def get_urls(frame):
    """Handles displaying the urls and information that has been retrieved"""
    selected = get_by_course_id(frame, DataStore.course_ids)
    for i, r in selected.iterrows():
        files = get_file_links_from_course_page(r['url'])
    return files

if __name__ == '__main__':
    pass