from datetime import datetime, timedelta, time
from random import randint

class Task:
    def __init__(self, task, duration):
        self.task = task
        self.duration = duration
        self.time = self.__random_time()
    
    def __random_time(self):
        now = datetime.utcnow().time()

        action_time = self.__future_time(now)
        return action_time

    def __future_time(self, t):

        r_hour = randint(0,23)
        r_minute = randint(10,59) # Minimum start from now is 10 minutes
        r_second = randint(0,59)

        return  time(hour = r_hour, minute = r_minute, second = r_second)
        

    

