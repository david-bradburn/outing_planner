import os
# import rowing_member
import json
import time
from sheets import sheets
# import csv
import utils


##############################################################
##
## Outing planner Class
##
##############################################################


class outing_planner():

  def __init__(self):
   # self.loaded_member
   self.memdata = self.load_member_data()
   self.main()

  def main(self):
   while True:
    self.main_menu()


  def main_menu(self):
    print("------------------------------------------------------")

    try:
      op = int(input("Please enter operation: \n  0 : create and outing\n  2 : display member \n  9 : quit program\n"))

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
          data = sheets.getSheets()
          utils.write_to_csv("dump", data)

        case 9:
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

  def raw_print(self):
    print(self.memdata)

  def display_members_raw(self):
    for mem in self.memdata['member_data']:
      print(mem)

  def display_members_formatted(self):
    for mem in self.memdata['member_data']:
      trmp_str = f"Name: {mem['Name']}\nSide: {mem['Side']}\nID: {mem['ID']}"
      print(trmp_str)


if __name__ == "__main__":
  outing_planner()