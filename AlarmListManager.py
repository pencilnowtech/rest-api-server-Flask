from Alarm import Alarm

dummy_alarm1 = Alarm(1, "Jon-alarm", "20:00", 1, [2, 4])
dummy_alarm2 = Alarm(2, "Jon-alarm", "20:00", 1, [2, 4])
dummy_alarm3 = Alarm(3, "Jon-alarm", "20:00", 1, [2, 4])

AlarmListData = [dummy_alarm1, dummy_alarm2, dummy_alarm3]

class AlarmListManager:
    def getAlarmsList(self):
        alarms = []
        for alarm in AlarmListData:
            alarms.append(alarm.getData())
        return alarms

    def AddAlarm(self, data):
        alarm = Alarm(data['alarm_id'], data['name'],
                      data['time'], data['status'], data['days'])
        AlarmListData.append(alarm)
        return 'Success'

    def findAlarm(self, alarm_id):
        for alarm in AlarmListData:
            if (alarm.getId() == alarm_id):
                return 'Success', alarm.getData()
        else:
            return 'Failure', {}

    def deleteAlarm(self, alarm_id):
        for index, alarm in enumerate(AlarmListData):
            if (alarm.getId() == alarm_id):
                del(AlarmListData[index])
                return 'Success'
        else:
            return 'Failure'

    def updateAlarm(self, alarm_id, new_alarm):
        for index, alarm in enumerate(AlarmListData):
            if (alarm.getId() == alarm_id):
                AlarmListData[index].updateAlarm(new_alarm['alarm_id'], new_alarm['name'],
                                                      new_alarm['time'], new_alarm['status'], new_alarm['days'])
                return 'Success'
        else:
            return 'Failure'
