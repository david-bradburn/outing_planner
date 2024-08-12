
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
      ip = utils.askForInput(self.msg)

      match ip:
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
            rowersCollectionArr = utils.cleanANDSplitRawDataInTo2DArr(self.rawdata)
          except AttributeError:
            print("Grabbing data")
            self.rawdata = sheets.getSheets()
            rowersCollectionArr = utils.cleanANDSplitRawDataInTo2DArr(self.rawdata)

          self.alldata =  rowersCollectionArr

          self.proccessWhoIsAvail(self.alldata[0])


        case "q":
          quit()


        case "t":
          utils.dateFormating("7 May", "16:00pm")

        case _:
          raise ValueError

    except ValueError as ex:
      print("Please enter valid value", ex)

  def proccessWhoIsAvail(self, data: list):
    self.availdata = {}
    timearr = []
    listOfOutingTimes = data[1][2:]
    # print(listOfOutingTimes)
    numberOfOutings = len(listOfOutingTimes) -2
    for i in range(numberOfOutings):
      timearr.append(f"{data[1][2+i]} {data[2][2+i]}")
    print(timearr)
    self.availpeople = {}

    for date_index in range(numberOfOutings):
      temp = []
      for rower_index in range(len(data)-5):
        # print(data[5+rower_index][2+date_index])
        try:
          if data[5+rower_index][2+date_index].lower() == "y":
            temp.append(data[5+rower_index][0])
        except:
          pass
      self.availpeople[timearr[date_index]] = temp

    for key in self.availpeople:
      print(f"date: {key} -> rowers: {self.availpeople[key]}")


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