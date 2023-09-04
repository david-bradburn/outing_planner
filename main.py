import os
import rowing_member
import json




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


                case 2: # view /edit member // load and edit
                    mem_name = input("Please enter the member you wish to view : ")
                    self.loaded_member_raw = self.load_member(mem_name)
                    print(self.loaded_member_raw)
                    self.loaded_member = rowing_member.rowing_member(self.loaded_member_raw)

                case 9:
                    quit()

                case _:
                    raise ValueError

        except ValueError as ex:
            print("Please enter valid value", ex)


    def create_outing(self):
        ...

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