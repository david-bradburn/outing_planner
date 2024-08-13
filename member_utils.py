import os
import time
import json

def create_file_name_from_member(name: str) -> str:
  splitName = name.split(' ')
  temp = splitName[0]
  if len(splitName) != 1:
    assert len(splitName) > 1
    temp = splitName[0]
    for i_name in splitName[1:]:
      temp += f"_{i_name}"
  
  return temp
  

def check_if_member_exists(name: str) -> bool:
  dir_path = os.path.dirname(os.path.realpath(__file__))
  root = "member_data"

  filename = create_file_name_from_member(name)
  filename_ext = f"{filename}.json"

  base = os.path.join(dir_path, root)
  filepath = os.path.join(base, filename_ext)

  return os.path.isfile(filepath)


def create_member_from_file(name, side):
  # id = int(time.time())
  # print(id, int(id))
  mem = {"Name": name, "Side": side, "History": []}

  save_members(mem)
  

def save_members(mem_dict: dict):
  dir_path = os.path.dirname(os.path.realpath(__file__))

  root = "member_data"
  n = create_file_name_from_member(mem_dict["Name"])
  filename_ext = f"{n}.json"

  base = os.path.join(dir_path, root)
  filepath = os.path.join(base, filename_ext)

  print(filepath)
  with open(filepath, "w", encoding='utf-8') as outfile:
    json.dump(mem_dict, outfile, ensure_ascii=False, indent=2)


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