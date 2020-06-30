import requests

# api-endpoint 
URL = "localhost/last-sensor-data"
  
def get_data():  
    r = requests.get(url = URL) 
    status = r.status_code
    data = r.json()
    return status, data

def send_health(id_record, timestamp, health_state, user_id = 1):
    data = {
        "id_record" : id_record,
        "user_id" : user_id,
        "timestamp" : timestamp,
        "health_state" : health_state
    }
    response = requests.post(URL, json = data)
    return response
