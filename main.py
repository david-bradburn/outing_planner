
import os
from sheets import sheets
import member_utils
import utils



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
            ListofListofMembers = utils.cleanANDSplitRawDataInTo2DArr(self.rawdata)
          except AttributeError:
            print("Grabbing data")
            self.rawdata = sheets.getSheets()
            ListofListofMembers = utils.cleanANDSplitRawDataInTo2DArr(self.rawdata)

          self.alldata =  ListofListofMembers
          print(self.alldata[0])
          self.proccessWhoIsAvail(self.alldata[0])

        case 6:
          # This creates local copies of all the members it finds in the spreadsheet
   

          typearr= ["rower", "cox", "coach", "sub"]
          for member_index in range(5, len(self.alldata[0])-1):
            name = self.alldata[0][member_index][0]
            side = self.alldata[0][member_index][1]
            print(name,side)
            if member_utils.check_if_member_exists(name):
              ...
            else:
              member_utils.create_member_from_file(name, side)
        


          ...
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




if __name__ == "__main__":
  outing_planner()