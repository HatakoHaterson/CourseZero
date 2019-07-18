"""
Created by 復讐者 on 2/15/19
"""
from CourseZero.Store import TakedownStore

__author__ = '復讐者'

from IPython.display import display
from ipywidgets import widgets


def make_email_helper_button( callback=None):
    """Creates a button for the document.
    Sets a handler on the button to toggle whether the doc is selected
    in the data store
    """
    layout = widgets.Layout( width='90%' )

    b = widgets.Button( description='Create draft takedown email', button_style='info', layout=layout )

    def handle( event ):

        if callback is not None:
            callback()

    b.on_click( handle )
    return b


def make_text_input( input_dict ):
    """Creates a text input field. The given dictionary should have keys 'label' and 'handler'"""
    text = widgets.Text( description=input_dict[ 'label' ], name=input_dict[ 'prop' ] )
    # display( text )
    text.observe( TakedownStore.event_handler )
    return text


if __name__ == '__main__':
    pass
