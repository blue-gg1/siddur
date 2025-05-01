import os, json
import pandas as pd 


def LoadJsonFromFile():
    global RawJson
    RawJson = open(str(os.getcwd())+"/Text/TanachPublicDomain.json", "r")

def PrintChaperByNumber(KapitelNumber):
    print(KapitelNumber)
    global KapitelList
    LoadJsonFromFile()
    KapitelList = json.loads(str(RawJson.read()))
    print(KapitelList['text'][KapitelNumber])


def Testing():
    PrintChaperByNumber(1)
    # print(KapitelList)
    pass



def main():
    pass


# main()
# LoadJsonFromFile()
Testing()