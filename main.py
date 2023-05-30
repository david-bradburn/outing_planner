import pickle
from enum import Enum

class rowing_side(Enum):
    stroke = 0
    bow = 1
    either = 2


 
class MyClass():
    def __init__(self, param):
        self.param = param
        self.name = ""
        self.side =     
 
def save_object(obj):
    try:
        with open("data.pickle", "wb") as f:
            pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        print("Error during pickling object (Possibly unsupported):", ex)
 

def load_object(filename):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except Exception as ex:
        print("Error during unpickling object (Possibly unsupported):", ex)
 



obj = MyClass(10)
obj.name = "steve"
save_object(obj)

obj2 = load_object("data.pickle")
 
print(obj2.param)
print(obj2.name)
# print(isinstance(obj, MyClass))



