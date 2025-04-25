#    Sail client and any of its modules are covered under the GNU Public usage licence, see License.MD for more info
#    Copyright (C) 2025  Lietzen (gameyoshis@gmail.com)
import json
import os
import sys

from osinfo import *
plat = getosinfo("plat")
udir = getosinfo("udir")
def getsource(type):
    global src
    global amt
    # heheh, linux only 4 now
    if plat == "linux":
        srcdir = f'{udir}/.SailClient/sources.json'
        print(srcdir)
        with open(srcdir, "r") as file:
            src = json.load(file)
        amt = len(src)
        print(amt)
        # Use source[number] for now

    elif():
        print("wth are you running on?")
    if type == 1:
        return src
    if type == 2:
        return amt
def sourcenames():
#returns a list of the sources names
    sec = getsource(1)
    names = []
    for key, sources in src.items():
        for source in sources:
            names.append(source["name"])
    return names

def sourceurls():
    # Returns a list of the sources' URLs
    sec = getsource(1)
    urls = []
    for key, sources in src.items():
        for source in sources:
            urls.append(source["url"])
    return urls

#commented out for now
#if __name__ == "__main__":
#    print("This should not be run directly")