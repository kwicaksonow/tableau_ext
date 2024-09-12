from ._anvil_designer import MainTemplate
from anvil import *
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
    dashboard.register_event_handler('selection_changed', self.selection_changed_event_handler)

  def selection_changed_event_handler(self, event):
    user_selection = event.worksheet.get_selected_marks()

    if len(user_selection) == 0:
        self.country_name = None
        self.happinessScore = None
    else:
        record = user_selection[0]
        self.country_name = record['Country']
        self.happinessScore = record['SUM(Happiness Score)']

  def btn_save_click(self, **event_args):
    """This method is called when the button is clicked"""
    
    msg = f"Country: {self.country_name}\nHappinessScore: {self.happinessScore}\nComment: {self.tb_comment.text}"
    Notification(msg).show()
    self.tb_comment.text = ""
