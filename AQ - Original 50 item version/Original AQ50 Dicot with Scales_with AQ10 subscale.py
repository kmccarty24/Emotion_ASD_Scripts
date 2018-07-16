# Only works on Win32 distributions of python on Windows.
# On OSX and Linux Kernels, must instsall via homebrew

# Import Necessary Modules

import numpy as np
import pandas as pd

import os

# Read CSV / Ammend missing values
wd = os.getcwd()
raw_csv = pd.read_csv(wd + '\\OriginalAQ Dataframe.csv')
aqdata = raw_csv.fillna(np.nan)
aqdata = raw_csv

#   List of columns which 'definitely agree','slightly agree' = 1
agree = ['AQ_1','AQ_2','AQ_4','AQ_5','AQ_6','AQ_7','AQ_9',
		 'AQ_12','AQ_13','AQ_16','AQ_18','AQ_19','AQ_20',
		 'AQ_21','AQ_22','AQ_23','AQ_26','AQ_33','AQ_35',
		 'AQ_39','AQ_41','AQ_42','AQ_43','AQ_45','AQ_46']

#   List of collumns which 'definitely disagree','slightly disagree' = 1
disagree = ['AQ_3','AQ_8','AQ_10','AQ_11','AQ_14','AQ_15',
			'AQ_17','AQ_24','AQ_25','AQ_27','AQ_28','AQ_29',
			'AQ_30','AQ_31','AQ_32','AQ_34','AQ_36','AQ_37',
			'AQ_38','AQ_40','AQ_44','AQ_47','AQ_48','AQ_49',
			'AQ_50']

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

# Sub-Scales
# Social-Skills (items 1+ 11+ 13+ 15+ 22+ 36+ 44+ 45+ 47+ 48)
SocialSk = ['AQ_1_scored', 'AQ_11_scored',
            'AQ_13_scored', 'AQ_15_scored',
            'AQ_22_scored', 'AQ_36_scored',
            'AQ_44_scored', 'AQ_45_scored',
            'AQ_47_scored', 'AQ_48_scored']

aqdata['SocialSK'] = aqdata[SocialSk].astype(float).sum(axis=1)

aqdata['SocialSK']

# Attention Switching (items 2+ 4+ 10+ 16+ 25+ 32+ 34+ 37+ 43+ 46)
AttenSW = ['AQ_2_scored', 'AQ_4_scored',
           'AQ_10_scored', 'AQ_16_scored',
           'AQ_25_scored', 'AQ_32_scored',
           'AQ_34_scored', 'AQ_37_scored',
           'AQ_43_scored', 'AQ_46_scored']

aqdata['AttenSW'] = aqdata[AttenSW].astype(float).sum(axis=1)

# Attention to Detail (items 5+ 6+ 9+ 12+ 19+ 23+ 28+ 29+ 30+ 49)
ATD = ['AQ_5_scored', 'AQ_6_scored',
       'AQ_9_scored', 'AQ_12_scored',
       'AQ_19_scored', 'AQ_23_scored',
       'AQ_28_scored', 'AQ_29_scored',
       'AQ_30_scored', 'AQ_49_scored']

aqdata['ATD'] = aqdata[ATD].astype(float).sum(axis=1)

# Communication (items 7+ 17+ 18+ 26+ 27+ 31+ 33+ 35+ 38+ 39)
Commun = ['AQ_7_scored', 'AQ_17_scored',
          'AQ_18_scored', 'AQ_26_scored',
          'AQ_27_scored', 'AQ_31_scored',
          'AQ_33_scored', 'AQ_35_scored',
          'AQ_38_scored', 'AQ_39_scored']

aqdata['Commun'] = aqdata[Commun].astype(float).sum(axis=1)

# Imagination (items 3+ 8+ 14+ 20+ 21+ 24+ 40+ 41+ 42+ 50)
Imag = ['AQ_3_scored', 'AQ_8_scored',
        'AQ_14_scored', 'AQ_20_scored',
        'AQ_21_scored', 'AQ_24_scored',
        'AQ_40_scored', 'AQ_41_scored',
        'AQ_42_scored', 'AQ_50_scored']

aqdata['Imag'] = aqdata[Imag].astype(float).sum(axis=1)

ShortForm_AQ10 = ['AQ_5_scored', 'AQ_28_scored',
                  'AQ_10_scored', 'AQ_37_scored',
                  'AQ_26_scored', 'AQ_38_scored',
                  'AQ_20_scored', 'AQ_40_scored',
                  'AQ_36_scored', 'AQ_22_scored']

aqdata['ShortForm_AQ10'] = aqdata[ShortForm_AQ10].astype(float).sum(axis=1)

# Total
Total = ['AQ_1_scored', 'AQ_2_scored',
         'AQ_3_scored', 'AQ_4_scored',
         'AQ_5_scored', 'AQ_6_scored',
         'AQ_7_scored', 'AQ_8_scored',
         'AQ_9_scored', 'AQ_10_scored',
         'AQ_11_scored', 'AQ_12_scored',
         'AQ_13_scored', 'AQ_14_scored',
         'AQ_15_scored', 'AQ_16_scored',
         'AQ_17_scored', 'AQ_18_scored',
         'AQ_19_scored', 'AQ_20_scored',
         'AQ_21_scored', 'AQ_22_scored',
         'AQ_23_scored', 'AQ_24_scored',
         'AQ_25_scored', 'AQ_26_scored',
         'AQ_27_scored', 'AQ_28_scored',
         'AQ_29_scored', 'AQ_30_scored',
         'AQ_31_scored', 'AQ_32_scored',
         'AQ_33_scored', 'AQ_34_scored',
         'AQ_35_scored', 'AQ_36_scored',
         'AQ_37_scored', 'AQ_38_scored',
         'AQ_39_scored', 'AQ_40_scored',
         'AQ_41_scored', 'AQ_42_scored',
         'AQ_43_scored', 'AQ_44_scored',
         'AQ_45_scored', 'AQ_46_scored',
         'AQ_47_scored', 'AQ_48_scored',
         'AQ_49_scored', 'AQ_50_scored']

aqdata['Total'] = aqdata[Total].astype(float).sum(axis=1)

output = aqdata.to_csv(str(wd + '\\OriginalAQ_Dataframe_scored.csv'))
# na_rep = '-999'
