### Problem 9: Vertical Throw with Drag

**Given:**
* Equation of motion: $$m\frac{dv}{dt} = -mg - kv$$
* Initial conditions: $v(0) = v_0$ and $x(0) = 10$

---

#### Part 1: Solve the equation analytically
We need to find the velocity $v(t)$ and position $x(t)$ as functions of time. 

**Step 1: Find Velocity $v(t)$**
First, isolate $\frac{dv}{dt}$ by dividing by mass $m$:
$$\frac{dv}{dt} = -g - \frac{k}{m}v$$

Factor out $-\frac{k}{m}$ to prepare for separation of variables:
$$\frac{dv}{dt} = -\frac{k}{m} \left( v + \frac{mg}{k} \right)$$

Separate the variables ($v$ on one side, $t$ on the other) and integrate:
$$\int \frac{dv}{v + \frac{mg}{k}} = \int -\frac{k}{m} dt$$
$$\ln\left| v + \frac{mg}{k} \right| = -\frac{k}{m}t + C_1$$

To find the constant $C_1$, use the initial condition $v(0) = v_0$:
$$C_1 = \ln\left| v_0 + \frac{mg}{k} \right|$$

Substitute $C_1$ back in, exponentiate both sides, and solve for $v(t)$:
$$v(t) + \frac{mg}{k} = \left(v_0 + \frac{mg}{k}\right)e^{-\frac{k}{m}t}$$
$$v(t) = \left(v_0 + \frac{mg}{k}\right)e^{-\frac{k}{m}t} - \frac{mg}{k}$$

**Step 2: Find Position $x(t)$**
Position is the integral of velocity: $x(t) = \int v(t) dt$.
$$x(t) = \int \left[ \left(v_0 + \frac{mg}{k}\right)e^{-\frac{k}{m}t} - \frac{mg}{k} \right] dt$$
$$x(t) = -\frac{m}{k}\left(v_0 + \frac{mg}{k}\right)e^{-\frac{k}{m}t} - \frac{mg}{k}t + C_2$$

Use the initial condition $x(0) = 10$ to find $C_2$:
$$10 = -\frac{m}{k}\left(v_0 + \frac{mg}{k}\right)e^0 - 0 + C_2$$
$$C_2 = 10 + \frac{m}{k}\left(v_0 + \frac{mg}{k}\right)$$

Substitute $C_2$ back in and factor to clean it up:
$$x(t) = 10 + \frac{m}{k}\left(v_0 + \frac{mg}{k}\right)\left(1 - e^{-\frac{k}{m}t}\right) - \frac{mg}{k}t$$

---

#### Part 2: Determine the maximum height
Maximum height occurs when the object stops moving upward, meaning velocity $v(t) = 0$.

**Step 1: Find the time to reach max height ($t_{max}$)**
$$0 = \left(v_0 + \frac{mg}{k}\right)e^{-\frac{k}{m}t_{max}} - \frac{mg}{k}$$
$$e^{-\frac{k}{m}t_{max}} = \frac{\frac{mg}{k}}{v_0 + \frac{mg}{k}} = \frac{mg}{kv_0 + mg}$$
Take the natural log of both sides:
$$-\frac{k}{m}t_{max} = \ln\left(\frac{mg}{kv_0 + mg}\right)$$
$$t_{max} = \frac{m}{k}\ln\left(1 + \frac{kv_0}{mg}\right)$$

**Step 2: Plug $t_{max}$ into the $x(t)$ equation**
Substituting this specific time back into our position equation and simplifying yields the maximum height:
$$x_{max} = 10 + \frac{mv_0}{k} - \frac{m^2g}{k^2}\ln\left(1 + \frac{kv_0}{mg}\right)$$

---

#### Part 3: Compare with the case without drag
If there were no air resistance ($k = 0$), the maximum height formula comes from standard kinematics ($v_f^2 = v_i^2 - 2g\Delta x$):
$$x_{max, \text{no drag}} = 10 + \frac{v_0^2}{2g}$$

**Comparison:** The maximum height *with* drag is strictly **lower** than the height *without* drag. This is because the drag force constantly does negative work on the particle as it moves upward, dissipating kinetic energy into the surrounding air as heat, rather than allowing all of it to convert into gravitational potential energy.

---

#### Part 4: Numerical simulation using Python
Here is a Python script using `numpy` and `matplotlib` to plot the trajectory, giving a clear visual of how drag affects the throw.

```python
import numpy as np
import matplotlib.pyplot as plt

# Define parameters (you can change these to test different scenarios)
m = 1.0     # Mass (kg)
g = 9.81    # Gravity (m/s^2)
k = 0.5     # Drag coefficient (kg/s)
v0 = 20.0   # Initial upward velocity (m/s)
x0 = 10.0   # Initial height (m)

# Time array (from 0 to 3.5 seconds)
t = np.linspace(0, 3.5, 500)

# Analytical position formula (with drag)
x_drag = x0 + (m/k)*(v0 + (m*g)/k)*(1 - np.exp(-(k/m)*t)) - ((m*g)/k)*t

# Analytical position formula (without drag for comparison)
x_nodrag = x0 + v0*t - 0.5*g*t**2

# Plotting the simulation
plt.figure(figsize=(8, 5))
plt.plot(t, x_drag, label='With Air Resistance (Drag)', color='red', linewidth=2)
plt.plot(t, x_nodrag, label='No Air Resistance', color='blue', linestyle='--')

# Adding labels and styling
plt.title('Numerical Simulation: Vertical Throw')
plt.xlabel('Time (seconds)')
plt.ylabel('Height (meters)')
plt.axhline(0, color='black', linewidth=1) # Ground level
plt.ylim(0, max(x_nodrag) + 5)
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend()

plt.show()
```

Let me know if you're ready to tackle Problem 10!
