import pickle
import os
import rowing_member
# from enum import Enum



class outing_planner():

    def __init__(self):

        self.main()
    
    def main(self):

        while True:
            self.main_menu()


    def main_menu(self):
        print("------------------------------------------------------")

        try: 
            op = int(input("Please enter operation: \n   0 : create and outing\n   1 : create member\n   2 : display/edit member \n   9 : quit program\n"))


            match op:

                case 0: # Create outing
                    ...

                case 1: # create_member + save
                    obj = rowing_member.rowing_member()
                    obj.save_object()
                case 2: # view /edit member // load and edit
                    mem_name = input("Please enter the member you wish to view / make a change: ")
                    self.loaded_mem_obj, valid_mem = self.load_object(mem_name)

                    if not valid_mem:
                        print("Error in loading")
                        return 
                    
                    self.loaded_mem_obj.display_member()
                    edit_mem = self.edit_member_ask()
                    if edit_mem:
                        self.edit_member()
                    



                case 9:
                    quit()

                case _:
                    raise ValueError

        except ValueError:
            print("Please enter valid value")

    def edit_member_ask(self):
        ip = str(input(f"Would you like to edit member ({self.loaded_mem_obj.mem_name})? y/n: "))
        try:
            match ip.lower():
                case "n":
                    return False
                case "y":
                    return True
                case _:
                    raise ValueError
        except ValueError:
            print("Please enter a valid valu")
            self.edit_member_ask()
            
    def edit_member(self):
        ip = int(input("Please enter which element to edit: \n   0 : name\n   1 : side\n   9 : save & exit"))

        name_changed = False
        try:
            match ip:
                case 0:
                    old_name = self.loaded_mem_obj.mem_name
                    self.loaded_mem_obj.enter_member_name()
                    name_changed = True
                case 1:
                    self.loaded_mem_obj.enter_side()
                case 9:
                    self.loaded_mem_obj.save_object(name_changed)

                case _:
                    raise ValueError

        except ValueError:
            print("Please enter a valid value 0 or 1")   
            self.edit_member()
        


    def create_outing(self):
        ...

    def load_object(self, filename):

        dir_path = os.path.dirname(os.path.realpath(__file__))

        root = "member_data"
        filename_ext = f"{filename}.pickle"

        base = os.path.join(dir_path, root)
        filepath = os.path.join(base, filename_ext)

        print(filepath)
        try:
            with open(filepath, "rb") as f:
                return pickle.load(f), True
        except Exception as ex:
            print("Error during unpickling object (Possibly unsupported):", ex)
            return None, False


outing_planner()