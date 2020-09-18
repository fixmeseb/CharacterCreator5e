import os
from wizardSpells import spells as wizardSpellList
from wizardSpells import slots as wizardSlots

from DnDLists import damageTypes
from DnDLists import languagesDungeonsAndDragons 
from DnDLists import skillsDungeonsAndDragons as skillsMaster
from DnDLists import artisanTools
from DnDLists import gamingSets
from DnDLists import musicalInstruments
from DnDLists import tools as toolsMaster
from DnDLists import weapons as weaponsMaster
from DnDLists import speeds as speedMaster
from DnDLists import sights as sightsMaster
from DnDLists import fightingStyles as fightingStylesMaster
from DnDLists import abilityScores as abilityScoresMaster

spellLists = {"Wizard":wizardSpellList}
sources = ["Dungeons & Dragons Official", "Unearthed Arcana", "SW5e", "Homebrew"]

testingThing = ["Elf", "Drow", "Fighter-02", "Acolyte", "Dexterity", "Charisma", "Constitution", "Strength", "Wisdom", "Intelligence"]
test = 0
testBool = 0

path = "C:\\Users\\Sebastian_Polge\\OneDrive-CaryAcademy\\Documents\\meNewBot\\extensions\\CharacterCreator5e\\Races"
races = {}
racialParents = []
for f in os.listdir(path): 
    if os.path.isdir(os.path.join(path, f)): 
        racialParents.append(f)
for raceParent in racialParents:
    subraces = []
    for f in os.listdir(os.path.join(path, raceParent)):
        if os.path.isfile(os.path.join(os.path.join(path, raceParent), f)):
            split = f.split(".")
            if not("PARENT" in split[0]):
                subraces.append(split[0])
    races[raceParent] = subraces
#Creates a "races" dict that contains the names and subraces of the races. 
#Format is that the race parent name is the key and a list of subraces is the value. 

path = "C:\\Users\\Sebastian_Polge\\OneDrive-CaryAcademy\\Documents\\meNewBot\\extensions\\CharacterCreator5e\\Classes"
classi = {}
parentClasses = []
for f in os.listdir(path): 
    if os.path.isdir(os.path.join(path, f)): 
        parentClasses.append(f)
for classer in parentClasses:
    subclasses = []
    for f in os.listdir(os.path.join(path, classer)):
        if os.path.isfile(os.path.join(os.path.join(path, classer), f)):
            split = f.split(".")
            if not("MASTER" in split[0]):
                subclasses.append(split[0])
    classi[classer] = subclasses
#Creates a "classes" dict that contains the names and subclasses of the subclasses. 
#Format is that the class name is the key and a list of subclasses is the value. 
pathFile = open("token.txt", "r")
pathin = pathFile.readline()
path = pathin
backgrounds = []
for file in os.listdir(path): 
    if os.path.isfile(os.path.join(path, file)):
        backgroundSplit = file.split(".")
        backgrounds.append(backgroundSplit[0])   

print("Welcome to The Invisible Man's Character Generator for D&D Fifth Edition!")
print('If you have any questions, input a single "?" to get more info about the available options.')
print("Let's set a character up here and we can get started!")
name = input("Enter a name for your character, please: ")
if name == "?":
    print("Your name is the name of your character.")
if name == "test":
    print("Testing Mode Enabled. ")
    testBool = 1

race = testingThing[0]
subrace = testingThing[1]
haveSubrace = False
if len(races[race]) >= 1: 
    haveSubrace = True
if testBool != 1:
    race = input("Enter your character's race: ")
    if race == "?":
        print("This is the parent race of your character. Valid races are inputted into the 'Races' folder. ")
        for i in races:
            if len(races[i]) >= 1:
                print("-" + i + ": ")
                for subrace in races[i]:
                    print("\t" + subrace)
            else:
                print("-" + i + " (no subraces)")
        race = input("Now, please choose one: ")
    if not(race in races):
        race = input("Enter a valid race, please: ")
        while not(race in races):
            race = input("Seriously, please enter a valid race: ")
    haveSubrace = False
    if len(races[race]) >= 1: 
        haveSubrace = True
        subrace = input("Enter your subrace: ")
        if subrace == "?":
            if len(races[race]) >= 1:
                    for subrace in races[race]:
                        print("\t" + subrace)
            else:
                print("no subraces")
            subrace = input("Please input subrace: ")
        if not(subrace in races[race]):
            race = input("Enter a valid subrace, please: ")
            while not(subrace in races[race]):
                race = input("Seriously, please enter a valid subrace: ")
else:
    print("Enter your character's race: Elf")
    print("Enter your subrace: Drow")
totalLevel = 0
clas = testingThing[2]
if testBool != 1:
    clas = input("Please enter your class in a format like so: Fighter-13/Cleric-07 (make sure to keep the numbers as 2 digits, not one.). ")
    if clas == "?":
        for i in classi:
            print("-" + i)
        clas = input("Now, please choose: ")
else:
    print("Please enter your class in a format like so: Fighter-13/Cleric-07 (make sure to keep the numbers as 2 digits, not one.). Fighter-02")

classesArray = clas.split("/")
classes = []
for Class in classesArray:
    classer = Class.split("-")
    if not(classer[0] in classi):
        classer[0] = input(classer[0] + " is not a valid class. Please correct any errors and re-input: ")
        if not(classer[0] in classi):
            while not(classer[0] in classi):
                classer[0] = input(classer[0] + " is not a valid class. Please correct any errors and re-input: ")
    classes.append(classer)
    totalLevel+=int(classer[1])
for i in classes:
    if (int(i[1]) >= 3) or (int(i[1]) >= 2 and i[0] == "Wizard"):
        subclass = input("Please add your subclass for " + i[0] + ": ")
        if subclass == "?":
            if len(classi[i[0]]) >= 1:
                print("-" + i[0] + ": ")
                for subclass in classi[i[0]]:
                    print("\t" + subclass)
            subclass = input("Now, please add your subclass for " + i[0] + ": ")
        if not(subclass in classi[i[0]]):
            subclass = input(subclass + " is not a valid subclass. Please correct any errors and re-input: ")
            if not(subclass in classi[i[0]]):
                while not(subclass in classi[i[0]]):
                    subclass = input(classer + " is not a valid subclass. Please correct any errors and re-input: ")
        i.append(subclass)
    else:
        i.append("None")

background = testingThing[3]
if testBool != 1:
    background = input("Input your background: ")
    if background == "?":
        for back in backgrounds:
            print("-" + back)
        background = input("Now, please input your background: ")
    if not(background in backgrounds):
            background = input(background + " is not a valid background. Please correct any errors and re-input:")  
            if not(background in backgrounds):
                while not(background in backgrounds):
                    background = input(background + " is not a valid background. Please correct any errors and re-input:")  
else:
    print("Input your background: Acolyte")
print("Now, character scores!")
scoresRemain = ["Dexterity", "Strength", "Constitution", "Intelligence", "Wisdom", "Charisma"]
scoresOrder = [testingThing[4], testingThing[5], testingThing[6], testingThing[7], testingThing[8], testingThing[9]]
if testBool != 1:
    scoresOrder[0] = input("First Score: ")
    scoresOrder[1] = input("Second Score: ")
    scoresOrder[2] = input("Third Score: ")
    scoresOrder[3] = input("Fourth Score: ")
    scoresOrder[4] = input("Fifth Score: ")
    scoresOrder[5] = input("Sixth Score: ")
else:
    print("First Score: Dexterity")
    print("Second Score: Charisma")
    print("Third Score: Constitution")
    print("Fourth Score: Strength")
    print("Fifth Score: Wisdom")
    print("Sixth Score: Intelligence")

scores = {}
scoresNumber = [15, 14, 13, 12, 10, 8]
for i in range(len(scoresOrder)):
    scores[scoresOrder[i]] = scoresNumber[i]
path = "C:\\Users\\Sebastian_Polge\\OneDrive-CaryAcademy\\Documents\\meNewBot\\extensions\\CharacterCreator5e"

featuresToNote = []
choices = []
spells = []
fightingStyles = []
skills = skillsMaster
tools = []
languages = []
damageResistances = []
savingThrowConditionAdvantages = []
sights = []
savingThrowProfs = []
spellListExtra = []
weapons = weaponsMaster

speeds = {}

hitDiceType = ""

hitDiceQuant = 0
abilityImprovFeatQuant = 0

lookUpTable = {
    "<":"Score Increase",
    "_":speeds,
    "#":sights,
    "@":savingThrowConditionAdvantages,
    "^":damageResistances,
    "=":tools,
    "!":weapons,
    ";":languages,
    "'":spells,
    "[":skills,
    "%":fightingStyles,
    "+":hitDiceType,
    "~":savingThrowProfs,
    "|":abilityImprovFeatQuant,
    "$":spellListExtra
}


file = open(path + "\\Races\\" + race + "\\" + race + "PARENT.txt", "r", errors='ignore')
raceText = file.read()
raceFeatures = raceText.split("\n")
file.close()

if (haveSubrace == True):
    file = open(path + "\\Races\\" + race + "\\" + subrace + ".txt", "r")
    subraceText = file.read()
    subraceFeatures = subraceText.split("\n")
    file.close()

classFeatures = []
subclassFeatures = []

for i in classes:
    file = open(path + "\\Classes\\" + i + "\\" + i + "PARENT.txt", "r", )
    classText = file.read()
    classFeatures.append(classText.split("\n"))
    file.close()
    if len(i) > 2: 
        file = open(path + "\\Classes\\" + i + "\\" + subclass + ".txt", "r")
        subclassText = file.read()
        subclassFeatures.append(subclassText.split("\n"))
        file.close()

for lineI in range(len(raceFeatures)-1):
    lineNum = lineI + 1
    line = raceFeatures[lineNum]
    if ":C:" in line:
        choices.append(line.split("-")[2])
    else:
        if ":F:" in line:
            featuresToNote.append(line.split("-")[2])
        else:
            levelRequire = line[1:2:]
            if totalLevel >= int(levelRequire):
                levelTags = line.split("-")
                for i in range(2, len(levelTags)):
                    keyTag = levelTags[i]
                    tagIdentify = keyTag[0:1:]
                    tagInfo = keyTag[1:len(keyTag)-1:]
                    print("tagInfo: " + keyTag)
                    if tagIdentify == "_":
                        if len(tagInfo.split(",")) > 1:
                            lookUpTable[tagIdentify][tagInfo.split(",")[1]] = tagInfo.split(",")[0]
                        else:
                            lookUpTable[tagIdentify]["Walking"] = tagInfo
                    else:
                        if tagIdentify == "+":
                            tagInfo = tagInfo[1:len(tagInfo)-1:]
                            lookUpTable[tagIdentify] = tagInfo
                        else:
                            if tagIdentify == "|":
                                lookUpTable[tagIdentify] +=1
                            else:
                                if tagIdentify == "<":
                                    abilityScoreSplit = tagInfo.split(",")
                                    scores[abilityScoreSplit[0]]+=int(abilityScoreSplit[1])
                                else:
                                    lookUpTable[tagIdentify].append(tagInfo)

for lineI in range(len(subraceFeatures)-1):
    lineNum = lineI + 1
    line = subraceFeatures[lineNum]
    if ":C:" in line:
        for i in range(2, len(line.split("-"))):
            choices.append(i)
    else:
        if ":F:" in line:
            for i in range(2, len(line.split("-"))):
                choices.append(i)
        else:
            levelRequire = line[1:2:]
            if totalLevel >= int(levelRequire):
                levelTags = line.split("-")
                for i in range(2, len(levelTags)):
                    keyTag = levelTags[i]
                    tagIdentify = keyTag[0:1:]
                    tagInfo = keyTag[1:len(keyTag)-1:]
                    print("tagInfo: " + keyTag)
                    if tagIdentify == "_":
                        if len(tagInfo.split(",")) > 1:
                            lookUpTable[tagIdentify][tagInfo.split(",")[1]] = tagInfo.split(",")[0]
                        else:
                            lookUpTable[tagIdentify]["Walking"] = tagInfo
                    else:
                        if tagIdentify == "+":
                            tagInfo = tagInfo[1:len(tagInfo)-1:]
                            lookUpTable[tagIdentify] = tagInfo
                        else:
                            if tagIdentify == "|":
                                lookUpTable[tagIdentify] +=1
                            else:
                                if tagIdentify == "<":
                                    abilityScoreSplit = tagInfo.split(",")
                                    scores[abilityScoreSplit[0]]+=int(abilityScoreSplit[1])
                                else:
                                    lookUpTable[tagIdentify].append(tagInfo)

for lineI in range(len(classFeatures)-1):
    lineNum = lineI + 1
    line = classFeatures[lineNum]
    if ":C:" in line:
        for i in range(2, len(line.split("-"))):
            choices.append(i)
    else:
        if ":F:" in line:
            for i in range(2, len(line.split("-"))):
                choices.append(i)
        else:
            levelRequire = line[1:2:]
            if totalLevel >= int(levelRequire):
                levelTags = line.split("-")
                for i in range(2, len(levelTags)):
                    keyTag = levelTags[i]
                    tagIdentify = keyTag[0:1:]
                    tagInfo = keyTag[1:len(keyTag)-1:]
                    print("tagInfo: " + keyTag)
                    if tagIdentify == "_":
                        if len(tagInfo.split(",")) > 1:
                            lookUpTable[tagIdentify][tagInfo.split(",")[1]] = tagInfo.split(",")[0]
                        else:
                            lookUpTable[tagIdentify]["Walking"] = tagInfo
                    else:
                        if tagIdentify == "+":
                            tagInfo = tagInfo[1:len(tagInfo)-1:]
                            lookUpTable[tagIdentify] = tagInfo
                        else:
                            if tagIdentify == "|":
                                lookUpTable[tagIdentify] +=1
                            else:
                                if tagIdentify == "<":
                                    abilityScoreSplit = tagInfo.split(",")
                                    scores[abilityScoreSplit[0]]+=int(abilityScoreSplit[1])
                                else:
                                    lookUpTable[tagIdentify].append(tagInfo)

for lineI in range(len(subclassFeatures)-1):
    lineNum = lineI + 1
    line = subclassFeatures[lineNum]
    if ":C:" in line:
        for i in range(2, len(line.split("-"))):
            choices.append(i)
    else:
        if ":F:" in line:
            for i in range(2, len(line.split("-"))):
                choices.append(i)
        else:
            levelRequire = line[1:2:]
            if totalLevel >= int(levelRequire):
                levelTags = line.split("-")
                for i in range(2, len(levelTags)):
                    keyTag = levelTags[i]
                    tagIdentify = keyTag[0:1:]
                    tagInfo = keyTag[1:len(keyTag)-1:]
                    print("tagInfo: " + keyTag)
                    if tagIdentify == "_":
                        if len(tagInfo.split(",")) > 1:
                            lookUpTable[tagIdentify][tagInfo.split(",")[1]] = tagInfo.split(",")[0]
                        else:
                            lookUpTable[tagIdentify]["Walking"] = tagInfo
                    else:
                        if tagIdentify == "+":
                            tagInfo = tagInfo[1:len(tagInfo)-1:]
                            lookUpTable[tagIdentify] = tagInfo
                        else:
                            if tagIdentify == "|":
                                lookUpTable[tagIdentify] +=1
                            else:
                                if tagIdentify == "<":
                                    abilityScoreSplit = tagInfo.split(",")
                                    scores[abilityScoreSplit[0]]+=int(abilityScoreSplit[1])
                                else:
                                    lookUpTable[tagIdentify].append(tagInfo)

for choice in choices:
    tagIdentify = choice[0:1:]
    tagInfo = keyTag[1:len(keyTag)-1:]
    print("tagInfo: " + keyTag)
    if tagIdentify == "<":
        abilityScoreSplit = tagInfo.split(",")
        stats = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
        if len(abilityScoreSplit) == 3 and (abilityScoreSplit[0] == "Any" or abilityScoreSplit[0] == "ANY"):
            for i in range(int(abilityScoreSplit[2])):
                increaseStat = input("Which stat would you like to increase? ")
                if increaseStat == "?":
                    print("The valid stats currently are: ")
                    for stat in stats:
                        print(stat)
                else:
                    validity = False
                    while validity != True:
                        if not(increaseStat in stats):
                            print(increaseStat + " is not a valid stat.")
                        else:
                            scores[increaseStat]+=int(abilityScoreSplit[1])
                            validity = True
        else: 
            if len(abilityScoreSplit[0].split("/")) > 1:
                for i in stats:
                    if not (i in abilityScoreSplit[0]):
                        stats.remove(i)
                print("Choose " + abilityScoreSplit[2] + " stats to increase from the following list. ")
                for i in stats:
                    print(i)
                for i in range(int(abilityScoreSplit[2])):
                    increaseStat = input("Which stat would you like to increase? ")
                    if increaseStat == "?":
                        print("The valid stats currently are: ")
                        for stat in stats:
                            print(stat)
                    else:
                        validity = False
                        while validity != True:
                            if not(increaseStat in stats):
                                print(increaseStat + " is not a valid stat.")
                            else:
                                scores[increaseStat]+=int(abilityScoreSplit[1])
                                validity = True
    else:
        if tagIdentify == ";":
            newLanguages = []
            validLang = False
            for lang in languagesDungeonsAndDragons:
                if not (lang in languages):
                    newLanguages.append(lang)
            newLang = input("Please choose a new language: ")
            if newLang == "?":
                print("Valid Languages: ")
                for lang in newLanguages:
                    print(lang)
            if newLang in languagesDungeonsAndDragons and not (newLang in languages):
                languages.append(newLang)
                newLanguages.remove(newLang)
            else:
                while validLang == False:
                    newLang = input("Please input a valid language: ")
                    if newLang in languagesDungeonsAndDragons and not (newLang in languages):
                        languages.append(newLang)
                        newLanguages.remove(newLang)
                        validLang = True
        else:
            if tagIdentify == "@": 
                if len(tagInfo.split("/")) > 2 or (len(tagInfo.split("/") > 1 and not (tagInfo.split("/")[0] == "Any"))):
                    print("Choose one of the following to have advantage on saving throws against:")
                    savingThrowOptions = []
                    for choice in tagInfo.split(",")[0].split("/"): 
                        print("-" + str(choice))
                        savingThrowOptions.append(choice)
                    choice = input("Choice? ")
                    onOff = True
                    while onOff == True: 
                        if choice in savingThrowOptions:
                            savingThrowConditionAdvantages.append(choice)
                            onOff = False
                        else: 
                            print("That was incorrect. Please input a valid option.")
                else:
                    if len(tagInfo.split("/")) > 1:
                        quant = int(tagInfo.split("/")[1])
                    else:
                        quant = 1
                    print("Choose " + str(quant) + " of the following to have advantage on saving throws against:")
                    for choice in damageTypes: 
                        print("-" + str(choice))
                    for i in range(quant):
                        choice = input("Choice? ")
                        onOff = True
                        while onOff == True: 
                            if choice in damageTypes:
                                savingThrowConditionAdvantages.append(choice)
                                onOff = False
                            else: 
                                print("That was incorrect. Please input a valid option.")
            else: 
                if tagIdentify == "+":
                    #alright, look. There's almost no chance of this one happening. I'm deleting the functions that physically should not work within the rules of 5e. If someone complains, I can jury rig something? I guess? Seriously, that would be really weird. 
                    if len(tagInfo.split("/")) > 2 or (len(tagInfo.split("/") > 1 and not (tagInfo.split("/")[0] == "Any"))):
                        print("Choose one of the following hit dice? I guess? ")
                        hitDiceChoices = []
                        for choice in tagInfo.split(",")[0].split("/"): 
                            print("-" + str(choice))
                            hitDiceChoices.append(choice)
                        choice = input("Choice? ")
                        onOff = True
                        while onOff == True: 
                            if choice in hitDiceChoices:
                                hitDiceType = choice
                                onOff = False
                            else: 
                                print("That was incorrect. Please input a valid option.")
                    else:
                        if len(tagInfo.split("/")) > 1:
                            quant = int(tagInfo.split("/")[1])
                        else:
                            quant = 1
                        print("Choose " + str(quant) + " of the following to be your hit dice:")
                        for choice in hitDiceType: 
                            print("-" + str(choice))
                        for i in range(quant):
                            choice = input("Choice? ")
                            onOff = True
                            while onOff == True: 
                                if choice in damageTypes:
                                    hitDiceType = choice
                                    onOff = False
                                else: 
                                    print("That was incorrect. Please input a valid option.")
                else: 
                    if tagIdentify == "_":
                        #Same deal with this one. Shouldn't work, but it could with some wack homebrew so it's all set up just in case.
                        if len(tagInfo.split("/")) > 2 or (len(tagInfo.split("/") > 1 and not (tagInfo.split("/")[0] == "Any"))):
                            print("Choose one of the following speeds: ")
                            speedChoices = []
                            for choice in tagInfo.split("/")[0]: 
                                if len(choice.split(",")) > 1:
                                    print("-" + str(choice.split(",")[0]) + " (" + choice.split(",")[1] + " feet)")
                                else: 
                                    print("-Walking ( " + choice.split(",")[0] + ")")
                                speedChoices.append(choice)
                            choice = input("Choice (input only the name of the choice, not the quantity)? ")
                            onOff = True
                            speed = 0
                            for i in speedChoices:
                                iType = ""
                                if i.split(",") > 1:
                                    iType = i.split(",")[0]
                                else: 
                                    iType == "Walking"
                                if iType == choice and i.split(",") > 1:
                                    speed = i.split(",")[1]
                                else:
                                    speed = i.split(",")[0]
                            while onOff == True: 
                                if choice in speedChoices:
                                    onOff = False
                                else: 
                                    print("That was incorrect. Please input a valid option.")
                        else:
                            if len(tagInfo.split(",")) > 1:
                                quant = int(tagInfo.split(",")[1])
                            else:
                                quant = 1
                            print("Choose " + str(quant) + " of the following speeds:")
                            for choice in speedMaster: 
                                print("-" + str(choice))
                            for i in range(quant):
                                choice = input("Choice? ")
                                onOff = True
                                while onOff == True: 
                                    if choice in speedMaster:
                                        speeds.append(choice)
                                        onOff = False
                                    else: 
                                        print("That was incorrect. Please input a valid option.")
                    else:
                        if tagIdentify == "#":
                            #And we continue the tradition of probably useless stuff. 
                            if len(tagInfo.split("/")) > 2 or (len(tagInfo.split("/") > 1 and not (tagInfo.split("/")[0] == "Any"))):
                                print("Choose one of the following sights. ")
                                sightOptions = []
                                for choice in tagInfo.split(",")[0].split("/"): 
                                    print("-" + str(choice))
                                    sightOptions.append(choice)
                                choice = input("Choice? ")
                                onOff = True
                                while onOff == True: 
                                    if choice in sightOptions:
                                        sights.append(choice)
                                        onOff = False
                                    else: 
                                        print("That was incorrect. Please input a valid option.")
                            else:
                                if len(tagInfo.split("/")) > 1:
                                    quant = int(tagInfo.split("/")[1])
                                else:
                                    quant = 1
                                print("Choose " + str(quant) + " as your sights:")
                                for choice in sightsMaster: 
                                    print("-" + str(choice))
                                for i in range(quant):
                                    choice = input("Choice? ")
                                    onOff = True
                                    while onOff == True: 
                                        if choice in sightsMaster:
                                            sights.append(choice)
                                            onOff = False
                                        else: 
                                            print("That was incorrect. Please input a valid option.")
                        else:
                            if tagIdentify == "^": 
                                if len(tagInfo.split("/")) > 2 or (len(tagInfo.split("/") > 1 and not (tagInfo.split("/")[0] == "Any"))):
                                    print("Choose one of the following to have resistance to:")
                                    resistanceDamageChoices = []
                                    for choice in tagInfo.split(",")[0].split("/"): 
                                        print("-" + str(choice))
                                        resistanceDamageChoices.append(choice)
                                    choice = input("Choice? ")
                                    onOff = True
                                    while onOff == True: 
                                        if choice in resistanceDamageChoices:
                                            damageResistances.append(choice)
                                            onOff = False
                                        else: 
                                            print("That was incorrect. Please input a valid option.")
                                else:
                                    if len(tagInfo.split("/")) > 1:
                                        quant = int(tagInfo.split("/")[1])
                                    else:
                                        quant = 1
                                    print("Choose " + str(quant) + " of the following to have resistance to:")
                                    for choice in damageTypes: 
                                        print("-" + str(choice))
                                    for i in range(quant):
                                        choice = input("Choice? ")
                                        onOff = True
                                        while onOff == True: 
                                            if choice in damageTypes:
                                                resistanceDamageChoices.append(choice)
                                                onOff = False
                                            else: 
                                                print("That was incorrect. Please input a valid option.")
                            else:
                                if tagIdentify == "!":
                                    if len(tagInfo.split("/")) > 2 or (len(tagInfo.split("/") > 1 and not (tagInfo.split("/")[0] == "Any"))):
                                        print("Choose one of the following weapons:")
                                        weaponsChoices = []
                                        for choice in tagInfo.split(",")[0].split("/"): 
                                            print("-" + str(choice))
                                            weaponsChoices.append(choice)
                                        choice = input("Choice? ")
                                        onOff = True
                                        while onOff == True: 
                                            if choice in weaponsChoices:
                                                for simpleMartial in weapons:
                                                    for weaponType in simpleMartial:
                                                        for weapon in weaponType:
                                                            if choice == weapon[0]:
                                                                weapon[5] == True
                                                onOff = False
                                            else: 
                                                print("That was incorrect. Please input a valid option.")
                                    else:
                                        if len(tagInfo.split("/")) > 1:
                                            quant = int(tagInfo.split("/")[1])
                                        else:
                                            quant = 1
                                        print("Choose " + str(quant) + " of the following weapons:")
                                        for simpleMartial in weapons:
                                            for weaponType in simpleMartial:
                                                for weapon in weaponType:
                                                    print("-" + str(weapon[0]))
                                        for i in range(quant):
                                            choice = input("Choice? ")
                                            onOff = True
                                            while onOff == True: 
                                                if choice in toolsMaster:
                                                    for simpleMartial in weapons:
                                                        for weaponType in simpleMartial:
                                                            for weapon in weaponType:
                                                                if choice == weapon[0]:
                                                                    weapon[5] == True
                                                    onOff = False
                                                else: 
                                                    print("That was incorrect. Please input a valid option.")
                                else:
                                    if tagIdentify == "=":
                                        if len(tagInfo.split("/")) > 2 or (len(tagInfo.split("/") > 1 and not (tagInfo.split("/")[0] == "Any"))):
                                            print("Choose one of the following tools:")
                                            toolsChoices = []
                                            for choice in tagInfo.split(",")[0].split("/"): 
                                                print("-" + str(choice))
                                                toolsChoices.append(choice)
                                            choice = input("Choice? ")
                                            onOff = True
                                            while onOff == True: 
                                                if choice in toolsChoices:
                                                    tools.append(choice)
                                                    onOff = False
                                                else: 
                                                    print("That was incorrect. Please input a valid option.")
                                        else:
                                            if len(tagInfo.split("/")) > 1:
                                                quant = int(tagInfo.split("/")[1])
                                            else:
                                                quant = 1
                                            print("Choose " + str(quant) + " of the following tools:")
                                            for choice in toolsMaster: 
                                                print("-" + str(choice))
                                            for i in range(quant):
                                                choice = input("Choice? ")
                                                onOff = True
                                                while onOff == True: 
                                                    if choice in toolsMaster:
                                                        tools.append(choice)
                                                        onOff = False
                                                    else: 
                                                        print("That was incorrect. Please input a valid option.")
                                    else:
                                        if tagIdentify == "'":
                                            #This one's a bit harder because of all the moving parts.
                                            if len(tagInfo.split(",")[3].split("/")) > 1:
                                                print("Choose one of the following spells:")
                                                spellChoices = []
                                                for choice in tagInfo.split(",")[3].split("/"): 
                                                    print("-" + str(choice))
                                                    spellChoices.append(choice)
                                                choice = input("Choice? ")
                                                onOff = True
                                                while onOff == True: 
                                                    if choice in spellChoices:
                                                        fullSpell = tagInfo.split(",")[0] + "," + tagInfo.split(",")[1] + "," + tagInfo.split(",")[2] + "," + choice
                                                        spells.append(choice)
                                                        onOff = False
                                                    else: 
                                                        print("That was incorrect. Please input a valid option.")
                                            else:
                                                if len(tagInfo.split("/")) > 1:
                                                    quant = int(tagInfo.split("/")[1])
                                                else:
                                                    quant = 1
                                                print("Choose " + str(quant) + " of the following spells:")
                                                for choice in spellLists[tagInfo.split(",")[2]][tagInfo.split(",")[1]]:
                                                    print("-" + str(choice))
                                                for i in range(quant):
                                                    choice = input("Choice? ")
                                                    onOff = True
                                                    while onOff == True: 
                                                        if choice in spellLists[tagInfo.split(",")[2]][tagInfo.split(",")[1]]:
                                                            spells.append(choice)
                                                            onOff = False
                                                        else: 
                                                            print("That was incorrect. Please input a valid option.")
                                        else:
                                            if tagIdentify == "[":
                                                if len(tagInfo.split("/")) > 2 or (len(tagInfo.split("/") > 1 and not (tagInfo.split("/")[0] == "Any"))):
                                                    print("Choose one of the following weapons:")
                                                    skillChoices = []
                                                    for choice in tagInfo.split(",")[0].split("/"): 
                                                        print("-" + str(choice))
                                                        skillChoices.append(choice)
                                                    choice = input("Choice? ")
                                                    onOff = True
                                                    while onOff == True: 
                                                        if choice in skillChoices:
                                                            skills[choice] = True
                                                            onOff = False
                                                        else: 
                                                            print("That was incorrect. Please input a valid option.")
                                                else:
                                                    if len(tagInfo.split("/")) > 1:
                                                        quant = int(tagInfo.split("/")[1])
                                                    else:
                                                        quant = 1
                                                    print("Choose " + str(quant) + " of the following weapons:")
                                                    for skill in skills:
                                                        print("-" + str(skill))
                                                    for i in range(quant):
                                                        choice = input("Choice? ")
                                                        onOff = True
                                                        while onOff == True: 
                                                            if choice in skills:
                                                                skills[choice] = True
                                                                onOff = False
                                                            else: 
                                                                print("That was incorrect. Please input a valid option.")
                                            else:
                                                if tagIdentify == "%":
                                                    if len(tagInfo.split("/")) > 2 or (len(tagInfo.split("/") > 1 and not (tagInfo.split("/")[0] == "Any"))):
                                                        print("Choose one of the following fighting styles:")
                                                        fightingStyleChoices = []
                                                        for choice in tagInfo.split(",")[0].split("/"): 
                                                            print("-" + str(choice))
                                                            fightingStyleChoices.append(choice)
                                                        choice = input("Choice? ")
                                                        onOff = True
                                                        while onOff == True: 
                                                            if choice in fightingStyleChoices:
                                                                fightingStyles.append(choice)
                                                                onOff = False
                                                            else: 
                                                                print("That was incorrect. Please input a valid option.")
                                                    else:
                                                        if len(tagInfo.split("/")) > 1:
                                                            quant = int(tagInfo.split("/")[1])
                                                        else:
                                                            quant = 1
                                                        print("Choose " + str(quant) + " of the following fighting styles:")
                                                        for choice in fightingStylesMaster: 
                                                            print("-" + str(choice))
                                                        for i in range(quant):
                                                            choice = input("Choice? ")
                                                            onOff = True
                                                            while onOff == True: 
                                                                if choice in fightingStylesMaster:
                                                                    fightingStyles.append(choice)
                                                                    onOff = False
                                                                else: 
                                                                    print("That was incorrect. Please input a valid option.")
                                                else:
                                                    if tagIdentify == "~":
                                                        #back to the one's that don't quite make sense. But, ya know, it's fine. Perfectly fine.
                                                        if len(tagInfo.split("/")) > 2 or (len(tagInfo.split("/") > 1 and not (tagInfo.split("/")[0] == "Any"))):
                                                            print("Choose one of the following saving throw advantages:")
                                                            savingThrowChoices = []
                                                            for choice in tagInfo.split(",")[0].split("/"): 
                                                                print("-" + str(choice))
                                                                savingThrowChoices.append(choice)
                                                            choice = input("Choice? ")
                                                            onOff = True
                                                            while onOff == True: 
                                                                if choice in savingThrowChoices:
                                                                    savingThrowProfs.append(choice)
                                                                    onOff = False
                                                                else: 
                                                                    print("That was incorrect. Please input a valid option.")
                                                        else:
                                                            if len(tagInfo.split("/")) > 1:
                                                                quant = int(tagInfo.split("/")[1])
                                                            else:
                                                                quant = 1
                                                            print("Choose " + str(quant) + " of the following to have resistance to:")
                                                            for choice in savingThrowsMaster: 
                                                                print("-" + str(choice))
                                                            for i in range(quant):
                                                                choice = input("Choice? ")
                                                                onOff = True
                                                                while onOff == True: 
                                                                    if choice in savingThrowsMaster:
                                                                        savingThrowProfs.append(choice)
                                                                        onOff = False
                                                                    else: 
                                                                        print("That was incorrect. Please input a valid option.")
                                                    else:
                                                        if tagIdentify == "|":
                                                            print("Hey there! Pretty sure there is absolutely no reason why your character should be making a choice about getting an ability score improvement- you may need to fix this in your homebrew.")
                                                            #There is no way for this to work and no way I'm coding it. 
                                                        else:
                                                            if tagIdentify == "$":
                                                                if len(tagInfo.split("/")) > 2 or (len(tagInfo.split("/") > 1 and not (tagInfo.split("/")[0] == "Any"))):
                                                                    print("Choose one of the following spells:")
                                                                    spellChoices = []
                                                                    for choice in tagInfo.split(",")[0].split("/"): 
                                                                        print("-" + str(choice))
                                                                        spellChoices.append(choice)
                                                                    choice = input("Choice? ")
                                                                    onOff = True
                                                                    while onOff == True: 
                                                                        if choice in spellChoices:
                                                                            spellListExtra.append(choice)
                                                                            onOff = False
                                                                        else: 
                                                                            print("That was incorrect. Please input a valid option.")
                                                                else:
                                                                    if len(tagInfo.split("/")) > 1:
                                                                        print("Alright, you got some issues that must be fixed in the homebrew. I can already etll you that allowing anyone to choose any spells defeats the purpose of having different spellcasting classes- besides, it doesn't work right now. Sorry.")