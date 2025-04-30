import os

def LoadJsonFromFile():
    with open(str(os.getcwd())+"/Text/TanachPublicDomain.json") as RawJson:
        print(RawJson.read())









def main():
    print("starting")

# main()
LoadJsonFromFile()