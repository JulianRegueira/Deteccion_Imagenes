import win32gui
import win32ui
import win32con
import win32com.client
from PIL import Image


def SearchImage():
    hwnd_targets = []

    def enum_window_callback(hwnd, hwnd_targets):
        window_title = win32gui.GetWindowText(hwnd)
        if window_title == 'MU':
            hwnd_targets.append(hwnd)

    # Enumerar todas las ventanas y filtrar las que tengan el título "MU"
    win32gui.EnumWindows(enum_window_callback, hwnd_targets)

    for hwnd_target in hwnd_targets:
        print(hwnd_targets)

        left, top, right, bot = win32gui.GetWindowRect(hwnd_target)
        w = right - left
        h = bot - top

        if (w != 1600 and h != 900): # Queremos mantener el tamaño de la ventana siempre igual para que coincida con nuestras plantillas
            win32gui.MoveWindow(hwnd_target, left, top, 1600, 900, True)
            #print("Redimensionando ventana: Altura", h, " Ancho", w)

        # Truco para que setForeground siempre funcione
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.SendKeys('%')
        win32gui.SetForegroundWindow(hwnd_target)

        hdesktop = win32gui.GetDesktopWindow()
        hwndDC = win32gui.GetWindowDC(hdesktop)
        mfcDC  = win32ui.CreateDCFromHandle(hwndDC)
        saveDC = mfcDC.CreateCompatibleDC()

        saveBitMap = win32ui.CreateBitmap()
        saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)

        saveDC.SelectObject(saveBitMap)

        result = saveDC.BitBlt((0, 0), (w, h), mfcDC, (left, top), win32con.SRCCOPY)

        bmpinfo = saveBitMap.GetInfo()
        bmpstr = saveBitMap.GetBitmapBits(True)

        im = Image.frombuffer(
            'RGB',
            (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
            bmpstr, 'raw', 'BGRX', 0, 1)

        win32gui.DeleteObject(saveBitMap.GetHandle())
        saveDC.DeleteDC()
        mfcDC.DeleteDC()
        win32gui.ReleaseDC(hdesktop, hwndDC)

        if result == None:
            # PrintWindow Succeeded
            return im, (left, top, right, bot)
            # im.save("screenshot.png")
        
        return None