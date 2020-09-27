import threading
import time
import Graphics
import OCR
import Upload
import settings
import yaml

def read_config(query):
    file = open("settings.yaml")
    parsed = yaml.load(file, Loader=yaml.FullLoader)

    return parsed[query]


def read_whole_config():
    file = open("settings.yaml")
    parsed = yaml.load(file, Loader=yaml.FullLoader)

    return parsed


def write_to_config(key, value):
    print("Writing: " + str(key) + " | " + str(value))
    parsed = read_whole_config()
    parsed[key] = value

    with open("settings.yaml", "w", encoding="utf8") as outFile:
        yaml.dump(parsed, outFile)


def main():
    settings.Variables.pytesseractPath = read_config("pytesseractPath")

    settings.Variables.displayName = read_config("displayName")

    settings.Variables.layerID = read_config("layerID")

    settings.Variables.layerName = read_config("layerName")

    settings.Variables.layerName = read_config("layerName")

    settings.Variables.saveImages = str(read_config("saveImages"))

    settings.Variables.doUpload = str(read_config("doUpload"))

    threading.Thread(target=refresh_coordinates_thread).start()
    threading.Thread(target=still_online_thread).start()
    Graphics.start_gui()


def refresh_coordinates_thread():
    time.sleep(2)
    Upload.new_ship(0,0,0,settings.Variables.layerName,settings.Variables.layerID)
    nextGetTime = 0
    while True:
        if time.time() > nextGetTime:
            nextGetTime = time.time() + 0.2
            threading.Thread(target=OCR.refresh_coordinates()).start()

        if OCR.Coordinates.success:
            OCR.Coordinates.success = False
            # noinspection SpellCheckingInspection
            threading.Thread(target=Upload.move_ship, args=(
                OCR.Coordinates.x, OCR.Coordinates.y, OCR.Coordinates.z, settings.Variables.layerName, settings.Variables.layerID)).start()

            coordinates_display = ""

            coordinates_display = coordinates_display + "X: " + str(Upload.Vars.latestOnlineX)
            for i in range(0, 10 - len(str(Upload.Vars.latestOnlineX))):
                coordinates_display = coordinates_display + " "

            coordinates_display = coordinates_display + "\n"

            coordinates_display = coordinates_display + "Y: " + str(Upload.Vars.latestOnlineY)
            for i in range(0, 10 - len(str(Upload.Vars.latestOnlineY))):
                coordinates_display = coordinates_display + " "

            coordinates_display = coordinates_display + "\n"

            coordinates_display = coordinates_display + "Z: " + str(Upload.Vars.latestOnlineZ)
            for i in range(0, 10 - len(str(Upload.Vars.latestOnlineZ))):
                coordinates_display = coordinates_display + " "

            Graphics.GUI.set_online_coordinates(coordinates_display)

def still_online_thread():
    while True:
        time.sleep(64)
        Upload.still_online()
        print("Still online...")


if __name__ == "__main__":
    main()
