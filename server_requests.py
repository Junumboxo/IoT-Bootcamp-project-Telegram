import requests

# api-endpoint 
URL = "localhost/last-sensors-data-aggregated"
  
def get_data():  
    r = requests.get(url = URL) 
    status = r.status_code
    data = r.json()
    return status, data

def send_health_status(health_status):
    data = {
        "health_status" : health_status
    }
    r = requests.post(URL, json = data)
    status = r.status_code
    return status