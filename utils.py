import csv

def print_ex_catch(msg: str, error_type: Exception):
    "Doesn't work if the error occurs in the message string :("
    try:
        print(msg)
    except:
        pass

def write_to_csv(filename, data):
  with open(f"{filename}.csv", "w") as fd:
    wr = csv.writer(fd, quoting=csv.QUOTE_ALL)
    for row in data:
      wr.writerow(row)

