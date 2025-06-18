# Arduino Quiz

An interactive quiz system combining Arduino hardware with a Python-based question generator powered by AI. Users can select topics and answer questions using physical buttons, with LED feedback for correct/incorrect answers.

## Features

- Interactive hardware-software quiz system
- AI-powered question generation
- Multiple topic categories:
  - Embedded Circuits
  - Machine Learning
  - Physics
  - Artificial Intelligence
- Real-time LED feedback for answers
- User-friendly Streamlit interface

## Hardware Requirements

- Arduino board
- 4 push buttons (for answers A, B, C, D)
- 2 LEDs (Green for correct, Red for incorrect answers)
- Connecting wires
- Breadboard

## Hardware Setup

Connect the following components to your Arduino:
- Button A: Pin 7
- Button B: Pin 6
- Button C: Pin 4
- Button D: Pin 5
- Green LED: Pin 12
- Red LED: Pin 13

## Software Requirements

- Python 3.10.0
- virtualenv (for package management)
- Arduino IDE

## Installation

1. Clone the repository:
```bash 
git clone <https://github.com/JakubKucharski9/Arduino-Quiz.git> 
cd Arduino-Quiz
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate # On Windows use `venv\Scripts\activate`
```

3. Install required Python packages:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file with:
```bash
GEMINI_API=your_gemini_api_key
```

5. Upload the Arduino code (`arduino_main.cpp`) to your Arduino board using the Arduino IDE.

## Usage

1. Connect your Arduino board to your computer and note the COM port.

2. Run the Streamlit application:
```bash 
streamlit run app.py
```

3. In the web interface:
   - Enter the correct COM port for your Arduino
   - Select a question category using the buttons on your Arduino
   - Answer questions using the A, B, C, D buttons
   - Watch for LED feedback (Green for correct, Red for incorrect)

## How It Works

- The system uses Gemini AI model to generate quiz questions
- Questions are presented through a Streamlit web interface
- Users interact with physical buttons for topic selection and answering
- Arduino provides immediate feedback through LED indicators
- Serial communication handles data exchange between Arduino and Python
