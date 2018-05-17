def is_loop_str(myinput):
    if isinstance(myinput, int):
        mystr = str(myinput)
    elif isinstance(myinput, str):
        mystr = myinput
    else:
        print("Error, input not a string or an integer")
        return False
    reverse_list= list(mystr)
    reverse_list.reverse()
    if mystr == "".join(reverse_list):
        return True
    else:
        return False

print is_loop_str(12321)
print is_loop_str("abkadsn")
print is_loop_str([1,2,1])
