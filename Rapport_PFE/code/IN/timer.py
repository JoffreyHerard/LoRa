
class TimerL:
    def __init__(self,timing):
        self.seconds = 0
        self.__alarm = Timer.Alarm(self._seconds_handler, timing, periodic=True)
    def _seconds_handler(self, alarm):
        global isListening
        alarm.cancel() # stop it
        if isListening:
            isListening=False