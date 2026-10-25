from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import math
import streamlit as st
import time
import random
import matplotlib.pyplot as plt

global sides

qComputerSim = AerSimulator()

def nBits():
    return math.floor(math.log2(sides) + 1)

def makeCircuit():

    #creates quantum circuit of 3 qubits
    global qCircuit
    qCircuit = QuantumCircuit(nBits())

    #Hadamard gate puts qubits into superposition and then sets up measurments
    qCircuit.h(range(nBits()))
    qCircuit.measure_all()

def quantumRoll():

    makeCircuit()

    #runs simulation of quantum circuit and stores results in qresult
    qresult = qComputerSim.run(qCircuit, shots = 1).result().get_counts()

    #pulls value from quantum simulation and coverts it from binary to decimal
    result = next(iter(qresult))
    side = int(result, 2)

    #Prevents values over the number of die faces
    if side > sides - 1:
        return quantumRoll()
    else:
        return side + 1

@st.fragment
def roll_section():
    clicked = st.button("Roll!", type="primary", key="roll_button")
    spot = st.empty()

    if clicked:
        final = quantumRoll()

        delay = 0.04
        for _ in range(14):
            fake = random.randint(1, sides)
            spot.markdown(f"<div class='die'>{fake}</div>", unsafe_allow_html=True)
            time.sleep(delay)
            delay += 0.012

        st.session_state.last_roll = final

    if "last_roll" in st.session_state:
        spot.markdown(f"<div class='die'>{st.session_state.last_roll}</div>", unsafe_allow_html=True)
        st.write(f"You rolled a **{st.session_state.last_roll}!**")

#Webpage setup
st.set_page_config(page_title="Quantum Dice", page_icon="🎲")

#extra config(s)
st.markdown("""
<style>
.die {
    display: block;
    width: 140px;
    margin: 20px auto;
    padding: 20px 0;
    text-align: center;
    font-size: 72px;
    border: 3px solid #00D1B2;
    border-radius: 20px;
    color: #00D1B2;
}
</style>
""", unsafe_allow_html=True)

#building webpage
st.title("Quantum Dice")
st.divider()
st.html("<div style='margin-top: 10px;'></div>")

st.write("This is functioning dice using a simulated quantum " \
"circuit! It functions by putting together a quantim " \
"computing circuit and then running it through a " \
"simulated quantum computer. That library is supplied by " \
"Qiskit—an open source toolkit from IBM.")

st.html("<div style='margin-top: 10px;'></div>")
with st.container(border=True):
    st.image("example_quantum_circuit.png", caption="Example quantum circuit", use_container_width=True)
st.html("<div style='margin-top: 10px;'></div>")

st.write("Why do we even bother with qubits ($q_n$)?, " \
"The biggest advantage of " \
"quantum computers comes in the form of $superposition$. " \
"Bascially, unlke bits in a classical computer quantum bits "
"(qubits) can exist in a state which is between 0 and 1. " \
"That can be used to generate a $quantum$ $advantage$ which "
"is the measured efficiancy/accuracy a quantum algorithm has " \
"over a classical one. In this little demo, we are simply using " \
"that superposition to give a peak into one specific benefit of " \
"quantum computers: true randomness. Classical computers can " \
"never be truly random, so any sort of randomness you have seen "
"is just complex math that can be hard for humans to predict. " \
"One of the benefits of quantum computers, that could even counter " \
"their own adept decryption abilities, is that the true randomness " \
"of a real quantum computer could generate keys that can't be " \
"predicted which could enhance cybersecurity as well as simply "
"make things that are intended to be random truly random. " \
"This demo will be trying to demonstrate that true " \
"randomness by rolling a die in a simulated quantum computer." \
"But to be clear, this demo isn't truly random either because it " \
"is a simulation of a quantom computer running on a classical computer. " \
"To see that true randomness this quantum circuit would have to be run " \
"on a real quantum computer such as IBM's.")

st.html("<div style='margin-top: 10px;'></div>")
st.header("Circuit rundown")
st.divider()

st.markdown("""
- **quibits**- At the beginning of the diagram you can see a 
number of qubits which begin our circuit. Be default there 
are three, but you will have a chance to add more yorself 
soon! When they are first created they are in their $ground$ 
$state$ which is simply 0. They are not in superposition, 
so they're basically like a classical bit switched off.

- **Hadamard** **Gate**- The H symbols you see are 
$Hadamard$ $Gates$. These are a fundemntal quantum 
gate which puts the qubits into a superposition of 
equal parts 1 and 0. When we later measure the qubits 
they will $collapse$ into a single one of those states 
(50% chance for 1, 50% chance for 0). This would give us 
true randomness if this were ran on a real quantum computer.

- **Barrier**- That dotted line simply tells the compiler to 
not reorder the gates along the circuit which keeps things 
nice and simple for us.

- **Measurment Operation**- Those gauge symbols are where our 
qubits get measured, its at this point that they collapse into 
a singlular state (1 or 0). All of the results are the ordered 
nto a bitstring that we will convert into a normal integer 
telling us what face of the dice came up!
""")

st.divider()
st.header("Time to roll your own dice!")
st.divider()

st.write("Now you can pick how many sides you want, roll your die, and look at how the circuit changes!")

sides = st.selectbox("Choose your die", [4, 6, 8, 10, 12, 20], index=1, format_func=lambda n: f"d{n}")

roll_section()

with st.expander(f"See the circuit for your d{sides}"):
    makeCircuit()                                   
    fig = qCircuit.draw("mpl", style="iqp-dark")    
    st.pyplot(fig)
    plt.close(fig)                                  
    st.caption(f"{nBits()} qubits: enough to represent {sides} outcomes")

st.divider()
st.html("<div style='margin-top: 10px;'></div>")

st.write("Now you've had the opportunity to roll your own " \
"quantum die! You've also taken peak inside a simple quantum " \
"circuit. Hopefull you've learned a lot, and I hope you've been " \
"inspired to investigate quantum computers on your own time. " \
"Feel free to stay around and roll some more dice—but if not, bye!")
