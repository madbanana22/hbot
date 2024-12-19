import os, json, getpass

cfg: dict = {}

def loadCfg():
    global cfg
    if os.path.isfile("pyrocfg.json"):
        file = open("pyrocfg.json", "r")
        cfg = json.loads(file.read())
        file.close()
    else:
        makeCfg()

def makeCfg():
    print("Making config")
    global cfg
    cfg["apikey"] = getpass.getpass("Enter your bot's Telegram API key: ")
    cfg["ownerId"] = input("Enter your Telegram ID: ")
    cfg["user"] = input("Enter your journal username:")
    cfg["pass"] = getpass.getpass("Enter your journal password:")
    #cfg["cookie"] = getpass.getpass("  Journal cookie: ")
    #cfg["path"] =             input("    Link: diary/s/") # no longer needed, now we directly talk to the api like the cool kids

    if input("Set logchat? y/n: ").lower() == "y":
        cfg["logchat"] =      input("      Logchat ID: ")

    writeCfg()

def writeCfg():
    print("Writing config")
    file = open("pyrocfg.json", "w")
    newJson = json.dumps(cfg)
    file.write(newJson)
    file.close()