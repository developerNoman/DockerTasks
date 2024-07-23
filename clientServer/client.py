import requests
import time
from datetime import datetime

SERVER_URL = 'http://server:5000'


def health_check():
    response = requests.get(f"{SERVER_URL}/health")
    print(f"Health Check: {response.text}")

def ping():
    response = requests.post(f"{SERVER_URL}/ping", json={"type": "ping"})
    print("I am running")
    print(f"Ping Response: {response.json()}")

def send_data():
    response = requests.post(f"{SERVER_URL}/data", json={"jsonrpc": "2.0", "method": "message-1"})
    print(f"Data Response: {response.json()}")

if __name__ == '__main__':
    while True:
        health_check()
        ping()
        send_data()
        time.sleep(5) 
