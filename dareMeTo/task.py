from datetime import datetime, timedelta
from random import randint

class Task:
    def __init__(self, task, duration):
        self.task = task
        self.duration = duration
        self.time = self.__random_time()
    
    def __random_time(self):
        now = datetime.now()

        action_time = self.__future_time(now)
        return action_time

    def __future_time(self, t):

        r_hours = randint(0,23)
        r_minutes = randint(10,59) # Minimum start from now is 10 minutes
        r_seconds = randint(0,59)
        return (t + timedelta(  hours = r_hours, 
                                minutes = r_minutes,
                                seconds = r_seconds)).strftime("%I:%M:%S %p")

    

