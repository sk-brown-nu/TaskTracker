import win32gui
import time
import win32process
import wmi

c = wmi.WMI()


def get_app_name(hwnd):
    try:
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        for p in c.query('SELECT Name FROM Win32_Process WHERE ProcessId = %s' % str(pid)):
            exe = p.Name
            break
    except:
        return None
    else:
        return exe


if __name__ == '__main__':
    active_app_name = ""
    while True:
        new_app = win32gui.GetForegroundWindow()
        new_app_name = get_app_name(new_app)

        if active_app_name != new_app_name:
            active_app_name = new_app_name
            print(active_app_name)

        time.sleep(3)
