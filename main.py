import pickle
import os
# from enum import Enum


class rowing_member():
    
    def __init__(self):
        self.enter_member_name()
        self.enter_side()
        self.display_member()


    def enter_member_name(self):
        self.mem_name = str(input("Enter member name (i.e. first last): "))


    # def enter_data(self, msg: str, options: list):

    #     for i in options:
    #         options_list

    #     temp = input(f"Enter {self.mem_name}'s rowing side (stroke, bow, either, n/a)")


    def enter_side(self): # sweep only
        # self.mem_side 
        temp = input(f"Enter {self.mem_name}'s rowing side (stroke, bow, either or n/a): ")
        match temp:

            case "stroke" | "bow" | "either" | "n/a":
                self.mem_side = temp
            case _:
                print("Please enter valid side (stroke, bow, either or n/a): ")
                self.enter_side()


    def check_if_file_exists(self, path, filename):
        """Checks to see if a given file exits at a given location"""
        for root, dir1, files in os.walk(path):
            # print(root)
            # print(dir1)
            # print(files)
            if filename in files:
                print(filename)
                return True

        # print("file does not exist")
        return False


    def display_member(self):
        """Just prints the rowing member attributes"""
        print(f"Name       : {self.mem_name}")
        print(f"Rowing side: {self.mem_side}")


    def save_object(self, overwrite = False):

        dir_path = os.path.dirname(os.path.realpath(__file__))

        root = "member_data"
        filename = f"{self.mem_name}.pickle"

        base = os.path.join(dir_path, root)
        filepath = os.path.join(base, filename)

        if(not overwrite):
            # print(f"checking if file exitsts in {base}")
            file_exists = self.check_if_file_exists(base, filename)
            if(file_exists):
                print(f"filename {self.mem_name} already exists please rename")
                self.enter_member_name()
                self.save_object()
                return

        try:

            with open(filepath, "wb") as f:
                pickle.dump(self, f, protocol=pickle.HIGHEST_PROTOCOL)
        except Exception as ex:
            print("Error during pickling object (Possibly unsupported):", ex)



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
                    obj = rowing_member()
                    obj.save_object()
                case 2: # view /edit member // load and edit
                    mem_name = input("Please enter the member you wish to view / make a change: ")
                    self.loaded_mem_obj, valid_mem = self.load_object(mem_name)

                    if not valid_mem:
                        return
                    
                    self.loaded_mem_obj.display_member()
                    self.edit_member()
                    



                case 9:
                    quit()

                case _:
                    raise ValueError

        except ValueError:
            print("Please enter valid value")

    def edit_member(self):
        ip = str(input(f"Would you like to edit member ({self.loaded_mem_obj.mem_name})? y/n: "))
    
        match ip.lower():
            case "n":
                return
            case "y":
                self.edit_member()
            case _
            
        op = int(input("Please enter which element to edit: \n   0 : name\n   1 : side\n"))


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