class Task:
    def __init__(self, name, time_entries):
        self.name = name
        self.time_entries = time_entries


class TimeEntry:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = end-start
