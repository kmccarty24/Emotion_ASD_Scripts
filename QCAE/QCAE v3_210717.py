# Only works on Win32 distributions of python on Windows. 
# On OSX and Linux Kernels, must instsall via homebrew

# Import Necessary Modules

import numpy as np
import pandas as pd

import os

# Read CSV / Ammend missing values
wd = os.getcwd()
raw_csv = pd.read_csv(wd + '\\Rachel Smith QCAE.csv', skip_blank_lines = False)
qcaedata = raw_csv.fillna('missing') 
qcaedata = raw_csv
#   List of columns which 'definitely agree','slightly agree' = 1 
forward = ['QCAE_15', 'QCAE_16','QCAE_19','QCAE_20','QCAE_21','QCAE_22',
           'QCAE_24','QCAE_25','QCAE_26','QCAE_27','QCAE_3','QCAE_4',
           'QCAE_5','QCAE_6','QCAE_18','QCAE_28','QCAE_30','QCAE_31',
           'QCAE_8','QCAE_9','QCAE_13','QCAE_14','QCAE_7','QCAE_10',
           'QCAE_12','QCAE_23','QCAE_11']

#   List of collumns which 'definitely disagree','slightly disagree' = 1 
reverse = ['QCAE_1','QCAE_2','QCAE_17','QCAE_29']

# 4 point likert scale: strongly agree = 4; slightly agree = 3; 
# slightly disagree = 2; strongly disagree = 1

wordsForward = ['strongly agree', 'slightly agree']
wordsReverse = ['strongly disagree', 'slightly disagree']

# Fill in these numbers, fingers crossed the data actually saved

# Count mising values BEFORE the scored cols but dont add to df until the end
noMissing = qcaedata.isnull().sum(axis=1).tolist()

for c in qcaedata:
    col_name = str(c)+"_scored" 
    score = []
    if c in forward:
        print "forward"
        for i in qcaedata[c]:
            if i == 'strongly agree' or i == 1:
                score.append(4)
            elif i == 'slightly agree' or i == 2:
                score.append(3)    
            elif i == 'slightly disagree' or i == 3:
                score.append(2)
            elif i == 'strongly disagree' or i == 4:
                score.append(1)    
            elif i == 'neutral' or i == 2.5:
                score.append(2.5)
            elif i == 'missing' or i == '' or i == None:
                score.append(0)
            else:
                score.append(i)
        qcaedata[col_name] = score
                        
    if c in reverse:
        print"reverse"
        for i in qcaedata[c]:
            if i == 'strongly agree' or i == 1:
                score.append(1)
            elif i == 'slightly agree' or i == 2:
                score.append(2)    
            elif i == 'slightly disagree' or i == 3:
                score.append(3)
            elif i == 'strongly disagree' or i == 4:
                score.append(4)    
            elif i == 2.5:
                score.append(2.5)
            elif i == 'missing' or i == '0' or i == None:
                score.append(0)
            else:
                score.append(i)
        qcaedata[col_name] = score



# Sub-Scales
#################################################

allCols = qcaedata.columns.tolist()


#################################################

# Cognitive Empathy Subscale
CogEmp = ['QCAE_15_scored', 'QCAE_16_scored',
          'QCAE_19_scored', 'QCAE_20_scored',
          'QCAE_21_scored', 'QCAE_22_scored',
          'QCAE_24_scored', 'QCAE_25_scored',
          'QCAE_26_scored', 'QCAE_27_scored',
          'QCAE_1_scored', 'QCAE_3_scored',
          'QCAE_4_scored', 'QCAE_5_scored',
          'QCAE_6_scored', 'QCAE_18_scored',
          'QCAE_28_scored', 'QCAE_30_scored',
          'QCAE_31_scored']

qcaedata['CogEmp'] = qcaedata[CogEmp].sum(axis=1)

# Affective Empathy Subscale
AffEmp = ['QCAE_8_scored', 'QCAE_9_scored',
          'QCAE_13_scored', 'QCAE_14_scored',
          'QCAE_7_scored', 'QCAE_10_scored',
          'QCAE_12_scored', 'QCAE_23_scored',
          'QCAE_2_scored', 'QCAE_11_scored',
          'QCAE_17_scored', 'QCAE_29_scored']

qcaedata['AffEmp'] = qcaedata[AffEmp].sum(axis=1)

# Cog Empathy Subscales

# Perspective Taking Subscale (15, 16, 19, 20, 21, 22, 24, 25, 26, 27)
PerTake = ['QCAE_15_scored', 'QCAE_16_scored',
           'QCAE_19_scored', 'QCAE_20_scored',
           'QCAE_21_scored', 'QCAE_22_scored',
           'QCAE_24_scored', 'QCAE_25_scored',
           'QCAE_26_scored', 'QCAE_27_scored']

qcaedata['PerTake'] = qcaedata[PerTake].sum(axis=1)

# Online Simulation Subscale (1, 3, 4, 5, 6, 18, 28, 30, 31)
Online = ['QCAE_1_scored', 'QCAE_3_scored',
          'QCAE_4_scored', 'QCAE_5_scored',
          'QCAE_6_scored', 'QCAE_18_scored',
          'QCAE_28_scored', 'QCAE_30_scored',
          'QCAE_31_scored']

qcaedata['Online'] = qcaedata[Online].sum(axis=1)

# Affective Empathy Subscales

# Emotion Contagion Subscale  (8, 9, 13, 14)
EmoCont = ['QCAE_8_scored', 'QCAE_9_scored',
           'QCAE_13_scored', 'QCAE_14_scored']

qcaedata['EmoCont'] = qcaedata[EmoCont].sum(axis=1)

# Proximinal Responsivity Subscale (7, 10, 12, 23)
ProxRes = ['QCAE_7_scored', 'QCAE_10_scored',
           'QCAE_12_scored', 'QCAE_23_scored']

qcaedata['ProxRes'] = qcaedata[ProxRes].sum(axis=1)

# Peripheral Responsivity Subscale (2, 11, 17, 29)
PerfRes = ['QCAE_2_scored', 'QCAE_11_scored',
           'QCAE_17_scored', 'QCAE_29_scored']

qcaedata['PerfRes'] = qcaedata[PerfRes].sum(axis=1)

# Overall
QCAETot = ['QCAE_1_scored', 'QCAE_2_scored',
           'QCAE_3_scored', 'QCAE_4_scored',
           'QCAE_5_scored', 'QCAE_6_scored',
           'QCAE_7_scored', 'QCAE_8_scored',
           'QCAE_9_scored', 'QCAE_10_scored',
           'QCAE_11_scored', 'QCAE_12_scored',
           'QCAE_13_scored', 'QCAE_14_scored',
           'QCAE_15_scored', 'QCAE_16_scored',
           'QCAE_17_scored', 'QCAE_18_scored',
           'QCAE_19_scored', 'QCAE_20_scored',
           'QCAE_21_scored', 'QCAE_22_scored',
           'QCAE_23_scored', 'QCAE_24_scored',
           'QCAE_25_scored', 'QCAE_26_scored',
           'QCAE_27_scored', 'QCAE_28_scored',
           'QCAE_29_scored', 'QCAE_30_scored',
           'QCAE_31_scored']

qcaedata['QCAETot'] = qcaedata[QCAETot].sum(axis=1)

# Print to DF

qcaedata['noMissing'] = noMissing


# would like it to have a column for the missing score
# do not want '-999' to be counted

output = qcaedata.to_csv(str(wd + '\\Rachel Smith QCAE_scored.csv'))
# na_rep = '-999'