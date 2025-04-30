import os, json
import pandas as pd 

def LoadJsonFromFile():
    RawJson = open(str(os.getcwd())+"/Text/TanachPublicDomain.json")
    DataFrame = pd.read_json(RawJson)
    print(DataFrame)







def main():
    print("starting")

# main()
LoadJsonFromFile()