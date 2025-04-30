import os, json
import pandas as pd 


def LoadJsonFromFile():
    global RawJson
    RawJson = open(str(os.getcwd())+"/Text/TanachPublicDomain.json")

def main():
    print("starting")


def Testing():
    item_dict = json.loads(RawJson)
    print (len(item_dict['result'][0]['run']))






# main()
LoadJsonFromFile()
Testing()