class TimeEntry:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = end-start
