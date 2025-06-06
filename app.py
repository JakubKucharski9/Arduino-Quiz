import agent 
import serial
import requests
import time
from dotenv import load_dotenv
import os

load_dotenv()

agent = agent.Agent()
response = agent("Machine Learning")
question = response["question"]
answers = response["answers"]
correct_answer = response["correct_answer"]

SERIAL_PORT = "COM3"
BAUD_RATE = 9600

ser = serial.Serial(SERIAL_PORT, BAUD_RATE)

LAPTOP_URL = os.getenv("LAPTOP_URL")

# Button port mappings
BUTTON_PORTS = {
    "1": "GPIO17",
    "2": "GPIO27",
    "3": "GPIO22",
    "4": "GPIO23"
}

# Initialize inputs array with zeros
inputs = [0, 0, 0, 0]

def read_button_states():
    if ser.in_waiting:
        data = ser.readline().decode().strip()
        if data in BUTTON_PORTS:
            button_index = int(data) - 1  # Convert to 0-based index
            inputs[button_index] = 1  # Set the corresponding input to 1
            print(f"Button {data} pressed - Port: {BUTTON_PORTS[data]}")
            print(f"Current inputs: {inputs}")

def check_laptop_status():
    if not LAPTOP_URL:
        return
    
    try:
        response = requests.get(LAPTOP_URL, timeout=1)
        if response.status_code == 200:
            print("Laptop is online")
        else:
            print("Laptop is offline")
    except requests.exceptions.RequestException:
        pass  # Silently ignore connection errors

while True:
    try:
        # Check laptop status (if URL is configured)
        # check_laptop_status()

            
        # Read button states
        button_pressed = read_button_states()
        if button_pressed:
            print(f"Button pressed: {button_pressed}")
            print(f"Question: {question}")
            print(f"Answers: {answers}")
            print(f"Correct answer: {correct_answer}")
        
    except Exception as e:
        print(f"Error: {e}")
    time.sleep(0.1)  # Reduced sleep time for better button response

