import os
from wizardSpells import spells
from weapons import weapons
sources = ["Dungeons & Dragons Official", "Unearthed Arcana", "SW5e", "Homebrew"]

testingThing = ["Elf", "Drow", "Fighter-02", "Acolyte", "Dexterity", "Charisma", "Constitution", "Strength", "Wisdom", "Intelligence"]
test = 0
testBool = 0

languagesDungeonsAndDragons = ["Common", "Elvish", "Dwarvish", "Giant", "Gnomish", "Goblin", "Halfling", "Orc", "Abyssal", "Celestial", "Deep Speech", "Draconic", "Infernal", "Primordial", "Sylvan", "Undercommon"]
skillsDungeonsAndDragons = {
    "Acrobatics": False,
    "Animal Handling": False,
    "Arcana": False,
    "Athletics": False,
    "Deception": False,
    "History": False,
    "Insight": False,
    "Intimidation": False,
    "Investigation": False,
    "Medicine": False,
    "Nature": False,
    "Perception": False,
    "Performance": False,
    "Persuasion": False,
    "Religion": False,
    "Sleight of Hand": False,
    "Stealth": False,
    "Survival": False
}
artisanTools = ["Alchemist's supplies", "Brewer's supplies", "Calligrapher's supplies", "Carpenter's tools", "Cartographer's tools", "Cobbler's tools", "Cook's tools", "Glassblower's tools", "Jeweler's tools", "Leatherworker's tools", "Mason's tools", "Painter's supplies", "Potter's tools", "Smith's tools", "Tinker's tools", "Weaver's tools", "Woodcarver's tools"]
gamingSets = ["Dice set", "Dragonchess set", "Playing card set", "Three-Dragon Ante set"]
musicalInstruments = ["Bagpipes", "Drum", "Dulcimer", "Flute", "Lute", "Lyre", "Horn", "Pan flute", "Shawm", "Viol"]

toolsMaster = ["Alchemist's supplies", "Brewer's supplies", "Calligrapher's supplies", "Carpenter's tools", "Cartographer's tools", "Cobbler's tools", "Cook's tools", "Glassblower's tools", "Jeweler's tools", "Leatherworker's tools", "Mason's tools", "Painter's supplies", "Potter's tools", "Smith's tools", "Tinker's tools", "Weaver's tools", "Woodcarver's tools", "Disguise kit", "Forgery kit", "Dice set", "Dragonchess set", "Playing card set", "Three-Dragon Ante set", "Herbalism kit", "Bagpipes", "Drum", "Dulcimer", "Flute", "Lute", "Lyre", "Horn", "Pan flute", "Shawm", "Viol", "Navigator's tools", "Poisoner's kit", "Thieves' tools", "Vehicles (land or water)"]
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
skills = []
toolsWeapons = []
languages = []
damageResistances = []
savingThrowConditionAdvantages = []
sights = []
savingThrowProfs = []
spellListExtra = []


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
    "=":toolsWeapons,
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

