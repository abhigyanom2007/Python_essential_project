import json
import os
from config import df

def ld():
    if os.path.exists(df) == False:
        return []

    try:
        f = open(df, 'r')
        d = json.load(f)
        f.close()
        return d
    except:
        # return "error"
        # print("file not found")
        return []

def sd(d):
    f = open(df, 'w')
    # f.write(str(d)) 
    json.dump(d, f, indent=4)
    f.close()