# import csv
import pandas as pd
import copy
import datetime as dt

def print_ex_catch(msg: str, error_type: Exception):
  "Doesn't work if the error occurs in the message string :("
  try:
      print(msg)
  except:
      pass



def get_data_size(data_arr: list) -> tuple:
  """
    Gets the size of the availability data
  """
  height = len(data_arr)
  max_width = 0

  for row in data_arr:
    max_width = len(row) if len(row) > max_width else max_width
  return max_width, height


def read_from_csv(filename):
  with open(f"{filename}.csv", "r"):
    ...

def csv_to_df(filename: str, pathtodir = "availability"):
  df = pd.read_csv(f"{pathtodir}/{filename}.csv")
  print(df)


def dateFormating(avalDate: str, time: str):
  """
    To convert the string to datetime format
    https://favtutor.com/blogs/get-current-year-python
    https://www.digitalocean.com/community/tutorials/python-string-to-datetime-strptime
  """
  todaydate = dt.date.today()

  thisYear = todaydate.year
  thisYearString = str(thisYear)
  # print(thisYearString) # Need to be able to handle the year switch over

  datetimestring = f"{avalDate} {thisYearString} {time}"
  dtformat = "%d %b %Y %H:%M%p"

  op = dt.datetime.strptime(datetimestring, dtformat)
  if op.date() < todaydate:
    thisYearString = str(thisYear + 1)
    datetimestring = f"{avalDate} {thisYearString} {time}"
    dtformat = "%d %b %Y %H:%M%p"

    op = dt.datetime.strptime(datetimestring, dtformat)

  print(op)


def askForInput(msg: str) -> str:
  ip = input(msg)

  return inputCleaning(ip)

def inputCleaning(ip: str) -> str | int:
  try:
    temp = int(ip)
  except:
    temp = ip

  return temp

def cleanANDSplitRawDataInTo2DArr(data: list) -> list:
  """
    New function to return a 2d array and save that instead
  """
  loc = 0
  # arrayOfstringsRowing = []
  header = []
  Rowers = []
  Coxes = []
  Coaches = []
  Subs = []
  for row_index, row in enumerate(data):
    if row_index in [1, 4, 5, 6, 7 , 9]:
      continue
    temparr = []
    # print(f"{row_index}, {loc}, {row}")
    for item in row:
      if item == "END": #cba stripping out the END
        continue
      match item:
        case "Rowers" | "Coxes" | "Subs" | "Coaches":
          if loc == 0:
            Rowers = copy.deepcopy(header)
            Coxes = copy.deepcopy(header)
            Coaches = copy.deepcopy(header)
            Subs = copy.deepcopy(header)
          loc += 1
          continue # cheeky/hacky way to remove the "Rowers" | "Coxes" | "Subs" | "Coaches" bit
        case _:
          pass

      temparr.append(item)

    # tempstr = tempstr[:-2] + "\n" # get rid of last comma and space

    match loc:
      case 0: #This is for the header
        header.append(temparr)

      case 1: #Rowers
        if len(temparr) == 0:
          pass
        else:
          Rowers.append(temparr)
      

      case 2: # Coxes
        if len(temparr) == 0:
          pass
        else:
          Coxes.append(temparr)

      case 3: # Coaches
        if len(temparr) == 0:
          pass
        else:
          Coaches.append(temparr)

      case 4: #Subs
        if len(temparr) == 0:
          pass
        else:
          Subs.append(temparr)

      case _:
        raise Exception("Should be impossible")

  # print(header)
  return [Rowers, Coxes, Coaches, Subs]



def cleanANDSplitRawDataForCSV(data: list) -> list:
  """
    This cleans and splits the data
  """
  loc = 0
  # arrayOfstringsRowing = []
  header = []
  Rowers = []
  Coxes = []
  Coaches = []
  Subs = []
  for row_index, row in enumerate(data):
    if row_index in [1, 4, 5, 6, 7 , 9]:
      continue
    tempstr = ""
    # print(f"{row_index}, {loc}, {row}")
    for item in row:
      if item == "END": #cba stripping out the END
        continue
      match item:
        case "Rowers" | "Coxes" | "Subs" | "Coaches":
          if loc == 0:
            Rowers = copy.deepcopy(header)
            Coxes = copy.deepcopy(header)
            Coaches = copy.deepcopy(header)
            Subs = copy.deepcopy(header)
          loc += 1
          continue # cheeky/hacky way to remove the "Rowers" | "Coxes" | "Subs" | "Coaches" bit
        case _:
          pass

      tempstr += f"{item}, "

    tempstr = tempstr[:-2] + "\n" # get rid of last comma and space

    match loc:
      case 0: #This is for the header
        header.append(tempstr)

      case 1: #Rowers
        Rowers.append(tempstr)

      case 2: # Coxes
        Coxes.append(tempstr)

      case 3: # Coaches
        Coaches.append(tempstr)

      case 4: #Subs
        Subs.append(tempstr)

      case _:
        raise Exception("Should be impossible")

  # print(header)
  return [Rowers, Coxes, Coaches, Subs]


def writeString2csv(filename: str, data: list) -> None:
  """
    Write data array to csv file
  """
  # I want to split the df into 4 main sections, core rowers, coxes, coaches and subs

  with open(f"{filename}.csv", "w") as fd:
    for rowstr in data:
      fd.write(rowstr)

# def readcsv22Darr(filename: str, pathtodir = "availability"):
#   with open(f"{pathtodir}/{filename}.csv", "r") as fd:

