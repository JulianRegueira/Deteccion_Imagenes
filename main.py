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

def showImage(img, max_loc):

    def getCoords(template, max_loc):
        w, h = template.shape[::-1]
        bottom_right = (max_loc[0] + w, max_loc[1] + h)
        return bottom_right
    
def click(x, y):
    current_x, current_y = pyautogui.position()
    pyautogui.click(x, y)
    pyautogui.moveTo(current_x, current_y) # We go back to where we were

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
    Bless = cv2.imread('./templates/Arco.jpg', 0)
    Soul = cv2.imread('./templates/Arcoprueba.jpg', 0)

    while(True):
        try:
            # Bless
            found, max_val = searchTemplate(Bless, accuracy=0.5)
            print(found, max_val)
            #if found:
                #windowsbeep(300,2000)
        except Exception as e:
            print(e) 
        time.sleep(5)