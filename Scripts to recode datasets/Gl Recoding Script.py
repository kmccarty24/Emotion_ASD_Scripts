# Only works on Win32 distributions of python on Windows. 
# On OSX and Linux Kernels, must instsall via homebrew

# Import Necessary Modules

import numpy as np
import pandas as pd

import os

# Read CSV / Ammend missing values
wd = os.getcwd()
raw_csv = pd.read_csv(wd + '\\GL Recode Frame.csv')
gldata = raw_csv.fillna('missing') 

#   List of original headers
OriginalHeader = ['GL1','GL2','GL3','GL4','GL5','GL6']

for c in gldata:
    col_name = str(c)+"_scored" 
    score = []
    if c in OriginalHeader:
        print "In Original Header"
        for i in gldata[c]:
            if i == 1:
                score.append(2)
            elif i == 2:
                score.append(1)
            elif i == 3:
                score.append(0)
            elif i == 'missing' or i == '' or i == None:
                score.append(-999)
            else:
                score.append(i)
        gldata[col_name] = score

output = gldata.to_csv(str(wd + '\\Gl Rescored.csv'))