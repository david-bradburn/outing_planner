import pickle
import os

class rowing_member():
    
    def __init__(self):
        self.enter_member_name()
        self.enter_side()
        self.display_member()


    # def enter_member_name(self):
    #     self.mem_name = str(input("Enter member name (i.e. first last): "))


    # def enter_side(self): # sweep only
    #     # self.mem_side 
    #     temp = input(f"Enter {self.mem_name}'s rowing side (stroke, bow, either or n/a): ")
    #     match temp:

    #         case "stroke" | "bow" | "either" | "n/a":
    #             self.mem_side = temp
    #         case _:
    #             print("Please enter valid side (stroke, bow, either or n/a): ")
    #             self.enter_side()


    def check_if_file_exists(self, path, filename):
        """Checks to see if a given file exits at a given location"""
        for root, dir1, files in os.walk(path):
            if filename in files:
                print(filename)
                return True

        # print("file does not exist")
        return False


    def display_member(self):
        """Just prints the rowing member attributes"""
        print(f"Name        : {self.mem_name}")
        print(f"Rowing side : {self.mem_side}")

