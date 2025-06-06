import json
import serial
import time
import agent

com_port = "COM3"

ser = serial.Serial(com_port, 9600, timeout=1)
time.sleep(2)

agent = agent.Agent()

answer = agent("Embeeded circuits")
answer = json.loads(answer)
question = answer.get("question")
answers = answer.get("answers")
correct_answer = answer.get("correct_answer")
print(f"Question: {question}")
for idx, ans in enumerate(answers, start=1):
    print(f"{chr(64 + idx)}: {ans}")

while True:
    if ser.in_waiting > 0:
        user_answer = ser.readline().decode("utf-8").strip()
        print(f"User answer: {user_answer}")
        if user_answer == correct_answer:
            print("Correct!")
            ser.write(b"1")
        else:
            print("Incorrect!")
            ser.write(b"0")

        break



ser.close()