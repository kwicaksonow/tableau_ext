# Code for user to select data

# from ._anvil_designer import client_codeTemplate
# from anvil import *
# import anvil.server
# from anvil.tables import app_tables
# from anvil import tableau
# from datetime import datetime
# from trexjacket.api import get_dashboard

# dashboard = get_dashboard()

# class client_code(client_codeTemplate):
#   def __init__(self, **properties):
#     self.init_components(**properties)
#     self.summary.visible = False
#     dashboard.register_event_handler('selection_changed', self.selection_changed_event_handler)

#   def selection_changed_event_handler(self, event):
#     user_selections = event.worksheet.get_selected_marks()
#     if len(user_selections) != 0:
#         self._data = user_selections

#   def btn_submit_click(self, **event_args):
#     """This method is called when the button is clicked"""
#     msg = "Mohon Tunggu"
#     Notification(msg).show()
#     self.summary.text = ''
#     dataSummary = anvil.server.call('generateDataSummary', prompt=self.user_question.text, data=self._data)
#     self.summary.visible = True
#     self.summary.text = dataSummary

#   def btn_clear_click(self, **event_args):
#     """This method is called when the button is clicked"""
#     self.summary.text = ''
#     self.user_question.text = ''
#     self._data = ''
#     self.summary.visible = False



# Code for named worksheet

from ._anvil_designer import client_codeTemplate
from anvil import *
import anvil.server
from anvil.tables import app_tables
from anvil import tableau
from datetime import datetime
from trexjacket.api import get_dashboard

class client_code(client_codeTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.dashboard = get_dashboard()
    # replace 'Viz' with the name of your worksheet
    self.chart     = self.dashboard.get_worksheet('Viz')

  def selection_changed_event_handler(self, event):
    user_selections = event.worksheet.get_selected_marks()
    if len(user_selections) != 0:
        self._data = user_selections

  def btn_submit_click(self, **event_args):
    Notification("Mohon Tunggu").show()
    self.summary.text = ''
    # OPTION A: get the aggregated summary data
    data = self.chart.get_summary_data()
    # OPTION B: get the full, row‑level data
    # data = self.chart.get_underlying_data()
    dataSummary = anvil.server.call(
      'generateDataSummary',
      prompt=self.user_question.text,
      data=data
    )
    self.summary.visible = True
    self.summary.text    = dataSummary

  def btn_clear_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.summary.text = ''
    self.user_question.text = ''
    self._data = ''
    self.summary.visible = False



# Code for all worksheet

# from ._anvil_designer import client_codeTemplate
# from anvil import *
# import anvil.server
# from anvil.tables import app_tables
# from anvil import tableau
# from datetime import datetime
# from trexjacket.api import get_dashboard

# class client_code(client_codeTemplate):
#   def __init__(self, **properties):
#     self.init_components(**properties)
#     self.dashboard = get_dashboard()
#     # replace 'Viz' with the name of your worksheet
#     self.chart     = self.dashboard.get_worksheet('Viz')

#   def selection_changed_event_handler(self, event):
#     user_selections = event.worksheet.get_selected_marks()
#     if len(user_selections) != 0:
#         self._data = user_selections

#   def btn_submit_click(self, **event_args):
#     Notification("Mohon Tunggu").show()
#     self.summary.text = ''
#     # OPTION A: get the aggregated summary data
#     data = self.chart.get_summary_data()
#     # OPTION B: get the full, row‑level data
#     # data = self.chart.get_underlying_data()
#     dataSummary = anvil.server.call(
#       'generateDataSummary',
#       prompt=self.user_question.text,
#       data=data
#     )
#     self.summary.visible = True
#     self.summary.text    = dataSummary

#   def btn_clear_click(self, **event_args):
#     """This method is called when the button is clicked"""
#     self.summary.text = ''
#     self.user_question.text = ''
#     self._data = ''
#     self.summary.visible = False