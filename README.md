# Damped_Oscillator_Simulation
This repository contains a Python script that uses the Duhamel integral to calculate the displacement and velocity of a damped harmonic oscillator subjected to an external force. The script allows the user to input system parameters and then computes the response of the system over a specified simulation time.
# Overview

The provided Python script analyzes the response of a damped harmonic oscillator by:

Calculating the displacement over time.

Calculating the velocity over time.

# User Guide
1. Initialization and Input Data
Import the necessary libraries: numpy for numerical computations and matplotlib.pyplot for plotting graphs.

2. System Parameters
Input the System Parameters: The script will prompt the user to input the following parameters:

Mass (kg)

Spring stiffness (N/m)

Damping ratio (dimensionless)

Simulation time (seconds)

3. Calculate Damping Coefficients
The script calculates the damping coefficient and critical damping coefficient based on the provided system parameters.

It then checks if the system is underdamped, critically damped, or overdamped. If the system is critically damped or overdamped, the script will exit as it cannot calculate the displacement for these cases.

4. Define External Force Function
The script uses an external force function to define the input force. Users can modify this function as needed to simulate different types of external forces.

5. Initialize Arrays for Time, Displacement, and Velocity
The script initializes arrays to store the time, displacement, and velocity values over the simulation period.

6. Numerical Integration Using Duhamel Integral
The script uses numerical integration to calculate the displacement and velocity of the system at each time step using the Duhamel integral.

7. Plot Results
The script plots the displacement-time graph and the velocity-time graph using matplotlib.pyplot.

# Output
Displacement-Time Graph: A plot showing the displacement of the system over time.

Velocity-Time Graph: A plot showing the velocity of the system over time.

# Example Usage
To run the script, execute it in a Python environment and follow the prompts to input the system parameters. The script will then display the displacement-time and velocity-time graphs based on the inputs provided.
