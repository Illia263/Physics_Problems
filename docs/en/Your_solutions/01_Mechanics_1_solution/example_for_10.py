import numpy as np
import matplotlib.pyplot as plt

# Define the constants
a = 5.0      # x-axis amplitude
b = 2.0      # y-axis amplitude (make a=b for the special case circular helix)
omega = 2.0  # angular frequency
b_z = 1.0    # z-axis velocity multiplier
t0 = 10.0    # end time

# Generate time values
t = np.linspace(0, t0, 1000)

# Parametric equations
x = a * np.cos(omega * t)
y = b * np.sin(omega * t)
z = b_z * t

# Create the 3D plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot the trajectory
ax.plot(x, y, z, label='Trajectory: Elliptical Helix', color='b')

# Labels and title
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis (time)')
ax.set_title('Kinematics: 3D Trajectory of Point M')
ax.legend()

plt.show()