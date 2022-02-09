import pyautogui

max_tries = 10

def get(image):
    r = None
    tries = max_tries
    if(image == "find_match"):
        tries = 15
    elif(image == "accept"):
        tries = 9999999
    while r is None and tries > 0:
        print(image, tries)
        r=pyautogui.locateOnScreen('images/'+image+'.png', confidence=.7)
        tries = tries - 1
    if tries == 0:
        return r
    return r