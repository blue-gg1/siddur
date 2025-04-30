import os, json
from pandas import *

def LoadJsonFromFile():
    RawJson = open(str(os.getcwd())+"/Text/TanachPublicDomain.json")
    BetterJson = json.dumps(RawJson)
    print(BetterJson)








def main():
    print("starting")

# main()
LoadJsonFromFile()