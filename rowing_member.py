import pickle
import os

class rowing_member():
    
    def __init__(self, dict):
        ## Need to write functions to always source from dict to avoid lots of conversions
        self.rowing_member_data = dict
        self.name_changed = False
        self.display_member()

    def get_member_name(self):
        return self.rowing_member_data["Name"]
    
    def get_member_side(self):
        return self.rowing_member_data["Side"]
    
    def get_member_history(self):
        return self.rowing_member_data["History"]

    def display_member(self):
        """Just prints the rowing member attributes"""
        print(f"Name        : {self.get_member_name()}")
        print(f"Rowing side : {self.get_member_side()}")
        print(f"History     : {self.get_member_history()}")

    def set_member_name(self, new_name):
        self.old_member_name = self.rowing_member_data["Name"]
        self.rowing_member_data["Name"] = new_name
        print(f"old name {self.old_member_name} -> new name {new_name}")

