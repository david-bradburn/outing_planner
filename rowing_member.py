import pickle
import os

class rowing_member():
    
    def __init__(self):
        self.enter_member_name()
        self.enter_side()
        self.display_member()


    def enter_member_name(self):
        self.mem_name = str(input("Enter member name (i.e. first last): "))


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
            if filename in files:
                print(filename)
                return True

        # print("file does not exist")
        return False


    def display_member(self):
        """Just prints the rowing member attributes"""
        print(f"Name        : {self.mem_name}")
        print(f"Rowing side : {self.mem_side}")

    def del_object(self, name):
        ...


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