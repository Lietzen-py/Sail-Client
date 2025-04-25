#    Sail client and any of its modules are covered under the GNU Public usage licence, see License.MD for more info
#    Copyright (C) 2025  Lietzen (gameyoshis@gmail.com)
from colorama import Fore
def logger(arg1, arg2): # logger("log, debug, mod, command", "message") Supports F
    if arg1.lower() == "debug":
        status = Fore.GREEN + "[debug]".upper()
    if arg1.lower() == "log":
        status = Fore.LIGHTBLACK_EX + "[log]".upper()
    if arg1.lower() == "bad":
        status = Fore.RED + "[bad!]".upper()
    if arg1.lower() == "warn":
        status = Fore.YELLOW + "[warn]".upper()
    if arg1.lower() == "extension":
        status = Fore.CYAN + "[extension]".upper()
    if arg1.lower() == "Dwnldmgr":
        status = Fore.BLUE + "[download manager]".upper()
    print(f"{status} {Fore.RESET} {arg2}")