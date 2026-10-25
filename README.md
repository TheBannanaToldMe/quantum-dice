#Quantum Dice

A dice-rolling web app that uses a simulated quantum circuit (Qiskit) to pick the number.

Live demo: https://quantum-dice-uqfeel88g6hwdrjpqkk82x.streamlit.app/

## How to run it on your computer

1. Install Python 3.10 or newer.
2. Download this repository and unzip it.
3. Open a Command Prompt/terminal, not powershell, inside the unzipped folder.

ex (to get to directory in Command Prompt:    cd C:\Users\YourName\Downloads\quantum-dice

4. Install the libraries (only needed once, takes a few minutes):

    python -m pip install -r requirements.txt

5. Start the app:

    python -m streamlit run quantum-dice.py

6. Your browser opens the app automatically. If it doesn't, go to http://localhost:8501

Troubleshooting:
- If "python" isn't recognized, try "py" (Windows) or "python3" (Mac/Linux) instead.
- If you get "No such file or directory", you're not in the project folder. Use "cd" to get to it first.

## Note
This runs on a simulator, not a real quantum computer.

## AI disclosure
I used Claude to explain certain concepts and help fix errors. I wrote the code myself minus the dice animation.
