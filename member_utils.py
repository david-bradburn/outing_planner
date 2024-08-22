import os
import time
from datetime import datetime
import json

class member():
  def __init__(self, name, side, type):
    self.member_name = name
    self.filename = self.create_file_name_from_member_wrapper(self.member_name)
    self._member_exists = self.check_if_member_exists()
    # print(self.member_name, self.filename, self._member_exists)
    self.member_side = side
    self.member_type = type

  def create_file_name_from_member(self, name: str) -> str:
    splitName = name.split(' ')
    temp = splitName[0]
    if len(splitName) != 1:
      assert len(splitName) > 1
      temp = splitName[0]
      for i_name in splitName[1:]:
        temp += f"_{i_name}"
    
    return temp

  def create_file_name_from_member_wrapper(self, name: str) -> os.path:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    root = "member_data"
    n = self.create_file_name_from_member(name)
    filename_ext = f"{n}.json"
    base = os.path.join(dir_path, root)
    filepath = os.path.join(base, filename_ext)
    return filepath

  def check_if_member_exists(self) -> bool:
    return os.path.isfile(self.filename)


  def create_member_and_save(self):
    date_created = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    mem = {"Name": self.member_name, 
           "Side": self.member_side, 
           "Type": self.member_type,
           "Member Created": date_created, 
           "Member Last Updated": date_created, 
           "Last Updated Items": [],
           "History": []}
    
    self.save_member(mem)

  def save_member(self, mem_dict: dict) -> None:
    """
      Function to save member data as a json file
    """
    print(self.filename)
    with open(self.filename, "w", encoding='utf-8') as outfile:
      json.dump(mem_dict, outfile, ensure_ascii=False, indent=2)


  def load_member_data(self):
    try:
      with open(self.filename, 'r') as f:
        return json.load(f)
    except Exception as ex:
      print("Error during loading object (possiblt does not exist):", ex)
      return None

  def load_member_update_and_save(self):
    loc_mem_data = self.load_member_data()
    updateFile = False#
    lastUpdatedItems = []
    assert(loc_mem_data["Name"] == self.member_name)
    if loc_mem_data["Side"] != self.member_side:
      loc_mem_data["Side"] = self.member_side
      lastUpdatedItems.append("Side")
      updateFile = True
    
    if loc_mem_data["Type"] != self.member_type:
      loc_mem_data["Type"] = self.member_type
      lastUpdatedItems.append("Type")
      updateFile = True

    if updateFile:
      todaydatetime = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
      loc_mem_data["Member Last Updated"] = todaydatetime
      loc_mem_data["Last Updated Items"] = lastUpdatedItems
      print(f"member: {self.member_name} updated" )
      self.save_member(loc_mem_data)
    

  def check_loaded_member_is_valid(self):
    # TODO: need a add a check to see if loaded member data is valid
    ...

  # def raw_print(self) -> None:
  #   """
  #     Prints raw member data
  #   """
  #   print(self.memdata)


  # def display_members_raw(self):
  #   """
  #     Prints member data
  #   """
  #   for mem in self.memdata['member_data']:
  #     print(mem)


  # def display_members_formatted(self):
  #   for mem in self.memdata['member_data']:
  #     trmp_str = f"Name: {mem['Name']}\nSide: {mem['Side']}\nID: {mem['ID']}"
  #     print(trmp_str)