# Write your solution here
from datetime import datetime
import string

def is_it_valid(pic : str):
    day = int(pic[0:2])
    month = int(pic[2:4])
    year = int(pic[4:6])
    century = pic[6]
    pid = int(pic[7:10])
    controlNumber = pic[10]
    stringReference = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    centuryReference = {"+" : 1800, "-":1900,"A":2000}

    try:
        remainder = int((pic[0:6]) + pic[7:10]) % 31
        getControlNumber = stringReference[remainder]
        
        if (datetime(centuryReference.get(century)+year,month,day) and 
            century in centuryReference and
            getControlNumber == controlNumber) and len(pic) < 12:
            return True
        else:
            return False
        
    except ValueError:
        return False
if __name__ == "__main__":
    print(is_it_valid("080842-720N"))
