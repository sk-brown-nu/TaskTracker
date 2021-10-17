import win32gui
import time
import win32process
import wmi
import json

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


def write_json(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


def is_new_task(app):
    with open('tasks.json', "r") as file:
        data = json.load(file)
        tasks = data["tasks"]
        for task in tasks:
            if task["name"] == app:
                return False
        return True


if __name__ == '__main__':
    active_app_name = ""
    while True:
        new_app = win32gui.GetForegroundWindow()
        new_app_name = get_app_name(new_app)

        if active_app_name != new_app_name:
            active_app_name = new_app_name

            if is_new_task(active_app_name):
                with open('tasks.json', "r") as file:
                    data = json.load(file)
                    tasks = data["tasks"]
                    entry = {"name": active_app_name}
                    tasks.append(entry)

                write_json(data, 'tasks.json')

            print(active_app_name)

        time.sleep(3)
