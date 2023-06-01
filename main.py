import pickle
import os
# from enum import Enum


class rowing_member():
    
    def __init__(self):
        self.create_member()
        self.enter_side()
        self.enter_sculling()
        self.enter_foot_steering()

        if self.can_scull == "yes":
            self.enter_1x_proficiency() 
        else:
            self.can_1x = "no"

        self.enter_coxing_ability()

        self.display_member()


    def create_member(self):
        self.mem_name = input("Enter member name (i.e. first last): ")


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


    def enter_sculling(self):
        temp = input(f"Can {self.mem_name} scull (yes/no): ")
        match temp:
            case "yes" | "no":
                self.can_scull = temp
            case _:
                print("Please enter a valid state (yes or no): ")
                self.enter_sculling()


    def enter_foot_steering(self):
        temp = input(f"Can {self.mem_name} foot steer (yes/no): ")
        match temp:
            case "yes" | "no":
                self.can_foot_steer = temp
            case _:
                print("Please enter a valid state (yes or no): ")
                self.enter_foot_steering()


    def enter_1x_proficiency(self):
        temp = input(f"Is {self.mem_name} confident in a 1x (yes/no): ")
        match temp:
            case "yes" | "no":
                self.can_1x = temp
            case _:
                print("Please enter a valid state (yes or no): ")
                self.enter_1x_proficiency()


    def enter_coxing_ability(self):
        temp = input(f"Can {self.mem_name} cox (yes/no): ")
        match temp:
            case "yes" | "no":
                self.can_cox = temp
            case _:
                print("Please enter a valid state (yes or no): ")
                self.enter_coxing_ability()


    def check_if_file_exists(self, path, filename):
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
        print(f"Name: {self.mem_name}")
        print(f"Rowing side: {self.mem_side}")
        print(f"Can scull: {self.can_scull}")
        print(f"Can foot steer: {self.can_foot_steer}")
        print(f"Confident in a 1x: {self.can_1x}")
        print(f"Can cox: {self.can_cox}")


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
                self.create_member()
                self.save_object()
                return

        try:

            with open(filepath, "wb") as f:
                pickle.dump(self, f, protocol=pickle.HIGHEST_PROTOCOL)
        except Exception as ex:
            print("Error during pickling object (Possibly unsupported):", ex)



class outing_planner():

    def __init__(self):

        self.main_menu()


    def main_menu(self):
        print("------------------------------------------------------")

        try: 
            op = int(input("Please enter operation: \n   0 : create and outing\n   1 : create member\n   2 : view / edit member \n   9 : quit program\n"))


            match op:

                case 0: # Create outing
                    ...

                case 1: # create_member + save
                    obj = rowing_member()
                    obj.save_object()
                case 2: # view /edit member // load and edit
                    mem_filename = input("Please enter the member you wish to view / make a change: ")
                    # print(type(mem_filename))
                    # temp_name = f"{mem_filename}.pickle"
                    # print(temp_name)
                    obj2 = self.load_object(temp_name)
                    obj2.display_member()


                case 9:
                    quit()

                case _:
                    raise ValueError

        except ValueError:
            print("Please enter valid value")
            self.main_menu()


        self.main_menu()


    def load_object(self, filename):

        dir_path = os.path.dirname(os.path.realpath(__file__))

        root = "member_data"
        filename = f"{self.mem_name}.pickle"

        base = os.path.join(dir_path, root)
        filepath = os.path.join(base, filename)

        try:
            with open(filepath, "rb") as f:
                return pickle.load(f)
        except Exception as ex:
            print("Error during unpickling object (Possibly unsupported):", ex)


outing_planner()