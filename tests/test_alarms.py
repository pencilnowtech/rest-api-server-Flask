import json

"""
List all the alarms
"""
def test_get_alarms(app, client):
    res = client.get('/alarms')
    assert res.status_code == 200
    expected = {"alarms": [{"days": [2, 4], "alarm_id":1, "name":"Jon-alarm", "status":1, "time":"20:00"},
                           {"days": [2, 4], "alarm_id":2, "name":"Jon-alarm", "status":1, "time":"20:00"},
                           {"days": [2, 4], "alarm_id":3, "name":"Jon-alarm", "status":1, "time":"20:00"}]}
    assert expected == json.loads(res.get_data(as_text=True))


"""
List a particular alarm (alarm_id=2)
"""
def test_get_alarm(app, client):
    res = client.get('/alarm/2')
    assert res.status_code == 200
    expected = {'days': [2, 4], 'alarm_id': 2, 'name': 'Jon-alarm', 'status': 1, 'time': '20:00'}
    assert expected == json.loads(res.get_data(as_text=True))


"""
List non-existent alarm (alarm_id=4)
"""
def test_get_alarm_invalid_id(app, client):
    res = client.get('/alarm/4')
    assert res.status_code == 404


"""
Delete a particular alarm (alarm_id=2)
"""
def test_delete_alarm(app, client):
    res = client.delete('/alarm/2')
    assert res.status_code == 200
    expected = {'message': 'Success'}
    assert expected == json.loads(res.get_data(as_text=True))


"""
delete non-existent alarm (alarm_id=4)
"""
def test_delete_alarm_invalid_id(app, client):
    res = client.delete('/alarm/4')
    assert res.status_code == 200
    expected = "\n\n<p>Alarm entry doesn't exists! (404)</p>\n\n"
    assert expected == res.get_data(as_text=True)


"""
Add a new alarm (alarm_id=1)
"""
def test_add_alarm(app, client):
    res = client.post('/alarms', json={
        "days": [3, 6], "alarm_id": 6, "name": "deep-alarm", "status": 1, "time": "08:00"
    })

    assert res.status_code == 200
    expected = {'message': 'Success'}
    assert expected == json.loads(res.get_data(as_text=True))

    # Verify newly added alarm along with others
    res = client.get('/alarms')
    assert res.status_code == 200
    expected = {"alarms": [{"days": [2, 4], "alarm_id":1, "name":"Jon-alarm", "status":1, "time":"20:00"},
                           {"days": [2, 4], "alarm_id":3, "name":"Jon-alarm", "status":1, "time":"20:00"},
                           {'days': [3, 6], 'alarm_id': 6, 'name': 'deep-alarm', 'status': 1, "time":"08:00"}]}
    assert expected == json.loads(res.get_data(as_text=True))


"""
Update alarm (alarm_id=4)
"""
def test_update_alarm(app, client):
    res = client.put('/alarm/6', json={
        "days": [3, 6], "alarm_id": 6, "name": "sukhdeep-alarm", "status": 1, "time": "06:00"
    })
    assert res.status_code == 200    

    #Verify newly added alarm
    res = client.get('/alarm/6')
    expected = {"days": [3, 6], "alarm_id": 6, "name": "sukhdeep-alarm", "status": 1, "time": "06:00"}
    assert expected == json.loads(res.get_data(as_text=True))

"""
Update non-exisitng alarm (alarm_id=14)
"""
def test_update_alarm_invalid_id(app, client):
    res = client.put('/alarm/14', json={
        "days": [3, 6], "alarm_id": 6, "name": "sukhdeep-alarm", "status": 1, "time": "06:00"
    })
    assert res.status_code == 404    
