#importing requests which is used to send HTTPs rqsts and handle responses
import requests
import time
from datetime import datetime

SERVER_URL = 'http://server:5000'

#used to check if the server is up and running
def health_check():
    response = requests.get(f"{SERVER_URL}/health")
    print(f"Health Check: {response.text}")
#used to check the server’s responsiveness and to verify that it’s correctly handling the ping request
def ping():
    response = requests.post(f"{SERVER_URL}/ping", json={"type": "ping"})
    print("I am running")
    print(f"Ping Response: {response.json()}")
#to verify that the server is processing the data correctly.
def send_data():
    response = requests.post(f"{SERVER_URL}/data", json={"jsonrpc": "2.0", "method": "message-1"})
    print(f"Data Response: {response.json()}")

#runs the code inside if when the the script execute
if __name__ == '__main__':
    while True:
        health_check()
        ping()
        send_data()
        time.sleep(5) 
