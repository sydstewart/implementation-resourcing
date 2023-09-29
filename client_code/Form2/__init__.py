from ._anvil_designer import Form2Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form2(Form2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    Sys_PR = self.Sys_PR.text
    Sys_Int = self.Sys_Int.text
    Sys_Sys = self.Sys_Sys.text
    Sys_Ins= self.Sys_Ins.text
    print(Sys_PR + ' ' + Sys_Int + ' ' + Sys_Sys + ' ' + Sys_Ins)
    
    

    app_tables..add_row(projects="Systems",
                          PreReqs = Sys_PR,
                          Interfacing = Sys_int)
                       


