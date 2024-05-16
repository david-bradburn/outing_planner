
import os
import json
import time
from sheets import sheets
# import csv
import utils
# import numpy as np


##############################################################
##
## Outing Planner Class
##
##############################################################


class outing_planner():

  def __init__(self):
   # self.loaded_member
  #  self.memdata = self.load_member_data()
   self.msg = """
    Please enter operation:
      0 : create and outing
          Does nothing
      1 : Create a member
      2 : display member
      3 : Save created members to file
      4 : grab availability data from sheets
      5 : Processes data from sheets and saves to csv
      6 : converts csv to df
      q : quit program

input : """

   self.main()

  def main(self):
   while True:
    self.main_menu()


  def main_menu(self):
    print("------------------------------------------------------")

    try:
      op = utils.askForInput(self.msg)

      match op:
        case 0:
          # Create outing
          ...

        case 1: # Create a member
          self.create_member()

        case 2: # view /edit member // load and edit
          self.raw_print()
          self.display_members_raw()
          self.display_members_formatted()

        case 3:
          self.save_members()

        case 4: # grab data from sheets
          self.rawdata = sheets.getSheets()
          # print(utils.get_data_size(data))

        case 5:

          try: # catch if we haven't ran 4
            rowersCollectionArr = utils.cleanANDSplitRawDataForCSV(self.rawdata)
          except AttributeError:
            print("Grabbing data")
            self.rawdata = sheets.getSheets()
            rowersCollectionArr = utils.cleanANDSplitRawDataForCSV(self.rawdata)

          self.filenames = ["rowers", "coxes", "coaches", "subs"]
          for index, item in enumerate(rowersCollectionArr):
            utils.writeString2csv(f"./availability/{self.filenames[index]}", item)

        case 6:

          utils.csv_to_df("rowers")
          utils.csv_to_df("coxes")
          utils.csv_to_df("coaches")
          utils.csv_to_df("subs")

        case "q":
          quit()

        case _:
          raise ValueError

    except ValueError as ex:
      print("Please enter valid value", ex)


  def create_outing(self):
    # Eventually I want to get the csv from google sheets

    ...

  def create_member(self):
    name = input("Please input name: ")
    side = input("Please input side: ")
    id = int(time.time())
    # print(id, int(id))
    mem = {"Name": name, "Side": side, "ID": id, "History": []}
    self.memdata["member_data"].append(mem)

  def save_members(self):
    dir_path = os.path.dirname(os.path.realpath(__file__))

    root = "member_data"
    filename_ext = "member_data.json"

    base = os.path.join(dir_path, root)
    filepath = os.path.join(base, filename_ext)
    # json_object = json.dumps(self.memdata, indent=4)

    print(filepath)
    with open(filepath, "w", encoding='utf-8') as outfile:
      json.dump(self.memdata, outfile, ensure_ascii=False, indent=2)


  def load_member_data(self):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    root = "member_data"
    fn = "member_data.json"
    base = os.path.join(dir_path, root)
    filepath = os.path.join(base, fn)

    try:
      with open(filepath, 'r') as f:
        return json.load(f)
    except Exception as ex:
      print("Error during loading object (possiblt does not exist):", ex)
      return None


  def raw_print(self) -> None:
    """
      Prints raw member data
    """
    print(self.memdata)


  def display_members_raw(self):
    """
      Prints member data
    """
    for mem in self.memdata['member_data']:
      print(mem)


  def display_members_formatted(self):
    for mem in self.memdata['member_data']:
      trmp_str = f"Name: {mem['Name']}\nSide: {mem['Side']}\nID: {mem['ID']}"
      print(trmp_str)


if __name__ == "__main__":
  outing_planner()