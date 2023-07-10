import numpy as np
import time
import windowcapture
import pyautogui
import cv2
import winsound

def windowsbeep(duration, frequency):
    for _ in range(0,2):
        winsound.Beep(frequency, duration)
        winsound.Beep(frequency, duration)
        winsound.Beep(frequency, duration)
        time.sleep(1)

def get_xy_center(coords, max_loc, template):
    left, top, _, _ = coords
    w, h = template.shape[::-1]
    return left + max_loc[0] + w/2, top + max_loc[1] + h/2

def Buscar_Imagen():
    pil_img, coords = windowcapture.SearchImage()
    img = cv2.cvtColor(np.asarray(pil_img), cv2.COLOR_RGB2GRAY)
    return img, coords

def match_image(img, template):
    matching_method = cv2.TM_CCOEFF_NORMED
    # Apply template Matching
    res = cv2.matchTemplate(img, template, matching_method, mask=None)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    return max_val, max_loc
    
def click(x, y):
    current_x, current_y = pyautogui.position()
    pyautogui.click(x, y)
    pyautogui.moveTo(current_x, current_y)

def searchTemplate(template, accuracy=0.87):
    time.sleep(0.1)
    img, coords = Buscar_Imagen()
    max_val, max_loc = match_image(img, template)

    if (max_val > accuracy):     
        # Get the coordinates of the center of the image 
        x, y = get_xy_center(coords, max_loc, template)
        # Click it
        click(x, y)
        return True, max_val
    else:
        return False, max_val
    
def main():
    Bless = cv2.imread('./templates/Bless.jpg', 0)
    Soul = cv2.imread('./templates/Soul.jpg', 0)
    Chaos = cv2.imread('./templates/Chaos.jpg', 0)
    Life = cv2.imread('./templates/Life.jpg', 0)
    Item1 = cv2.imread('./templates/Item1.jpg', 0)
    Item2 = cv2.imread('./templates/Item2.jpg', 0)
    Item3 = cv2.imread('./templates/Item3.jpg', 0)
    Item4 = cv2.imread('./templates/Item4.jpg', 0)
    Item5 = cv2.imread('./templates/Item5.jpg', 0)

    while(True):
        try:
            # Bless
            found, max_val = searchTemplate(Bless, accuracy=0.9)
            print(found, max_val)
            if found:
                windowsbeep(100,500)
            # Soul
            found, max_val = searchTemplate(Soul, accuracy=0.9)
            print(found, max_val)
            if found:
                windowsbeep(100,500)
            # Chaos
            found, max_val = searchTemplate(Chaos, accuracy=0.9)
            print(found, max_val)
            if found:
                windowsbeep(100,500)
            found, max_val = searchTemplate(Life, accuracy=0.9)
            print(found, max_val)
            if found:
                windowsbeep(100,500)
            found, max_val = searchTemplate(Item1)
            print(found, max_val)
            if found:
                windowsbeep(100,500)
            found, max_val = searchTemplate(Item2)
            print(found, max_val)
            if found:
                windowsbeep(100,500)
            found, max_val = searchTemplate(Item3)
            print(found, max_val)
            if found:
                windowsbeep(100,500)
            found, max_val = searchTemplate(Item4)
            print(found, max_val)
            if found:
                windowsbeep(100,500)
            found, max_val = searchTemplate(Item5)
            print(found, max_val)
            if found:
                windowsbeep(100,500)
                
        except Exception as e:
            print(e) 
        time.sleep(2)