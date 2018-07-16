# Only works on Win32 distributions of python on Windows. 
# On OSX and Linux Kernels, must instsall via homebrew

# Import Necessary Modules

import numpy as np
import pandas as pd

import os

# Read CSV / Ammend missing values
wd = os.getcwd()
raw_csv = pd.read_csv(wd + '\\Condition Original.csv', skip_blank_lines = False)
conddata = raw_csv.fillna('missing') 

#   List of original headers
CondHeader = ['Condition']

for c in conddata:
    col_name = str(c)+"_scored" 
    score = []
    if c in CondHeader:
        print "In Original Condition Header"
        for i in conddata[c]:
            if i == 1:
                score.append(3)
            elif i == 2:
                score.append(2)
            elif i == 3:
                score.append(1)
            elif i == 4:
                score.append(5)
            elif i == 5:
                score.append(6)
            elif i == 6:
                score.append(9)
            elif i == 7:
                score.append(7)
            elif i == 8:
                score.append(8)
            elif i == 'missing' or i == '' or i == None:
                score.append(-999)
            else:
                score.append(i)
        conddata[col_name] = score

output = conddata.to_csv(str(wd + '\\Cond Rescored.csv'))