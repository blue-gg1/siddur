import os, json
import pandas as pd 


def LoadJsonFromFile():
    global RawJson
    RawJson = open(str(os.getcwd())+"/Text/TanachPublicDomain.json", "r")

def main():
    print("starting")


def Testing():
    # print(str(RawJson.read()))
    item_dict = json.loads(str(RawJson.read))
    print(item_dict)
    print (len(item_dict['text'][0]['sectionNames']))






# main()
LoadJsonFromFile()
Testing()