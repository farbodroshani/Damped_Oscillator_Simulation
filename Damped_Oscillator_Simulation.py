import numpy as np
import matplotlib.pyplot as plt


# System parameters
m = float(input("Enter mass (kg): "))
k = float(input("Enter spring stiffness (N/m): "))
zeta = float(input("Enter damping ratio (dimensionless): "))  # Damping ratio
t_final = float(input("Enter simulation time (seconds): "))
dt = 0.01  # Time step for integration

# Calculate the damping coefficient
c = 2 * zeta * np.sqrt(k * m)

# Calculate the critical damping coefficient
c_critical = 2 * np.sqrt(m * k)

# Check if the system is underdamped, critically damped, or overdamped
if c < c_critical:
    print("The system is underdamped.")
elif c == c_critical:
    print("The system is critically damped.")
    print("the following code cannot calculate the displacement")
    quit()
else:
    print("The system is overdamped.")
    print("the following code cannot calculate the displacement")
    quit()

omega_n = np.sqrt(k / m)  # Natural frequency
omega_d = omega_n * np.sqrt(1 - zeta**2)  # Damped natural frequency

# External force function (e.g., sinusoidal force)

def external_force(t):
    return 10* t  # Modify this function as needed

# Initialize arrays for time, displacement, and velocity
time = np.arange(0, t_final, dt)
displacement = np.zeros_like(time)
velocity = np.zeros_like(time)

# Initial conditions
displacement[0] = 0.0
velocity[0] = 0.0

# Numerical integration using Duhamel integral
for i in range(1, len(time)):
    t = time[i]
    F = external_force(t)

    # Calculate the Duhamel integral
    integral_term = 0.0
    for j in range(i):
        tau = time[j]
        integrand = F * np.sin(omega_d * (t - tau)) * np.exp(-c * (t - tau) / (2 * m))
        integral_term += integrand * dt

    displacement[i] = (F / (m * omega_d**2)) * (1 - np.cos(omega_d * t)) + integral_term
    velocity[i] = (F / (m * omega_d)) * np.sin(omega_d * t) - (c / m) * integral_term

# Plot the displacement-time graph
plt.figure(figsize=(8, 6))
plt.plot(time, displacement, label="Displacement")
plt.xlabel("Time (s)")
plt.ylabel("Displacement (m)")
plt.title("Displacement-Time Graph using Duhamel Integral")
plt.grid(True)
plt.legend()
plt.show()

# Plot the velocity-time graph
plt.figure(figsize=(8, 6))
plt.plot(time, velocity, label="velocity")
plt.xlabel("Time (s)")
plt.ylabel("velocity (m/s)")
plt.title("velocity-Time Graph using Duhamel Integral")
plt.grid(True)
plt.legend()
plt.show()
