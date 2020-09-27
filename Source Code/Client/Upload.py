import requests
import settings
import Graphics

class Vars:
    baseUrl = "http://173.212.194.49:5000"
    latestOnlineX = 0
    latestOnlineY = 0
    latestOnlineZ = 0
    shipID = ""

def move_ship(x, y, z, layer, layerid):
    if settings.Variables.doUpload == "False":
        return
    Vars.latestOnlineX = x
    Vars.latestOnlineY = y
    Vars.latestOnlineZ = z
    headers = {"xpos": str(x), "ypos": str(y), "zpos": str(z), "layername": layer, "layerid": layerid,
               "name": settings.Variables.displayName, "id" : Vars.shipID}

    requests.post(Vars.baseUrl + "/modifyplayer", headers=headers)


def new_ship(x, y, z, layer, layerid):
    if settings.Variables.doUpload == "False":
        return
    Vars.latestOnlineX = x
    Vars.latestOnlineY = y
    Vars.latestOnlineZ = z
    headers = {"xpos": str(x), "ypos": str(y), "zpos": str(z), "layername": layer, "layerid": layerid,
               "name": settings.Variables.displayName}

    r = requests.post(Vars.baseUrl + "/newplayer", headers=headers)
    Vars.shipID = r.text
    print("Assigned ID: " + Vars.shipID)

def still_online():
    if settings.Variables.doUpload == "False":
        return
    headers = {"id" : Vars.shipID}

    requests.post(Vars.baseUrl + "/stillonline", headers=headers)