import csv

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
  with open(f"{filename}.csv", "w") as fd:
    wr = csv.writer(fd, quoting=csv.QUOTE_ALL)
    for row in data:
      wr.writerow(row)

