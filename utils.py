import csv
import pandas as pd
import copy

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

def csv_to_df(filename: str):
  df = pd.read_csv(f"{filename}.csv")
  print(df)


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
            # print(header)
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

