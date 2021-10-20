import win32gui
import time
import win32process
import wmi
import json
import datetime
from task import *


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
    c = wmi.WMI()
    active_app_name = ""
    start_time = datetime.datetime.now()
    task_list = TaskList([])
    first_time = True

    try:
        task_list.initialise_me()
    except Exception:
        print("No json or read json failed.")

    try:
        while True:
            new_app = win32gui.GetForegroundWindow()
            new_app_name = get_app_name(new_app)

            if active_app_name != new_app_name:
                active_app_name = new_app_name

                if not first_time:
                    end_time = datetime.datetime.now()
                    time_entry = TimeEntry(start_time, end_time)

                    exists = False
                    for task in task_list.tasks:
                        if task.name == active_app_name:
                            exists = True
                            task.time_entries.append(time_entry)

                    if not exists:
                        task = Task(active_app_name, [time_entry])
                        task_list.tasks.append(task)
                    with open('tasks.json', "w") as file:
                        json.dump(task_list.serialise(), file, indent=4)
                        start_time = datetime.datetime.now()

                first_time = False
                active_app_name = new_app_name

            time.sleep(1)

    except KeyboardInterrupt:
        with open('tasks.json', "w") as file:
            json.dump(task_list.serialise(), file, indent=4)
