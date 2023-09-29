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
    self.scenario_dropdown.items= [(str(row['Scenario_Desc']), row) for row in app_tables.scenario.search(tables.order_by('Scenario_Desc'))]
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

    SM_PR = self.SM_PR.text
    SM_Int = self.SM_Int.text
    SM_Sys = self.SM_Sys.text
    SM_Ins= self.SM_Ins.text
    
    UP_PR = self.UP_PR.text
    UP_Int = self.UP_Int.text
    UP_Sys = self.UP_Sys.text
    UP_Ins= self.UP_Ins.text

    
    app_tables.days_effort.add_row(projects= "Systems",
                          PreReqs = Sys_PR,
                          Interfacing = Sys_Int,
                          System_config= Sys_Sys,
                          Installing = Sys_Ins)
                       
    app_tables.days_effort.add_row(projects= "Standalone Interfaces",
                          PreReqs = SI_PR,
                          Interfacing = SI_Int,
                          System_config= SI_Sys,
                          Installing = SI_Ins)

    app_tables.days_effort.add_row(projects= "Server Moves",
                          PreReqs = SM_PR,
                          Interfacing = SM_Int,
                          System_config= SM_Sys,
                          Installing = SM_Ins)
    app_tables.days_effort.add_row(projects= "Upgrades",
                          PreReqs = UP_PR,
                          Interfacing = UP_Int,
                          System_config= UP_Sys,
                          Installing = UP_Ins)

  def scenario_dropdown_change(self, **event_args):
    """This method is called when an item is selected"""
    data = app_tables.days_effort.search(Scenario=self.scenario_dropdown.selected_value)
    for row in data:
      print(row['projects'],row['PreReqs'],row['Interfacing'],row['System_config'],row['Installing'])
      if row['projects'] == 'Systems':
        self.Sys_PR.text = row['PreReqs']
        self.Sys_Int.text = row['Interfacing']
        self.Sys_Sys.text = row['System_config']
        self.Sys_Ins.text = row['Installing']

      if row['projects'] == 'Standalone Interfaces':
        self.SI_PR.text = row['PreReqs']
        self.SI_Int.text = row['Interfacing']
        self.SI_Sys.text = row['System_config']
        self.SI_Ins.text = row['Installing']
    pass


