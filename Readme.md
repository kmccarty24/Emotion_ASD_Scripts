#Readme for Scoring Scripts for GitHub

Replace XXX with number



##Accessible AQ
A script for marking the new accessible versions of the AQ
It takes both versions
This will give scores for overall, subscales and the Short Form AQ 10 item version
Marks dichotomously
Marks neutral as 0.5
Must be CSV

###Version A
Four possible responses (on Likert scale)
Items 1 - 50
Column names must be AccAQ_A_XXX

###Version B
Two images version
Items 1-50
Column names must be AccAQ_B_XXX

Will mark numbers or words if in lower case (e.g. definitely agree)

___

##Original AQ
A script to mark the original AQ 50 item version
This will give scores for overall, subscales and the Short Form AQ 10 item version
Marks dichotomously
Marks neutral as 0.5
Must be CSV

Item columns must be labelled: AQ_XXX
Will mark numbers or words

Currently trying to adapt so it takes words with capitals at start (Definitely Agree) however this doesn't seem to be working

___

##QCAE
Marks the original and our adapted for parents version
Takes numbers and lower case wording (strongly agree)
Marks on scale
Marks neutral as 2.5
Provides subscales, overall cognitive empathy, overall affective empathy and Total
Must be CSV

Item columns must be labelled: QCAE_XXX

___

#Scripts to recode datasets

These are small scripts to be used when compiling multiple datasets
For instance when one study uses a 3 to indicate someone has dyslexia while another uses 5 to indicate the same thing
Must be CSV

These aren't a big deal but might be handy

___

##Emotion Scoring Script

Scores emotion stimuli
I feel this description will need adding to...

Takes CSV files
It strips out all columns that have happy, sad etc. in the second row [see cols to keep for full list]
It uses these words to identify which emotion it should be
It replaces punctuation with a space
It spelling corrects

It then scores items as correct or not depending on their presence in a list [this is a separate csv]
If it is in any other list it is deemed incorrect
If it is on no list, you score by hand saying YES or NO

If you say yes, it goes onto the correct list
If you say no, it does not go on the list, so you can add by hand if need be

It will then calculate scores
Certain things need to be present in column 1
For instance, angry must have 'ang' in the title
For medium context it must have 'mc' in the title
See stackedDF for further info

Therefore be careful when naming columns
It was first designed for the static data, but can easily be used for the dynamic if column names are changed

___
