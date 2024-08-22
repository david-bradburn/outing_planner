
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
      1 : Processes data from sheets and calulates who is available
          Then does nothing
      2 : Creates or updates memeb files on system
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

        case 1:

          try: # catch if we haven't ran 4
            ListofListofMembers = utils.cleanANDSplitRawDataInTo2DArr(self.rawdata)
          except AttributeError:
            print("Grabbing data")
            self.rawdata = sheets.getSheets()
            ListofListofMembers = utils.cleanANDSplitRawDataInTo2DArr(self.rawdata)

          self.alldata =  ListofListofMembers
          # print(self.alldata[0])
          # print(self.alldata[1])
          # print(self.alldata[2])
          # print(self.alldata[3])
          typearr = ["rower", "cox", "coach", "sub"]
          for index, memtype in enumerate(typearr):
            self.proccessWhoIsAvail(self.alldata[index], memtype)

        case 2:
          # This creates local copies of all the members it finds in the spreadsheet

          typearr= ["rower", "cox", "coach", "sub"]
          for member_type in range(4):
            for member_index in range(5, len(self.alldata[member_type])): ## this just skips the header
              name = self.alldata[member_type][member_index][0]
              try:
                side = self.alldata[member_type][member_index][1]
              except:
                side = "N/A"
              member = member_utils.member(name, side, typearr[member_type])
              
              if member._member_exists:
                # print("member exits")
                member.load_member_update_and_save()
              else:
                print("member does not exist, creating file")
                member.create_member_and_save()
        
          ...
        case "q":
          quit()


        case "t":
          utils.dateFormating("7 May", "16:00pm")

        case _:
          raise ValueError

    except ValueError as ex:
      print("Please enter valid value", ex)

  def proccessWhoIsAvail(self, data: list, member_type: str):
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
      print(f"date: {key} -> {member_type}: {self.availpeople[key]}")

  def create_outing(self):
    # Eventually I want to get the csv from google sheets

    ...


if __name__ == "__main__":
  outing_planner()