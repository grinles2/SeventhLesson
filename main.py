class PC:
    def __init__(self):
        self.memory = 128
        super().__init__()
class Monitor:
    def __init__(self):
        super().__init__()
        self.resolution = "4K"
class Phone(PC, Monitor):
    def print_info(self):
        print(self.memory)
        print(self.resolution)
iphone = Phone()
iphone.print_info()