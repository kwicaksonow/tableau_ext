from ._anvil_designer import MainTemplate
from anvil import *
import anvil.server
from anvil.tables import app_tables
from anvil import tableau
from datetime import datetime

from trexjacket.api import get_dashboard
dashboard = get_dashboard()

class Main(MainTemplate):
  def __init__(self, **properties):
    self.country_name = None
    self.happinessScore = None
    self.logged_in_user = None
    self.init_components(**properties)
    self.Summary.visible = False
    dashboard.register_event_handler('selection_changed', self.selection_changed_event_handler)

  def selection_changed_event_handler(self, event):
    user_selections = event.worksheet.get_selected_marks()

    if len(user_selections) != 0:
        self._data = user_selections

  def fetchSummary(self):
    msg = "Wait"
    Notification(msg).show()
    self.Summary.text = ''
    dataSummary = anvil.server.call('generateDataSummary', prompt=self.tb_comment.text, data=self._data)
    self.Summary.visible = True
    self.Summary.text = dataSummary
    self._data = ''

  def btn_save_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.fetchSummary()

  def Clear_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.Summary.text = ''
    self.tb_comment.text = ''
    self._data = ''
    self.Summary.visible = False
    