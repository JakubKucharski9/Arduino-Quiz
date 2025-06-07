import json
import pandas as pd
import serial
import time
import agent
import streamlit as st

agent = agent.Agent()

fields_of_questions = ["Embed Circuits", "Machine Learning", "Physics", "Artificial Intelligence"]
question = fields_of_questions[0]

st.title("Interactive Question-Answer System")

try:
    com_port = st.text_input("Enter COM Port of Arduino board:", help="Enter your COM port, for example: COM3")
    if com_port and not com_port.startswith("COM"): raise AssertionError

    if com_port:
        st.write("Choose a field of question:")
        fields_df = pd.DataFrame(fields_of_questions, columns=["Field of Question"])
        selected_field = st.table(fields_df)

        if st.button("Start"):
            try:
                ser = serial.Serial(com_port, 9600, timeout=1)
                time.sleep(2)

                stage = 0

                try:
                    while True:
                        if stage == 0:
                            if ser.in_waiting > 0:
                                user_answer = ser.readline().decode("utf-8").strip()
                                if user_answer == "QA":
                                    question = fields_of_questions[0]
                                elif user_answer == "QB":
                                    question = fields_of_questions[1]
                                elif user_answer == "QC":
                                    question = fields_of_questions[2]
                                elif user_answer == "QD":
                                    question = fields_of_questions[3]

                                stage = 1

                        if stage == 1:
                            answer = agent(question)
                            answer = json.loads(answer)
                            question = answer.get("question")
                            answers = answer.get("answers")
                            correct_answer = answer.get("correct_answer")
                            st.write(f"Question: {question}")
                            for idx, ans in enumerate(answers, start=1):
                                st.write(f"{chr(64 + idx)}: {ans}")
                            if ser.in_waiting > 0:
                                user_answer = ser.readline().decode("utf-8").strip()
                                st.write(f"User answer: {user_answer}")
                                if user_answer == correct_answer:
                                    st.write("Correct!")
                                    ser.write(b"1")
                                else:
                                    st.write("Incorrect!")
                                    ser.write(b"0")

                                stage = 0
                except KeyboardInterrupt:
                    st.write("\nEnd of the program – closing port")
                finally:
                    ser.close()
            except serial.serialutil.SerialException:
                st.error(f"Failed to open {com_port} port")
except AssertionError:
    st.error("Invalid COM port")


