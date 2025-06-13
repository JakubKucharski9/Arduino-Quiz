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

                qa_fetched = False  # flaga ograniczająca zapytanie do agenta
                answer = None  # cache odpowiedzi

                try:
                    while True:
                        if stage == 0:
                            qa_fetched = False  # reset przy każdej nowej odpowiedzi z Arduino
                            if ser.in_waiting > 0:
                                user_answer = ser.readline().decode("utf-8").strip()
                                mapping = {
                                    "QA": "Embed Circuits",
                                    "QB": "Machine Learning",
                                    "QC": "Physics",
                                    "QD": "Artificial Intelligence"
                                }
                                if user_answer in mapping:
                                    question = mapping[user_answer]
                                    stage = 1

                        if stage == 1:
                            if not qa_fetched:
                                answer = agent(question)
                                try:
                                    answer = json.loads(str(answer))
                                except json.JSONDecodeError:
                                    answer = answer
                                qa_fetched = True

                                question_text = answer.get("question")
                                answers = answer.get("answers")
                                correct_answer = answer.get("correct_answer")

                                st.write(f"Question: {question_text}")
                                for idx, ans in enumerate(answers, start=1):
                                    st.write(f"{chr(64 + idx)}: {ans}")
                                user_answer = b''
                                while user_answer == b'':
                                    user_answer = ser.readline().decode("utf-8").strip()
                                    if user_answer != b'':
                                        break
                                user_answer = str(user_answer)[2]

                                mapping_answers = {
                                    "A": answers[0],
                                    "B": answers[1],
                                    "C": answers[2],
                                    "D": answers[3]
                                }

                                user_answer_normalised = mapping_answers[user_answer]

                                if user_answer_normalised:
                                    st.write(f"User answer: {user_answer_normalised}")
                                    if user_answer_normalised == correct_answer:
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


