import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.files
from anvil.files import data_files
import anvil.server
import sqlite3

@anvil.server.callable
def get_gefaengnisse():
  conn = sqlite3.connect(data_files['gefaengnisverwaltung.db'])
  cursor = conn.cursor()
  gefaengnisse = list(cursor.execute("SELECT * FROM Gefaengnis"))
  conn.close()
  print(f"Gefängnisse: {gefaengnisse}")
  dropdown = []
  for i in gefaengnisse:
    dropdown.append((i[1], i[0]))
  return dropdown
  
@anvil.server.callable
def get_direktor_freieZellen(gefID):
  conn = sqlite3.connect(data_files['gefaengnisverwaltung.db'])
  cursor = conn.cursor()
  verwaltungen = list(cursor.execute(f"SELECT * FROM Verwaltung WHERE FKGefID = {gefID}"))
  conn.close()
  print(f"Verwaltung: {verwaltungen}")
  dropdown = []
  for i in verwaltungen:
    dropdown.append((i[1], i[2]))
  return dropdown

@anvil.server.callable
def get_zellen(gefID):
  conn = sqlite3.connect(data_files['gefaengnisverwaltung.db'])
  cursor = conn.cursor()
  zellen = list(cursor.execute(f"SELECT * FROM Zelle WHERE FKGefID = {gefID}"))
  conn.close()
  
  dropdown = []
  for i in zellen:
    dropdown.append((i[1], i[0]))
  print(f"Zellen: {dropdown}")
  return dropdown