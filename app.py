import json
import serial
import time
import agent

com_port = "COM3"

ser = serial.Serial(com_port, 9600, timeout=1)
time.sleep(2)
stage = 0

agent = agent.Agent()

fields_of_questions = ["Embed Circuits", "Machine Learning", "Physics", "Artificial Intelligence"]
question = fields_of_questions[0] # Default

try:
    while True:
        if stage == 0:
            print(fields_of_questions)
            for idx, ans in enumerate(fields_of_questions, start=1):
                print(f"{chr(64 + idx)}: {ans}")
            if ser.in_waiting > 0:
                while True:
                    user_answer = ser.readline().decode("utf-8").strip()
                    if user_answer == "QA":
                        question = fields_of_questions[0]
                    if user_answer == "QB":
                        question = fields_of_questions[1]
                    if user_answer == "QC":
                        question = fields_of_questions[2]
                    if user_answer == "QD":
                        question = fields_of_questions[3]
                    break

                stage = 1


        if stage == 1:
            answer = agent(question)
            answer = json.loads(answer)
            question = answer.get("question")
            answers = answer.get("answers")
            correct_answer = answer.get("correct_answer")
            print(f"Question: {question}")
            for idx, ans in enumerate(answers, start=1):
                print(f"{chr(64 + idx)}: {ans}")
            if ser.in_waiting > 0:
                while True:
                    user_answer = ser.readline().decode("utf-8").strip()
                    print(f"User answer: {user_answer}")
                    if user_answer == correct_answer:
                        print("Correct!")
                        ser.write(b"1")
                    else:
                        print("Incorrect!")
                        ser.write(b"0")
                    break

                stage = 0
except KeyboardInterrupt:
    print("\nKoniec programu – zamykam port")
finally:
    ser.close()
