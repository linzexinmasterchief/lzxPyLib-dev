#Last modify [2017-8-24|13-06]
#@Auther Michael 3778
#@version 1.8

# check if input type equals to TYPE
#TYPE: int -> 0
#      string -> " "
#      bool -> false
def isSameType(Input1 = 0, Input2 = 0):
    return type(Input1) == type(Input2)
# no error in this part [2017-8-24|13-06] by @Michael 3778

# check if enter is number (float)
def FloatInput(prompt = "enter a float: ", errorMsg = "not a float"):
    while True:
        try:
            enter = float(input(prompt))
            return enter
        except:
            pass
        print(errorMsg)
# no error in this part [2017-8-24|13-06] by @Michael 3778

# check if enter is number (int)
def IntInput(prompt = "enter a integer: ", errorMsg = "not a integer"):
    while True:
        try:
            enter = FloatInput(prompt, "not a number")
            if enter.is_integer():
                enter = int(enter)
                return enter
        except:
            pass
        print(errorMsg)
# no error in this part [2017-8-24|13-06] by @Michael 3778

# check if enter is string
def StringInput(prompt = "enter a string", errorMsg = "not a string"):
    while True:
        enter = input(prompt)
        if isSameType(enter, " "):
            enter = str(enter)
            return enter
        print(errorMsg)
        continue
# no error in this part [2017-8-24|13-06] by @Michael 3778

# check if enter is binary
def BinInputAsStr(prompt = "enter a binary: ", errorMsg = "not a binary"):
    isBinary = False
    while not isBinary:
        binary = StringInput(prompt)
        isBinary = True
        for i in binary:
            if i == "1" or i == "0":
                pass
            else:
                isBinary = False
                print(errorMsg)
                break
    return binary
# no error in this part [2017-9-25|10-08] by @Michael 3778

#======================[test field]=======================