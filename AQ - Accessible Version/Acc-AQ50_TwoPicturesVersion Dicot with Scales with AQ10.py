# Only works on Win32 distributions of python on Windows. 
# On OSX and Linux Kernels, must instsall via homebrew

# Import Necessary Modules

import numpy as np
import pandas as pd

import os

#Mark scheme for Version A  (2 pictures)

# Read CSV / Ammend missing values
wd = os.getcwd()
raw_csv = pd.read_csv(wd + '\\AccAQ_Data_Frame_TwoVersions.csv')
aqdata = raw_csv.fillna('missing')

#   List of columns which 'definitely agree','slightly agree' = 1 
#   Columns where picture selected indicates ASD traits

#   Columns where Picture 1 = Score of 1
agree_a = ['AccAQ_A_2', 'AccAQ_A_4', 'AccAQ_A_5', 'AccAQ_A_6', 'AccAQ_A_9', 
           'AccAQ_A_12', 'AccAQ_A_13', 'AccAQ_A_16', 'AccAQ_A_18', 'AccAQ_A_19', 'AccAQ_A_23', 
           'AccAQ_A_25', 'AccAQ_A_28', 'AccAQ_A_29', 'AccAQ_A_30', 'AccAQ_A_33', 'AccAQ_A_34', 
           'AccAQ_A_39', 'AccAQ_A_41', 'AccAQ_A_43', 'AccAQ_A_49']

#   List of collumns which 'definitely disagree','slightly disagree' = 1 

#   Columns where Picture 2 = Score of 1
disagree_a = ['AccAQ_A_1', 'AccAQ_A_3', 'AccAQ_A_7', 'AccAQ_A_8', 'AccAQ_A_10',
              'AccAQ_A_11', 'AccAQ_A_14', 'AccAQ_A_15', 'AccAQ_A_17', 'AccAQ_A_20', 'AccAQ_A_21',
              'AccAQ_A_22', 'AccAQ_A_24', 'AccAQ_A_26', 'AccAQ_A_27', 'AccAQ_A_31', 'AccAQ_A_32',
              'AccAQ_A_35', 'AccAQ_A_36', 'AccAQ_A_37', 'AccAQ_A_38', 'AccAQ_A_40', 'AccAQ_A_42',
              'AccAQ_A_44', 'AccAQ_A_45', 'AccAQ_A_46', 'AccAQ_A_47', 'AccAQ_A_48', 'AccAQ_A_50']

# complete = agree + disagree

wordsYes = ['definitely agree', 'slightly agree']
wordsNo = ['definitely disagree', 'slightly disagree']

for c in aqdata:
    col_name = str(c)+"_scored" 
    score = []
    if c in agree_a:
        print "in agree_a"
        for i in aqdata[c]:
            if i == 'definitely agree' or i == 1:
                score.append(1)
            elif i == 'slightly agree' or i == 2:
                score.append(0)    
            elif i == 'slightly disagree' or i == 3:
                score.append(0)
            elif i == 'definitely disagree' or i == 4:
                score.append(0)    
            elif i == 'neutral' or i == 2.5:
                score.append(0.5)
            elif i == 'missing' or i == '' or i == None:
                score.append(None)
            else:
                score.append(i)
        aqdata[col_name] = score
                        
    if c in disagree_a:
        print"in disagree_a"
        for i in aqdata[c]:
            if i == 'definitely agree' or i == 1:
                score.append(0)
            elif i == 'slightly agree' or i == 2:
                score.append(1)    
            elif i == 'slightly disagree' or i == 3:
                score.append(0)
            elif i == 'definitely disagree' or i == 4:
                score.append(0)    
            elif i == 2.5:
                score.append(0.5)
            elif i == 'missing' or i == '0' or i == None:
                score.append(None)
            else:
                score.append(i)
        aqdata[col_name] = score

# Sub-Scales

#'AccAQ_A_1'


# Social-Skills (items 1+ 11+ 13+ 15+ 22+ 36+ 44+ 45+ 47+ 48) 
aqdata['SocialSk_Acc_AQ_A'] = (aqdata['AccAQ_A_1_scored'] + aqdata['AccAQ_A_11_scored'] + 
					           aqdata['AccAQ_A_13_scored'] + aqdata['AccAQ_A_15_scored']+ 
					           aqdata['AccAQ_A_22_scored'] + aqdata['AccAQ_A_36_scored']+ 
					           aqdata['AccAQ_A_44_scored'] + aqdata['AccAQ_A_45_scored']+ 
					           aqdata['AccAQ_A_47_scored'] + aqdata['AccAQ_A_48_scored'])

# Attention Switching (items 2+ 4+ 10+ 16+ 25+ 32+ 34+ 37+ 43+ 46) 
aqdata['AttenSW_Acc_AQ_A'] = (aqdata['AccAQ_A_2_scored'] + aqdata['AccAQ_A_4_scored']+
					          aqdata['AccAQ_A_10_scored'] + aqdata['AccAQ_A_16_scored']+
					          aqdata['AccAQ_A_25_scored'] + aqdata['AccAQ_A_32_scored']+
					          aqdata['AccAQ_A_34_scored'] + aqdata['AccAQ_A_37_scored']+
					          aqdata['AccAQ_A_43_scored'] + aqdata['AccAQ_A_46_scored'])

# Attention to Detail (items 5+ 6+ 9+ 12+ 19+ 23+ 28+ 29+ 30+ 49)
aqdata['ATD_Acc_AQ_A'] = (aqdata['AccAQ_A_5_scored'] + aqdata['AccAQ_A_6_scored']+
				          aqdata['AccAQ_A_9_scored'] + aqdata['AccAQ_A_12_scored']+
				          aqdata['AccAQ_A_19_scored'] + aqdata['AccAQ_A_23_scored']+
				          aqdata['AccAQ_A_28_scored'] + aqdata['AccAQ_A_29_scored']+
				          aqdata['AccAQ_A_30_scored'] + aqdata['AccAQ_A_49_scored'])
  
# Communication (items 7+ 17+ 18+ 26+ 27+ 31+ 33+ 35+ 38+ 39)
aqdata['Commun_Acc_AQ_A'] = (aqdata['AccAQ_A_7_scored'] + aqdata['AccAQ_A_17_scored']+
				             aqdata['AccAQ_A_18_scored'] + aqdata['AccAQ_A_26_scored']+
				             aqdata['AccAQ_A_27_scored'] + aqdata['AccAQ_A_31_scored']+
				             aqdata['AccAQ_A_33_scored'] + aqdata['AccAQ_A_35_scored']+
				             aqdata['AccAQ_A_38_scored'] + aqdata['AccAQ_A_39_scored'])
 
# Imagination (items 3+ 8+ 14+ 20+ 21+ 24+ 40+ 41+ 42+ 50) 
aqdata['Imag_Acc_AQ_A'] = (aqdata['AccAQ_A_3_scored']+aqdata['AccAQ_A_8_scored']+
				           aqdata['AccAQ_A_14_scored']+aqdata['AccAQ_A_20_scored']+
				           aqdata['AccAQ_A_21_scored']+aqdata['AccAQ_A_24_scored']+
				           aqdata['AccAQ_A_40_scored']+aqdata['AccAQ_A_41_scored']+
				           aqdata['AccAQ_A_42_scored']+aqdata['AccAQ_A_50_scored'])

# Total
aqdata['Total_Acc_AQ_A'] =  (aqdata['AccAQ_A_1_scored'] + aqdata['AccAQ_A_2_scored'] + 
				             aqdata['AccAQ_A_3_scored'] + aqdata['AccAQ_A_4_scored'] + 
				             aqdata['AccAQ_A_5_scored'] + aqdata['AccAQ_A_6_scored'] + 
				             aqdata['AccAQ_A_7_scored'] + aqdata['AccAQ_A_8_scored'] + 
				             aqdata['AccAQ_A_9_scored'] + aqdata['AccAQ_A_10_scored'] + 
				             aqdata['AccAQ_A_11_scored'] + aqdata['AccAQ_A_12_scored'] + 
				             aqdata['AccAQ_A_13_scored'] + aqdata['AccAQ_A_14_scored'] + 
				             aqdata['AccAQ_A_15_scored'] + aqdata['AccAQ_A_16_scored'] + 
				             aqdata['AccAQ_A_17_scored'] + aqdata['AccAQ_A_18_scored'] + 
				             aqdata['AccAQ_A_19_scored'] + aqdata['AccAQ_A_20_scored'] + 
				             aqdata['AccAQ_A_21_scored'] + aqdata['AccAQ_A_22_scored'] + 
				             aqdata['AccAQ_A_23_scored'] + aqdata['AccAQ_A_24_scored'] + 
				             aqdata['AccAQ_A_25_scored'] + aqdata['AccAQ_A_26_scored'] + 
				             aqdata['AccAQ_A_27_scored'] + aqdata['AccAQ_A_28_scored'] + 
				             aqdata['AccAQ_A_29_scored'] + aqdata['AccAQ_A_30_scored'] + 
				             aqdata['AccAQ_A_31_scored'] + aqdata['AccAQ_A_32_scored'] + 
				             aqdata['AccAQ_A_33_scored'] + aqdata['AccAQ_A_34_scored'] + 
				             aqdata['AccAQ_A_35_scored'] + aqdata['AccAQ_A_36_scored'] + 
				             aqdata['AccAQ_A_37_scored'] + aqdata['AccAQ_A_38_scored'] + 
				             aqdata['AccAQ_A_39_scored'] + aqdata['AccAQ_A_40_scored'] + 
				             aqdata['AccAQ_A_41_scored'] + aqdata['AccAQ_A_42_scored'] + 
				             aqdata['AccAQ_A_43_scored'] + aqdata['AccAQ_A_44_scored'] + 
				             aqdata['AccAQ_A_45_scored'] + aqdata['AccAQ_A_46_scored'] + 
				             aqdata['AccAQ_A_47_scored'] + aqdata['AccAQ_A_48_scored'] + 
				             aqdata['AccAQ_A_49_scored'] + aqdata['AccAQ_A_50_scored'])

aqdata['ShortForm10_AQ_A'] = (aqdata['AccAQ_A_5_scored']+aqdata['AccAQ_A_28_scored']+
                           aqdata['AccAQ_A_10_scored']+aqdata['AccAQ_A_37_scored']+
                           aqdata['AccAQ_A_26_scored']+aqdata['AccAQ_A_38_scored']+
                           aqdata['AccAQ_A_20_scored']+aqdata['AccAQ_A_40_scored']+
                           aqdata['AccAQ_A_36_scored']+aqdata['AccAQ_A_22_scored'])

#################################################################################

#Mark scheme for version B (picture with 4 responses)

# Read CSV / Ammend missing values
# wd = os.getcwd()
# raw_csv = pd.read_csv(wd + '\\aqdata_2017.csv')
# aqdata = raw_csv.fillna('missing') 

#   List of columns which 'definitely agree','slightly agree' = 1 
agree_b = ['AccAQ_B_2', 'AccAQ_B_4', 'AccAQ_B_5', 'AccAQ_B_6', 'AccAQ_B_7', 
         'AccAQ_B_9', 'AccAQ_B_12', 'AccAQ_B_13','AccAQ_B_16', 'AccAQ_B_18', 
         'AccAQ_B_19', 'AccAQ_B_20', 'AccAQ_B_21', 'AccAQ_B_22','AccAQ_B_23', 
         'AccAQ_B_26', 'AccAQ_B_28', 'AccAQ_B_33', 'AccAQ_B_35', 'AccAQ_B_39',
         'AccAQ_B_41', 'AccAQ_B_42', 'AccAQ_B_43', 'AccAQ_B_45', 'AccAQ_B_46']

#   List of collumns which 'definitely disagree','slightly disagree' = 1 
disagree_b = ['AccAQ_B_1', 'AccAQ_B_3', 'AccAQ_B_8', 'AccAQ_B_10', 'AccAQ_B_11', 
            'AccAQ_B_14', 'AccAQ_B_15', 'AccAQ_B_17', 'AccAQ_B_24', 'AccAQ_B_25',
            'AccAQ_B_27', 'AccAQ_B_29', 'AccAQ_B_30', 'AccAQ_B_31', 'AccAQ_B_32', 
            'AccAQ_B_34', 'AccAQ_B_36', 'AccAQ_B_37', 'AccAQ_B_38', 'AccAQ_B_40', 
            'AccAQ_B_44', 'AccAQ_B_47', 'AccAQ_B_48', 'AccAQ_B_49', 'AccAQ_B_50']

# complete = agree + disagree

wordsYes = ['definitely agree', 'slightly agree']
wordsNo = ['definitely disagree', 'slightly disagree']

for c in aqdata:
    col_name = str(c)+"_scored" 
    score = []
    if c in agree_b:
        print "in agree_b"
        for i in aqdata[c]:
            if i == 'definitely agree' or i == 1:
                score.append(1)
            elif i == 'slightly agree' or i == 2:
                score.append(1)    
            elif i == 'slightly disagree' or i == 3:
                score.append(0)
            elif i == 'definitely disagree' or i == 4:
                score.append(0)    
            elif i == 'neutral' or i == 2.5:
                score.append(0.5)
            elif i == 'missing' or i == '' or i == None:
                score.append(None)
            else:
                score.append(i)
        aqdata[col_name] = score
                        
    if c in disagree_b:
        print"in disagree_b"
        for i in aqdata[c]:
            if i == 'definitely agree' or i == 1:
                score.append(0)
            elif i == 'slightly agree' or i == 2:
                score.append(0)    
            elif i == 'slightly disagree' or i == 3:
                score.append(1)
            elif i == 'definitely disagree' or i == 4:
                score.append(1)    
            elif i == 2.5:
                score.append(0.5)
            elif i == 'missing' or i == '0' or i == None:
                score.append(None)
            else:
                score.append(i)
        aqdata[col_name] = score

# Sub-Scales

# Social-Skills (items 1+ 11+ 13+ 15+ 22+ 36+ 44+ 45+ 47+ 48) 
aqdata['SocialSk_Acc_AQ_B'] = (aqdata['AccAQ_B_1_scored'] + aqdata['AccAQ_B_11_scored'] + 
                               aqdata['AccAQ_B_13_scored'] + aqdata['AccAQ_B_15_scored']+ 
                               aqdata['AccAQ_B_22_scored'] + aqdata['AccAQ_B_36_scored']+ 
                               aqdata['AccAQ_B_44_scored'] + aqdata['AccAQ_B_45_scored']+ 
                               aqdata['AccAQ_B_47_scored'] + aqdata['AccAQ_B_48_scored'])

# Attention Switching (items 2+ 4+ 10+ 16+ 25+ 32+ 34+ 37+ 43+ 46) 
aqdata['AttenSW_Acc_AQ_B'] = (aqdata['AccAQ_B_2_scored'] + aqdata['AccAQ_B_4_scored']+
                              aqdata['AccAQ_B_10_scored'] + aqdata['AccAQ_B_16_scored']+
                              aqdata['AccAQ_B_25_scored'] + aqdata['AccAQ_B_32_scored']+
                              aqdata['AccAQ_B_34_scored'] + aqdata['AccAQ_B_37_scored']+
                              aqdata['AccAQ_B_43_scored'] + aqdata['AccAQ_B_46_scored'])

# Attention to Detail (items 5+ 6+ 9+ 12+ 19+ 23+ 28+ 29+ 30+ 49)
aqdata['ATD_Acc_AQ_B'] = (aqdata['AccAQ_B_5_scored'] + aqdata['AccAQ_B_6_scored']+
                          aqdata['AccAQ_B_9_scored'] + aqdata['AccAQ_B_12_scored']+
                          aqdata['AccAQ_B_19_scored'] + aqdata['AccAQ_B_23_scored']+
                          aqdata['AccAQ_B_28_scored'] + aqdata['AccAQ_B_29_scored']+
                          aqdata['AccAQ_B_30_scored'] + aqdata['AccAQ_B_49_scored'])
  
# Communication (items 7+ 17+ 18+ 26+ 27+ 31+ 33+ 35+ 38+ 39)
aqdata['Commun_Acc_AQ_B'] = (aqdata['AccAQ_B_7_scored'] + aqdata['AccAQ_B_17_scored']+
                             aqdata['AccAQ_B_18_scored'] + aqdata['AccAQ_B_26_scored']+
                             aqdata['AccAQ_B_27_scored'] + aqdata['AccAQ_B_31_scored']+
                             aqdata['AccAQ_B_33_scored'] + aqdata['AccAQ_B_35_scored']+
                             aqdata['AccAQ_B_38_scored'] + aqdata['AccAQ_B_39_scored'])
 
# Imagination (items 3+ 8+ 14+ 20+ 21+ 24+ 40+ 41+ 42+ 50) 
aqdata['Imag_Acc_AQ_B'] = (aqdata['AccAQ_B_3_scored']+aqdata['AccAQ_B_8_scored']+
                           aqdata['AccAQ_B_14_scored']+aqdata['AccAQ_B_20_scored']+
                           aqdata['AccAQ_B_21_scored']+aqdata['AccAQ_B_24_scored']+
                           aqdata['AccAQ_B_40_scored']+aqdata['AccAQ_B_41_scored']+
                           aqdata['AccAQ_B_42_scored']+aqdata['AccAQ_B_50_scored'])

# Total
aqdata['Total_Acc_AQ_B'] =  (aqdata['AccAQ_B_1_scored'] + aqdata['AccAQ_B_2_scored'] + 
                             aqdata['AccAQ_B_3_scored'] + aqdata['AccAQ_B_4_scored'] + 
                             aqdata['AccAQ_B_5_scored'] + aqdata['AccAQ_B_6_scored'] + 
                             aqdata['AccAQ_B_7_scored'] + aqdata['AccAQ_B_8_scored'] + 
                             aqdata['AccAQ_B_9_scored'] + aqdata['AccAQ_B_10_scored'] + 
                             aqdata['AccAQ_B_11_scored'] + aqdata['AccAQ_B_12_scored'] + 
                             aqdata['AccAQ_B_13_scored'] + aqdata['AccAQ_B_14_scored'] + 
                             aqdata['AccAQ_B_15_scored'] + aqdata['AccAQ_B_16_scored'] + 
                             aqdata['AccAQ_B_17_scored'] + aqdata['AccAQ_B_18_scored'] + 
                             aqdata['AccAQ_B_19_scored'] + aqdata['AccAQ_B_20_scored'] + 
                             aqdata['AccAQ_B_21_scored'] + aqdata['AccAQ_B_22_scored'] + 
                             aqdata['AccAQ_B_23_scored'] + aqdata['AccAQ_B_24_scored'] + 
                             aqdata['AccAQ_B_25_scored'] + aqdata['AccAQ_B_26_scored'] + 
                             aqdata['AccAQ_B_27_scored'] + aqdata['AccAQ_B_28_scored'] + 
                             aqdata['AccAQ_B_29_scored'] + aqdata['AccAQ_B_30_scored'] + 
                             aqdata['AccAQ_B_31_scored'] + aqdata['AccAQ_B_32_scored'] + 
                             aqdata['AccAQ_B_33_scored'] + aqdata['AccAQ_B_34_scored'] + 
                             aqdata['AccAQ_B_35_scored'] + aqdata['AccAQ_B_36_scored'] + 
                             aqdata['AccAQ_B_37_scored'] + aqdata['AccAQ_B_38_scored'] + 
                             aqdata['AccAQ_B_39_scored'] + aqdata['AccAQ_B_40_scored'] + 
                             aqdata['AccAQ_B_41_scored'] + aqdata['AccAQ_B_42_scored'] + 
                             aqdata['AccAQ_B_43_scored'] + aqdata['AccAQ_B_44_scored'] + 
                             aqdata['AccAQ_B_45_scored'] + aqdata['AccAQ_B_46_scored'] + 
                             aqdata['AccAQ_B_47_scored'] + aqdata['AccAQ_B_48_scored'] + 
                             aqdata['AccAQ_B_49_scored'] + aqdata['AccAQ_B_50_scored'])

aqdata['ShortForm10_AQ_B'] = (aqdata['AccAQ_B_5_scored']+aqdata['AccAQ_B_28_scored']+
                           aqdata['AccAQ_B_10_scored']+aqdata['AccAQ_B_37_scored']+
                           aqdata['AccAQ_B_26_scored']+aqdata['AccAQ_B_38_scored']+
                           aqdata['AccAQ_B_20_scored']+aqdata['AccAQ_B_40_scored']+
                           aqdata['AccAQ_B_36_scored']+aqdata['AccAQ_B_22_scored'])

output = aqdata.to_csv(str(wd + '\\ERAQsCoded_withAQ10.csv'))
