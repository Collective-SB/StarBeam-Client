import Graphics
import mss
import pyautogui
import pytesseract
import settings
import time
from PIL import Image

class Coordinates:
    x = 0
    y = 0
    z = 0

    hasXUpdated = False
    hasYUpdated = False
    hasZUpdated = False
    do_push = False

    lastPushTime = 0

    success = False


def refresh_coordinates():
    image = screenshot()

    text = read_text(image)

    text = discard_from_text(text)

    new_x, new_y, new_z = parse(text, "x"), parse(text, "y"), parse(text, "z")

    if sanity_check(new_x):
        print("Updating X")
        Coordinates.x = new_x
        Coordinates.hasXUpdated = True

    if sanity_check(new_y):
        print("Updating Y")
        Coordinates.y = new_y
        Coordinates.hasYUpdated = True

    if sanity_check(new_z):
        print("Updating Z")
        Coordinates.z = new_z
        Coordinates.hasZUpdated = True

    coordinates_display = ""
    coordinates_display = coordinates_display + "X: " + str(Coordinates.x)
    for i in range(0, 10 - len(str(Coordinates.x))):
        coordinates_display = coordinates_display + " "

    coordinates_display = coordinates_display + "\n"

    coordinates_display = coordinates_display + "Y: " + str(Coordinates.y)
    for i in range(0, 10 - len(str(Coordinates.y))):
        coordinates_display = coordinates_display + " "

    coordinates_display = coordinates_display + "\n"

    coordinates_display = coordinates_display + "Z: " + str(Coordinates.z)
    for i in range(0, 10 - len(str(Coordinates.z))):
        coordinates_display = coordinates_display + " "

    Graphics.GUI.set_coordinates(coordinates_display)

    # I tried less annoying ways to do this but I ended up going with the simple method
    if Coordinates.hasXUpdated and Coordinates.hasYUpdated:  # 110
        Coordinates.do_push = True
    elif Coordinates.hasYUpdated and Coordinates.hasZUpdated:  # 011
        Coordinates.do_push = True

    elif Coordinates.hasXUpdated and Coordinates.hasZUpdated:  # 101
        Coordinates.do_push = True

    elif Coordinates.hasXUpdated and Coordinates.hasYUpdated and Coordinates.hasZUpdated:  # 111
        Coordinates.do_push = True

    if Coordinates.do_push and Coordinates.lastPushTime + 10 < time.time():
        Coordinates.lastPushTime = time.time()
        Coordinates.hasXUpdated = False
        Coordinates.hasYUpdated = False
        Coordinates.hasZUpdated = False
        Coordinates.do_push = False
        Coordinates.success = True

    else:
        Coordinates.success = False
        return False


def int_rnd(num):
    return int(round(num))


def screenshot():
    screen_x, screen_y = pyautogui.size()

    with mss.mss() as sct:
        area = {"top": int_rnd(screen_y / 2) + int_rnd(screen_y / 4), "left": int_rnd(screen_x / 4),
                "width": int_rnd(screen_x / 2), "height": int_rnd(screen_y / 4)}

        output = "sct-{top}x{left}_{width}x{height}.png".format(**area)

        sct_img = sct.grab(area)

        if settings.Variables.saveImages == "True":
            mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
            return Image.open(output)
        else:
            img = Image.frombytes("RGB", sct_img.size, sct_img.rgb, "raw")

            return img

def read_text(image):
    pytesseract.pytesseract.tesseract_cmd = settings.Variables.pytesseractPath

    return pytesseract.image_to_string(image, lang="eng", config="--user-words words.txt")


def discard_from_text(text):
    # means I don't have to look at random rubbish it picked up and probably improves performance too, cause this is
    # one discard step to speed up 3 read functions
    allow_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "X", "Y", "Z", ":", ".", "-", "%"]
    new_text = ""

    for char in text:
        if char in allow_list:
            new_text = new_text + char

    return new_text.replace("x", "X").replace("y", "Y").replace("¥", "Y").replace("%", "X")


def parse(text, search_letter):
    result = ""
    i = 0
    iterating_num = False

    # get rid of out of range when it looks for the colon after and it's at the end of the list
    text = text + " "

    endingArray = [".", "X", "x", "y", "Y", "z", "Z"]

    for c in text:
        if iterating_num:
            char = c.replace("Z", "2").replace("z", "2")

        else:
            char = c.replace("2", "Z")

        if char == search_letter.lower() or char == search_letter.upper():
            if text[i + 1] == ":":
                iterating_num = True

        if char in endingArray and iterating_num == True and not char == search_letter.lower() and not char == search_letter.upper():
            iterating_num = False

        if iterating_num:
            result = result + char

        i = i + 1

    # remove the "X:"
    result = result[2:]

    # fix 2's sometimes being read as Z's
    result = result.replace("Z", "2")

    return result


def sanity_check(value):
    try:
        int(value)
        return True
    except (TypeError, ValueError):
        return False
