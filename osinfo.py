#    Sail client and any of its modules are covered under the GNU Public usage licence, see License.MD for more info
#    Copyright (C) 2025  Lietzen (gameyoshis@gmail.com)
import sys
import os
def getosinfo(obj):
    if sys.platform == "win32":
        plat = "windows"
        usrdir = os.path.expanduser('C:/Users/$USERNAME')
    if sys.platform == "linux":
        plat = "linux"
        usrdir = os.path.expanduser('~')
    if sys.platform == "darwin":
        plat = "macos"
        userdir = os.path.expanduser('~')
    if obj == "plat":
        return plat
    if obj == "udir":
        return usrdir
