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
    scenarios = app_tables.scenario.search()
    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    Sys_PR = self.Sys_PR.text
    Sys_Int = self.Sys_Int.text
    Sys_Sys = self.Sys_Sys.text
    Sys_Ins= self.Sys_Ins.text
    print(str(Sys_PR) + ' ' + str(Sys_Int) + ' ' + str(Sys_Sys) + ' ' + str(Sys_Ins))
    SI_PR = self.SI_PR.text
    SI_Int = self.SI_Int.text
    SI_Sys = self.SI_Sys.text
    SI_Ins= self.SI_Ins.text
    

    app_tables.days_effort.add_row(projects= "Systems",
                          PreReqs = Sys_PR,
                          Interfacing = Sys_Int,
                          System_config= Sys_Sys,
                          Installing = Sys_Ins)
                       
    app_tables.days_effort.add_row(projects= "Standalone Systems",
                          PreReqs = SI_PR,
                          Interfacing = SI_Int,
                          System_config= SI_Sys,
                          Installing = SI_Ins)

  def scenario_dropdown_change(self, **event_args):
    """This method is called when an item is selected"""
    pass


