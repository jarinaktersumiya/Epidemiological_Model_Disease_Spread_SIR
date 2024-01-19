# Importing Libraries
# I'm using numpy for calculations, scipy for solving the differential equations, 
# and matplotlib for plotting the model's results.

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Defining the SIR Model
# This function represents how the disease spreads and recovers in a population.
# It's crucial for understanding the dynamics of the disease in Bucharest.
def sir_model(y, t, N, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

# Setting Initial Conditions for Bucharest
# I'm considering a more realistic outbreak scenario with 1,000 initially infected people.
# The transmission and recovery rates are estimates based on typical values for infectious diseases.


N = 1800000  # Bucharest's population
I0, R0 = 1000, 0  # 1,000 initially infected, none recovered
S0 = N - I0 - R0  # Rest of the population is susceptible
beta, gamma = 0.3, 1./10  # Estimated transmission and recovery rates

# Solving the SIR Model Equations
# I'm using a time frame of 160 days to observe the disease progression.

t = np.linspace(0, 160, 160)  # Time grid for the simulation (in days)
y0 = S0, I0, R0  # Initial state of the population
ret = odeint(sir_model, y0, t, args=(N, beta, gamma))
S, I, R = ret.T

# Plotting the Results
# The plot shows how the disease could potentially spread and eventually be controlled in Bucharest.

plt.figure(figsize=(10,6))
plt.plot(t, S, 'b', alpha=0.7, linewidth=2, label='Susceptible')
plt.plot(t, I, 'y', alpha=0.7, linewidth=2, label='Infected')
plt.plot(t, R, 'g', alpha=0.7, linewidth=2, label='Recovered')
plt.xlabel('Time (days)')
plt.ylabel('Number of people')
plt.legend()
plt.title('SIR Model Simulation for Bucharest')
plt.show()
