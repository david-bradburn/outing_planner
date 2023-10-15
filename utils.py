
def print_ex_catch(msg: str, error_type: Exception):
    "Doesn't work if the error occurs in the message string :("
    try:
        print(msg)
    except:
        pass

