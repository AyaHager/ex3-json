import json

dictBetweenIdAndName = {}

def readFile():
    file = open("�צאט WhatsApp עם יום הולדת בנות לנויה.txt", "r", encoding="utf-8")
    txt = file.readlines()
    file.close()
    return txt

def readBonusFile():
    file = open("�צ'אט WhatsApp עם מסיבת הפתעה לטולדנו🎉.txt", "r", encoding="utf-8")
    txt = file.readlines()
    file.close()
    return txt

def get_key(val):
    global dictBetweenIdAndName
    for key, value in dictBetweenIdAndName.items():
         if val == value:
             return key

def splitRow(line: str):
    global dictBetweenIdAndName
    global numOfParticipants
    if (len(line.split("-")) == 1):
        return line
    if(line.__contains__("הוסיף/ה")):
        return {}
    splitByHyphen = line.split("-", 1)
    if (len(splitByHyphen)==1):
        return {}
    dict = {}
    dict["datetime"] = splitByHyphen[0]
    splitByDots = splitByHyphen[1].split(":")
    if(len(splitByDots) == 1):
        return {}
    id = len(dictBetweenIdAndName)
    if(splitByDots[0] in dictBetweenIdAndName.values()):
        id = get_key(splitByDots[0])
    dictBetweenIdAndName[id] = splitByDots[0]
    dict["id"] = id
    dict["text"] = splitByDots[1]
    return dict

def getMetaData(someOfMetaData:str):
    dict = {}
    splitByHyphen = someOfMetaData.split("-", 1)
    dict["creation_date"] = splitByHyphen[0]
    splitByGershaim = splitByHyphen[1].split('"')
    dict["chat_name"] = splitByGershaim[1]
    creator = splitByGershaim[2][14:-2]
    dict["creator"] = creator
    dict["num_of_participants"] = "<" + str(len(dictBetweenIdAndName)) + ">"
    return dict

def getJsonFromNoyaBirthday():
    txt = readFile()
    listOfMessages = []
    someOfMetaData = txt[1]
    for line in txt:
        dict = splitRow(line)
        if (type(dict) == str):
            listOfMessages[-1]["text"] = listOfMessages[-1]["text"] + dict
        if(len(dict) > 0):
            listOfMessages.append(dict)
    metaData = getMetaData(someOfMetaData)
    finalDict = {}
    finalDict["messages"] = listOfMessages
    finalDict["metadata"] = metaData
    with open(metaData["chat_name"] + ".txt", 'w', encoding='utf8') as json_file:
        json.dump(finalDict, json_file, ensure_ascii=False)

def getJsonForBonus():
    txt = readBonusFile()
    listOfMessages = []
    someOfMetaData = txt[1]
    for line in txt:
        dict = splitRow(line)
        if (type(dict) == str):
            listOfMessages[-1]["text"] = listOfMessages[-1]["text"] + dict
        if(len(dict) > 0):
            listOfMessages.append(dict)
    metaData = getMetaData(someOfMetaData)
    finalDict = {}
    finalDict["messages"] = listOfMessages
    finalDict["metadata"] = metaData
    with open(metaData["chat_name"] + ".txt", 'w', encoding='utf8') as json_file:
        json.dump(finalDict, json_file, ensure_ascii=False)

if __name__ == '__main__':
    getJsonFromNoyaBirthday()
    dictBetweenIdAndName = {}
    getJsonForBonus()
