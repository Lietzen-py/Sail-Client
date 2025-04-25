#    Sail client and any of its modules are covered under the GNU Public usage licence, see License.MD for more info
#    Copyright (C) 2025  Lietzen (gameyoshis@gmail.com)
import os
from getsrc import *
import json
import qbittorrentapi
from logger import logger
conn_info = dict(
    host="localhost",
    port=8080,
    username="admin",
    password="adminadmin",
)
qbt_client = qbittorrentapi.Client(**conn_info)
def index(dsrc):
    src = getsource(1)
    keys = list(src.keys())
    len(keys)
    for key in keys:
        print("placeholder")

def getdesc(prod, dsrc):
    unfilteredurls = sourceurls()
    src = unfilteredurls[dsrc]

    try:
        desc = os.system(f"curl {src}/{prod}/description")
        return desc
    except BaseExceptionGroup:
        return ""

try:
    qbt_client.auth_log_in()
except qbittorrentapi.LoginFailed as e:
      logger("Dwnldmgr", "Qbittorrent is either not installed, or has a incorrect config...")

# Fuck trump btdubs