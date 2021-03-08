from AlarmListManager import AlarmListManager
from flask import Flask, request, jsonify, render_template, abort, Response


api = Flask(__name__)
alarmList = AlarmListManager()


@api.route('/alarms', methods=['GET'])
def list_alarms():
    return jsonify({"alarms": alarmList.getAlarmsList()})


@api.route('/alarms', methods=['POST'])
def add_alarm():
    print('hi')
    alarm_data = request.get_json()
    print(alarm_data)
    return_status = alarmList.AddAlarm(alarm_data)
    return jsonify({'message': return_status})


@api.route('/alarm/<int:alarm_id>', methods=['GET'])
def get_alarm(alarm_id):
    return_status, alarm = alarmList.findAlarm(alarm_id)

    if return_status == 'Failure':
        status_code = Response(status=404)
        return status_code

    return jsonify(alarm)


@api.route('/alarm/<int:alarm_id>', methods=['DELETE'])
def delete_alarm(alarm_id):
    return_status = alarmList.deleteAlarm(alarm_id)

    if return_status == 'Failure':
        abort(404)

    return jsonify({'message': return_status})


@api.route('/alarm/<int:alarm_id>', methods=['PUT'])
def update_alarm(alarm_id):
    print('hi')
    new_alarm = request.get_json()
    return_status = alarmList.updateAlarm(alarm_id, new_alarm)

    if return_status == 'Failure':
        status_code = Response(status=404)
        return status_code

    return jsonify({'message': return_status})


@api.errorhandler(404)
def alarm_not_found(e):
    return render_template("404.html")
