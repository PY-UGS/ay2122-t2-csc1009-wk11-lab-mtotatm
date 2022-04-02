class clockTime:

    def __init__(self):
        self._hours = 12
        self._minutes = 0
        self._seconds = 0

    def getHours(self):
        return self._hours

    def setHours(self, hours):
        self._hours = hours

    def getMinutes(self):
        return self._minutes

    def setMinutes(self, minutes):
        self._minutes = minutes

    def getSeconds(self):
        return self._seconds

    def setSeconds(self, seconds):
        self._seconds = seconds

    def setTime(self,hours,minutes,seconds):
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds

    def show(self):
        print ("%d:%02d:%02d" % (self._hours, self._minutes, self._seconds))

clock = clockTime()
clock.setTime(6,30,35)
clock.show()