# Only works on Win32 distributions of python on Windows.
# On OSX and Linux Kernels, must instsall via homebrew

# Import Necessary Modules

# Adaption for AQ_10

import numpy as np
import pandas as pd
import os


# Read CSV / Ammend missing values
wd = os.getcwd()
raw_csv = pd.read_csv('C:\\Users\Owner\\Desktop\\Mark this for KM\\AQ10_template.csv')
aqdata = raw_csv.fillna(np.nan)
aqdata = raw_csv

#   List of columns which 'definitely agree','slightly agree' = 1
agree = ['aq10_1', 'aq10_7', 'aq10_8', 'aq10_10']

#   List of collumns which 'definitely disagree','slightly disagree' = 1
disagree = ['aq10_2', 'aq10_3', 'aq10_4', 'aq10_5', 'aq10_6', 'aq10_9']

# complete = agree + disagree

wordsYes = ['definitely agree', 'slightly agree']
wordsNo = ['definitely disagree', 'slightly disagree']

for c in aqdata:
    col_name = str(c)+"_scored"
    score = []
    if c in agree:
        print "in agree"
        for i in aqdata[c]:
            if str(i) in ['definitely agree', 'Definitely Agree', '1']:
                score.append(1)
            elif str(i) in ['slightly agree', 'Slightly Agree', '2']:
                score.append(1)
            elif str(i) in ['slightly disagree', 'Slightly Disagree', '3']:
                score.append(0)
            elif str(i) in ['definitely disagree', 'Definitely Disagree', '4']:
                score.append(0)
            elif str(i) in ['neutral', '2.5']:
                score.append(0.5)
            elif str(i) in ['missing', '0', None]:
                score.append(np.nan)
            else:
                score.append(i)
        aqdata[col_name] = score

    if c in disagree:
        print"in disagree"
        for i in aqdata[c]:
            if str(i) in ['definitely agree', 'Definitely Agree', '1']:
                score.append(0)
            elif str(i) in ['slightly agree', 'Slightly Agree', '2']:
                score.append(0)
            elif str(i) in ['slightly disagree', 'Slightly Disagree', '3']:
                score.append(1)
            elif str(i) in ['definitely disagree', 'Definitely Disagree', '4']:
                score.append(1)
            elif str(i) in ['neutral', '2.5']:
                score.append(0.5)
            elif str(i) in ['missing', '0', None]:
                score.append(np.nan)
            else:
                score.append(i)
        aqdata[col_name] = score

# Total
AQ10_Total = ['aq10_1_scored', 'aq10_2_scored',
         'aq10_3_scored', 'aq10_4_scored',
         'aq10_5_scored', 'aq10_6_scored',
         'aq10_7_scored', 'aq10_8_scored',
         'aq10_9_scored', 'aq10_10_scored']

aqdata['AQ10_Total'] = aqdata[AQ10_Total].astype(float).sum(axis=1)

output = aqdata.to_csv(str('C:\\Users\Owner\\Desktop\\Mark this for KM\\karen_september_AQ10_data.csv'))
# na_rep = '-999'
