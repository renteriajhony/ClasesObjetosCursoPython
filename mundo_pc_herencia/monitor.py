class Monitor:
    counter_monitor: int = 0
    def __init__(self, mark: str, size: float):
        Monitor.counter_monitor += 1
        self.id_monitor = Monitor.counter_monitor
        self.mark = mark
        self.size = size

    def __str__(self):
            return f'Id: {self.id_monitor}, Mark: {self.mark}, Size: {self.size}'