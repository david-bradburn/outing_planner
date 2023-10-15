import os
import rowing_member
import json
import time




class outing_planner():

    def __init__(self):
        # self.loaded_member
        
        self.main()
    
    def main(self):
        while True:
            self.main_menu()


    def main_menu(self):
        print("------------------------------------------------------")

        try: 
            op = int(input("Please enter operation: \n   0 : create and outing\n   2 : display member \n   9 : quit program\n"))


            match op:
                case 0:
                    # Create outing
                    ...
                
                case 1: # Create a member
                    member_name = str(input("Please enter member name : "))
                    member_side = str(input(f"Please enter {member_name}'s rowing side: "))
                    member_ID   = int(time.time()) ## might want to think of a better userid method? nah this is fine
                    # print(member_ID)
                    member_dict = {"Name":member_name,
                                   "Side":member_side,
                                   "ID"  :member_ID,
                                   "History" : []}

                    # print(member_dict)
                    self.save_member(member_dict)


                case 2: # view /edit member // load and edit
                    mem_name = input("Please enter the member you wish to view : ")
                    self.loaded_member_raw = self.load_member(mem_name)
                    self.loaded_member = rowing_member.rowing_member(self.loaded_member_raw)

                case 9:
                    quit()

                case _:
                    raise ValueError

        except ValueError as ex:
            print("Please enter valid value", ex)


    def create_outing(self):
        ...

    def save_member(self, member_data: dict):
        dir_path = os.path.dirname(os.path.realpath(__file__))

        root = "member_data"
        filename_ext = f"{member_data['Name']}.json"

        base = os.path.join(dir_path, root)
        filepath = os.path.join(base, filename_ext)
        json_object = json.dumps(member_data, indent=4)

        print(filepath)
        with open(filepath, "w") as outfile:
            outfile.write(json_object)


    def load_member(self, filename):
        dir_path = os.path.dirname(os.path.realpath(__file__))

        root = "member_data"
        filename_ext = f"{filename}.json"

        base = os.path.join(dir_path, root)
        filepath = os.path.join(base, filename_ext)

        print(filepath)

        try:
            with open(filepath, 'r') as f:
                return json.load(f)
        except Exception as ex:
            print("Error during loading object (possiblt does not exist):", ex)
            return None
    


outing_planner()