class LoggableList(list, Loggable):
    def append(self, x):
        self.log(x)
        super().append()