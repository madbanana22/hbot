import os, json

cfg: dict

def loadCfg():
    global cfg
    if os.path.isfile("pyrocfg.json"):
        file = open("pyrocfg.json", "r")
        cfg = json.loads(file.read())
        file.close()
    else:
        print("Config not found. Making a new one...")
        makeCfg()

def makeCfg():
    cfg["apikey"] = input("Enter your API key: ")
    cfg["cookie"] = input("Enter your cookie: ")
    
    writeCfg()

def writeCfg():
    file = open("pyrocfg.json", "w")
    newJson = json.dumps(cfg)
    file.write(newJson)
    file.close()