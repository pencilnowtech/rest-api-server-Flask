import uuid
from datetime import datetime

from enum import Enum


class AlarmStatus(Enum):
    INACTIVE = 0
    ACTIVE = 1


class Alarm:
    def __init__(self, alarm_id, name, time_str, status, days):
        self.__id = alarm_id
        self.__name = name
        self.__time = datetime.strptime(time_str, '%H:%M')
        self.__status = AlarmStatus(status)
        self.__days = days.copy()

    def getId(self):
        return self.__id

    def setId(self, alarm_id):
        self.__id = alarm_id

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getTime(self):
        return self.__time.strftime('%H:%M')

    def setTime(self, time_str):
        self.__time = datetime.strptime(time_str, '%H:%M')

    def getStatus(self):
        return self.__status

    def setStatus(self, status):
        self.__status = AlarmStatus(int(status))

    def getDays(self):
        return self.__days

    def setDays(self, days):
        self.__days = days.copy()

    def updateAlarm(self, alarm_id, name, time_str, status, days):
        self.__id = alarm_id
        self.__name = name
        self.__time = datetime.strptime(time_str, '%H:%M')
        self.__status = AlarmStatus(status)
        self.__days = days.copy()

    def getData(self):
        return ({"alarm_id": self.getId(), "name": self.getName(), "time": self.getTime(), "status": self.getStatus().value, "days": self.getDays()})

    def __str__(self):
        return (f'"alarm_id": "{self.getId()}","name":"{self.getName()}", "time":"{self.getTime()}", "status":"{self.getStatus().value}","days": "{self.getDays()}"')
