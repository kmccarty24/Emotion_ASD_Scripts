# Dales Scoring Script
# November 2016
# To
# July 2017


# Use Whoosh perhaps?

# Import Necessary Modules
import pandas as pd
import spell
import os


class SpellingError(Exception):
    pass


# Read CSV / Ditch unecessary columns
wd = os.getcwd()
raw_csv = pd.read_csv(wd + '\\KarenDataToAdd.csv')

print(raw_csv.head())


raw_csv = raw_csv.fillna(value='minus999')


ColstoKeep = ['happy',
              'sad',
              'scared',
              'worried',
              'bored',
              'angry',
              'neutral',
              'disgusted',
              'surprised',
              'other']

extractedDF = pd.DataFrame()

for col in raw_csv:
    if str(raw_csv[col][0]) in ColstoKeep:  # The First Row
        extractedDF[col] = raw_csv[col]
        del raw_csv[col]

print(extractedDF.head())

clonedRaw = raw_csv

# Load Word Lists and create relevant lists
wordDF = pd.read_csv(str(wd + '\\EmotionWords.csv'))

happy = wordDF['happy'].dropna().tolist()
sad = wordDF['sad'].dropna().tolist()
scared = wordDF['scared'].dropna().tolist()
worried = wordDF['worried'].dropna().tolist()
bored = wordDF['bored'].dropna().tolist()
angry = wordDF['angry'].dropna().tolist()
neutral = wordDF['neutral'].dropna().tolist()
disgusted = wordDF['disgusted'].dropna().tolist()
surprised = wordDF['surprised'].dropna().tolist()
other = wordDF['other'].dropna().tolist()


# Functions

def correctSpelling(element):  # SORT regex for multiple punctuation

    word = str(element).lower()

    if ',' in word:
        replacedPunc = word.replace(',', ' ')
    elif '/' in word:
        replacedPunc = word.replace('/', ' ')
    elif '\\' in word:
        replacedPunc = word.replace('\\', ' ')
    elif '.' in word:
        replacedPunc = word.replace('.', ' ')
    elif '-' in word:
        replacedPunc = word.replace('-', ' ')
    elif '_' in word:
        replacedPunc = word.replace('_', ' ')
    else:
        replacedPunc = word

    splits = replacedPunc.split()

    if len(splits) == 1:
        corrWord = spell.correction(word)
    elif len(splits) > 0:
        corrWord = [spell.correction(wrd) for wrd in splits]
        corrWord = ' '.join(corrWord)
    else:
        raise SpellingError('Something went terribly wrong here, please investigate')
    return corrWord


def userInput(unknown, correctAns, correct_list):  # TO DO Add to CSV if 'correct'

    acceptedTerms = ['YES', 'NO', 'yes', 'no', 'Yes', 'No']

    yesState = ['y', 'yes']
    noState = ['n', 'no']

    validResp = False
    while validResp is False:

        print("##########################################################")
        print("Correct Answer: {}".format(correctAns))
        print("Unknown Word Found: {} ".format(unknown))
        print("Mark as Correct?")
        print("Type Yes if Correct")
        print("Type No if Incorrect")
        print("##########################################################")

        userinput = input("Your Response: ").lower()

        if str(userinput) not in acceptedTerms:
            print("Invalid Response, Please Try Again...")
            continue
        elif str(userinput) in acceptedTerms:
            validResp = True

    if userinput in yesState:
        response = 1
        if len(unknown.split()) == 1:
            correct_list.append(unknown)

    elif userinput in noState:
        response = 0
    else:
        raise Exception('no response') 

    return response, correct_list


# Apply the spelling and punctuation correction

extractedDF_NoSpell = extractedDF

print('Starting Spelling')
extractedDF = extractedDF.applymap(correctSpelling)
print('Passed Spelling')

keywords = {'happy': happy, 'sad': sad, 'scared': scared,
            'worried': worried, 'bored': bored, 'angry': angry,
            'disgusted': disgusted, 'surprised': surprised,
            'neutral': neutral}

# Begin Marking (finally)

scoredDF = pd.DataFrame()

counter = 1
for c in extractedDF:
    score = []
    col_name = str(c) + '_Scored'
    print("##########################################################")
    print("Column Name %s" % (c))
    print("iteration %i" % (counter))
    print("##########################################################")
    correct_word = str((extractedDF[c][0]))
    correct_list = keywords[correct_word]

    # pop the correct list out and flatten the remaining incorrect words
    keywords.pop(correct_word)

    # Flatten the list of dictionary values (double for loop: for item within each sub_list in keywords.values)
    incorrFlat = [item for sublist in list(keywords.values()) for item in sublist]

    score.append(correct_word)
    for words in extractedDF[c][1:]:  # Skip first row
        print('Cell: ', words)

        if len(words.split()) == 1:
            if words in correct_list:
                score.append(1)
                print('1 word, correct')

            elif str(words) is 'nan':
                print('found NaN')
                score.append(0)

            elif words in incorrFlat or words in other:
                score.append(0)
                print('1 word, wrong')

            else:
                print('going to user')
                userScore, correct_list = userInput(words, correct_word, correct_list)
                score.append(userScore)

        elif len(words.split()) > 1:
            print('more than one word: ', words)
            wordList = words.split()
            tally = []

            for word in wordList:
                if word in incorrFlat:
                    score.append(0)
                    tally = []
                    print('Found illegal word, automatic incorrect')
                    break
                elif word in correct_list:
                    tally.append(1)
                    print('adding correct word to tally')
                elif word in other:
                    tally.append(2)
                    print('adding alternative word to tally')
                elif word not in correct_list and word not in incorrFlat:

                    userScore, correct_list = userInput(words, correct_word, correct_list)
                    score.append(userScore)
                    tally = []
                    break

            if len(tally) == 0:
                pass
            elif 1 in tally:
                score.append(1)
            else:
                score.append(0)

    scoredDF[col_name] = score
    keywords[correct_word] = correct_list  # add the correct list back in
    counter += 1

# Save the new Keywords File
keywords['other'] = other
updatedEmoWords = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in keywords.items()]))
updatedEmoWordsOUT = updatedEmoWords.to_csv(str(wd + '\\EmotionWords.csv'), index= False)
print('Iteration Finished')

# Concatenate DFs

# Stack DFs
stackedDF = pd.concat([extractedDF, scoredDF], axis=1)

# Extract Column Names
origColNames = extractedDF.columns.tolist()
scoredColNames = scoredDF.columns.tolist()

# Zip names together
orderedCols = []
for orig, scored in zip(origColNames, scoredColNames):
    orderedCols.append(orig)
    orderedCols.append(scored)

stackedDF = stackedDF[orderedCols]

# Add in scoring
stackedDF['AngryTotal'] = scoredDF[[col for col in scoredDF.columns if 'ang' in col]].sum(axis=1)
stackedDF['BoredTotal'] = scoredDF[[col for col in scoredDF.columns if 'bor' in col]].sum(axis=1)
stackedDF['DisgustTotal'] = scoredDF[[col for col in scoredDF.columns if 'dis' in col]].sum(axis=1)
stackedDF['ScaredTotal'] = scoredDF[[col for col in scoredDF.columns if 'sca' in col]].sum(axis=1)
stackedDF['HappyTotal'] = scoredDF[[col for col in scoredDF.columns if 'hap' in col]].sum(axis=1)
stackedDF['SadTotal'] = scoredDF[[col for col in scoredDF.columns if 'sad' in col]].sum(axis=1)
stackedDF['SurpriseTotal'] = scoredDF[[col for col in scoredDF.columns if 'sur' in col]].sum(axis=1)
stackedDF['WorriedTotal'] = scoredDF[[col for col in scoredDF.columns if 'wor' in col]].sum(axis=1)
stackedDF['NeutralTotal'] = scoredDF[[col for col in scoredDF.columns if 'neu' in col]].sum(axis=1)
stackedDF['LowContextTotal'] = scoredDF[[col for col in scoredDF.columns if 'lc' in col]].sum(axis=1)
stackedDF['MedContextTotal'] = scoredDF[[col for col in scoredDF.columns if 'mc' in col]].sum(axis=1)
stackedDF['HighContextTotal'] = scoredDF[[col for col in scoredDF.columns if 'hc' in col]].sum(axis=1)
stackedDF['OverallTotal'] = scoredDF[[col for col in scoredDF.columns if '_Scored' in col]].sum(axis=1)


outputDF = pd.concat([clonedRaw, stackedDF], axis=1)

output = outputDF.to_csv(str(wd + "\\KarenDataToAdd_Scored.csv"))


# Make it able to add incorrect words to the column as it iterates through responses