import csv
import pandas as pd

def print_ex_catch(msg: str, error_type: Exception):
    "Doesn't work if the error occurs in the message string :("
    try:
        print(msg)
    except:
        pass



def get_data_size(data_arr) -> tuple:
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

# def format_data_array(data_arr):
#   """
#     Format data array
#   """
#   aval_dict = {}
#   outingDates = []
#   outingTimes = []
#   for row_index, row in enumerate(data_arr):
#     match row_index:
#       case 0:
#         crew_name = row[0]

#       case 2:
#         for date in row:
#           outingDates.append(date)

#       case _:
#         pass

#   return arr

def write_to_csv(filename: str, data: list):
  """
    Write data array to csv file
  """

  strarr = []
  for row_index, row in enumerate(data):
    if row_index in [1, 4, 5, 6, 7 , 9]:
       continue
    tempstr = ""
    for item in row:
      tempstr += f"{item}, "
    # print(tempstr)
    tempstr = tempstr[:-2] + "\n"
    strarr.append(tempstr)


  with open(f"{filename}.csv", "w") as fd:
    for rowstr in strarr:
      fd.write(rowstr)

