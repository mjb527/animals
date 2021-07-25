# !usr/bin/python3

def getYesNoInput():
    res = input("Enter Yes or No\n")
    if(res.lower().strip() == "yes"):
        return True
    elif(res.lower().strip() == "no"):
        return False
    else: getYesNoInput()
