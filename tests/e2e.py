import requests
import json

def test_add_shipment():
    App_URL="http://127.0.0.1:8000/shipments/"
    f = open('request.json', 'r')
    request_json = json.loads(f.read())
    response = requests.post(App_URL,request_json)
    print(response.text)

def test_list_shipments():
    App_URL="http://127.0.0.1:8000/shipments/"
    response = requests.get(App_URL)
    print(response.text)

