from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    # Any code you write here will run before the form opens.
    self.gefaengnisse_drop_down.items = anvil.server.call('get_gefaengnisse')
    self.label_direktor.text = "bitte Dropdown aktualisieren" 
    self.label_freie_zellen.text = "bitte Dropdown aktualisieren"
    self.repeating_zellen.items = [{'zellennummer': 'TODO', 'anzahl_häftlinge': 'TODO'}, 
                                   {'zellennummer': 'TODO', 'anzahl_häftlinge': 'TODO'}]

  def gefaengnisse_drop_down_change(self, **event_args):
    self.gefaengnisse_drop_down.items = anvil.server.call('get_gefaengnisse')
    self.label_direktor.text = anvil.server.call('get_direktor_freieZellen', self.gefaengnisse_drop_down.selected_value)[0][0]
    self.label_freie_zellen.text = anvil.server.call('get_direktor_freieZellen', self.gefaengnisse_drop_down.selected_value)[0][1]

    items = anvil.server.call('get_zellen', self.gefaengnisse_drop_down.selected_value)
    toAdd = []
    for item in len(items):
      temp = {'zellennummer':item[0][0], 'anzahl_häftlinge':item[0][1]}
      toAdd.append(temp)
    self.data_grid_zellen.columns = toAdd
    
    
    pass

 



  
 
