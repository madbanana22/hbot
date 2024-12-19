import config, parse, bot, sys, user
from argparse import ArgumentParser

print("Pyrobot v0.1")

print("> Parsing arguments...")

parser = ArgumentParser()
parser.add_argument("-n", "--nobot", help="Start without the bot", action="store_true")
parser.add_argument("-r", "--reconfig", help="Reset configuration", action="store_true")

args = parser.parse_args()

print("> Loading config")
if args.reconfig:
    config.makeCfg()

config.loadCfg()

print("> Initializing bot")

if not args.nobot:
    bot.init()