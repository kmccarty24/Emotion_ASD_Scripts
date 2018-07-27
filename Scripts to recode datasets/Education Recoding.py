# Only works on Win32 distributions of python on Windows. 
# On OSX and Linux Kernels, must instsall via homebrew

# Import Necessary Modules

import numpy as np
import pandas as pd

import os

# Read CSV / Ammend missing values
wd = os.getcwd()
raw_csv = pd.read_csv(wd + '\\education data.csv', skip_blank_lines = False)
edudata = raw_csv.fillna('missing') 

#   List of original headers
EduHeader = ['edu']

for c in edudata:
    col_name = str(c)+"_scored" 
    score = []
    if c in EduHeader:
        print("In Original Condition Header")
        for i in edudata[c]:
            print(i)
            # print type(i)
            if i == 1:
                score.append(2)
            elif i == 2:
                score.append(4)
            elif i == 3:
                score.append(4)
            elif i == 4:
                score.append(8)
            elif i == 5:
                score.append(9)
            elif i == 6:
                score.append(5)
            elif i == 7:
                score.append(6)
            elif i == 8:
                score.append(7)
            elif i == 9:
                score.append(3)
            elif i == 10:
                score.append(1)
            elif i == 'missing' or i == '' or i == None:
                print('in missing')
                score.append(-999)
            else:
                print('else')
                score.append(i)
        edudata[col_name] = score

output = edudata.to_csv(str(wd + '\\edu rescored.csv'))
