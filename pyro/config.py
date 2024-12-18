import os, json, getpass

cfg: dict = {}

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
    global cfg
    cfg["apikey"] = getpass.getpass("Telegram API key: ")
    cfg["cookie"] = getpass.getpass("  Journal cookie: ")
    cfg["path"] =             input("    Link: diary/s/")
    writeCfg()

def writeCfg():
    file = open("pyrocfg.json", "w")
    newJson = json.dumps(cfg)
    file.write(newJson)
    file.close()