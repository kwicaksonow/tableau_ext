# ------------- Code to let user select data -------------

# from anvil import *
# import anvil.server
# from anvil import tableau
# from anvil.tables import app_tables
# from datetime import datetime
# from trexjacket.api import get_dashboard
# from ._anvil_designer import client_codeTemplate

# class client_code(client_codeTemplate):
#   def __init__(self, **properties):
#     self.init_components(**properties)
#     self.summary.visible = False
#     self.dashboard = get_dashboard()
#     self.dashboard.register_event_handler('selection_changed', 
#                                           self.selection_changed_event_handler)

#   def selection_changed_event_handler(self, event):
#     user_selections = event.worksheet.get_selected_marks()
#     if len(user_selections) != 0:
#         self._data = user_selections

#   def btn_submit_click(self, **event_args):
#     """This method is called when the button is clicked"""
#     msg = "Mohon Tunggu"
#     Notification(msg).show()
#     self.summary.text = ''
#     dataSummary = anvil.server.call('generateDataSummary', 
#                                     prompt=self.user_question.text, 
#                                     data=self._data)
#     self.summary.visible = True
#     self.summary.text = dataSummary

#   def btn_clear_click(self, **event_args):
#     """This method is called when the button is clicked"""
#     self.summary.text = ''
#     self.user_question.text = ''
#     self._data = ''
#     self.summary.visible = False



# ------------- Code to pick a worksheet -------------

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
#     self.chart = self.dashboard.get_worksheet('Viz')

#   def btn_submit_click(self, **event_args):
#     Notification("Mohon Tunggu").show()
#     self.summary.text = ''
#     # OPTION A: get the aggregated summary data
#     data = self.chart.get_summary_data()
#     # OPTION B: get the full, row‑level data
#     data = self.chart.get_underlying_data()

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



# ------------- Code for all worksheet -------------

# from ._anvil_designer import client_codeTemplate
# from anvil import *
# import anvil.tables as tables
# import anvil.tables.query as q
# from anvil.tables import app_tables
# import anvil.server
# from anvil import tableau
# from datetime import datetime
# from trexjacket.api import get_dashboard

# # Setup class untuk UI dalam client_code de
# class client_code(client_codeTemplate):
#   # Setup konstruktor
#   def __init__(self, **properties):
#     self.init_components(**properties)
#     # Ambil dashboard dan semua worksheet-nya
#     self.dashboard  = get_dashboard()
#     self.worksheets = self.dashboard.worksheets

#   def btn_submit_click(self, **event_args):
#     # Ketika tombol submit diklik
#     Notification("Mohon Tunggu").show()
#     self.summary.text = ''
    
#     all_data = {}
#     for ws in self.worksheets:
#       sheet_name = ws.name  # Menggunakan atribut 'name' langsung
#       # OPTION A: get the aggregated summary data
#       # summary = ws.get_summary_data(ignore_selection=True)
#       summary = ws.get_summary_data()
#       # OPTION B: get the full, row‑level data
#       # summary = ws.get_underlying_data()
#       all_data[sheet_name] = summary

#     dataSummary = anvil.server.call('generateDataSummary',
#                                     prompt=self.user_question.text,
#                                     data=all_data)

#     self.summary.visible = True
#     self.summary.text = dataSummary

#   def btn_clear_click(self, **event_args):
#     """This method is called when the button is clicked"""
#     self.summary.text = ''
#     self.user_question.text = ''
#     self._data = ''
#     self.summary.visible = True


    
# ------------- Code for ask the database -------------

from ._anvil_designer import client_codeTemplate
from anvil import *
import anvil.server
from anvil import tableau
from datetime import datetime
from trexjacket.api import get_dashboard

class client_code(client_codeTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)   
    # Ambil dashboard dan semua worksheet-nya
    self.dashboard  = get_dashboard()
    self.worksheets = self.dashboard.worksheets

  def btn_submit_click(self, **event_args):
    # Ketika tombol submit diklik
    Notification("Mohon Tunggu").show()
    self.summary.text = ''
    
    all_data = {}
    for ws in self.worksheets:
      sheet_name = ws.name  # Menggunakan atribut 'name' langsung
      summary = ws.get_summary_data(ignore_selection=True)
      all_data[sheet_name] = summary

    dataSummary = anvil.server.call(
      'query_database',
      self.user_question.text
    )

    self.summary.visible = True
    self.summary.text = dataSummary

  def btn_clear_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.summary.text = ''
    self.user_question.text = ''
    self._data = ''
    self.summary.visible = True

  # def user_question1_pressed_enter(self, **event_args):
  #   """This method is called when the user presses Enter in this text box"""
  #   Notification("Mohon Tunggu").show()
  #   self.summary.text = ''
    
  #   all_data = {}
  #   for ws in self.worksheets:
  #     sheet_name = ws.name  # Menggunakan atribut 'name' langsung
  #     summary = ws.get_summary_data(ignore_selection=True)
  #     all_data[sheet_name] = summary

  #   dataSummary = anvil.server.call(
  #     'generateDataSummary',
  #     prompt=self.user_question.text,
  #     data=all_data
  #   )

  #   self.summary.visible = True
  #   self.summary.text = dataSummary