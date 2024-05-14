import time
import ctypes
import win32gui
import win32api
import win32con
import pyautogui

# Callback function for window enumeration
def EnumWindowCallback(hwnd, lParam):
    global HWND_CalSheet
    text = win32gui.GetWindowText(hwnd)
    if "Calibration entry sheet" in text:
        HWND_CalSheet = hwnd

        return False
    return True

# Simulate clicking on "Take Measurements" button
def take_measurement(hwnd_cal_sheet, hwnd_take_meas):
    rect = win32gui.GetWindowRect(hwnd_take_meas)
    center_x = (rect[0] + rect[2]) // 2
    center_y = (rect[1] + rect[3]) // 2
    pyautogui.click(center_x, center_y)

# Main function to take CS043 reading
def take_cs043_reading():
    global HWND_CalSheet
    HWND_CalSheet = 0
    try:
        win32gui.EnumWindows(EnumWindowCallback, 0)
    except:
        if HWND_CalSheet != 0:
            hwnd_take_meas = win32gui.FindWindowEx(HWND_CalSheet, 0, None, "Take Measurement")
            if hwnd_take_meas != 0:
                take_measurement(HWND_CalSheet, hwnd_take_meas)
                time.sleep(0.4)
                text = ""
                while not text.startswith("Take"):
                    time.sleep(0.2)
                    win32gui.SendMessage(hwnd_take_meas, win32con.WM_GETTEXT, 18, text)
#             # Button is enabled again, measurement process completed
    return

# Entry point
# if __name__ == "__main__":
#     take_cs043_reading()