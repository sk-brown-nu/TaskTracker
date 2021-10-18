class TaskList:
    def __init__(self, tasks):
        self.tasks = tasks

    def serialise(self):
        return {
            "tasks": self.get_serialised_tasks()
        }

    def get_serialised_tasks(self):
        serialised_list = []
        for task in self.tasks:
            serialised_list.append(task.serialise())
        return serialised_list


class Task:
    def __init__(self, name, time_entries):
        self.name = name
        self.time_entries = time_entries

    def get_serialised_time_entries(self):
        serialised_list = []
        for entry in self.time_entries:
            serialised_list.append(entry.serialise())
        return serialised_list

    def serialise(self):
        return {
            "name": self.name,
            "time_entries": self.get_serialised_time_entries()
        }


class TimeEntry:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.duration = end-start
        duration_in_seconds = self.duration.total_seconds()
        self.hours = divmod(duration_in_seconds, 3600)
        self.minutes = divmod(self.hours[1], 60)
        self.seconds = divmod(self.minutes[1], 1)

    def serialise(self):
        return {
            "start": self.start.strftime("%Y-%m-%d %H:%M:%S"),
            "end": self.end.strftime("%Y-%m-%d %H:%M:%S"),
            "hours": self.hours[0],
            "minutes": self.minutes[0],
            "seconds": self.seconds[0]
        }
