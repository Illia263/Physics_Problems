### Problem 12: Work and energy with a constant force

**Given:**
* Mass ($m$): $2\ \mathrm{kg}$
* Constant force ($\vec{F}$): $[6, 2]\ \mathrm{N}$
* Initial velocity ($\vec{v}(0)$): $(1, -1)\ \mathrm{m/s}$
* Initial position ($\vec{r}(0)$): $(0, 0)\ \mathrm{m}$

---

**Step 1: Determine $\vec{a}(t)$**
Using Newton's Second Law ($\vec{F} = m\vec{a}$), we find acceleration by dividing the force vector by the mass. Since the force is constant, the acceleration will also be constant.
$$\vec{a}(t) = \frac{\vec{F}}{m}$$
$$\vec{a}(t) = \frac{1}{2}[6, 2]$$
$$\vec{a}(t) = (3, 1)\ \mathrm{m/s^2}$$

**Step 2: Determine $\vec{v}(t)$**
Velocity is the integral of acceleration with respect to time.
$$\vec{v}(t) = \int \vec{a} \, dt = \left( \int 3 \, dt, \int 1 \, dt \right)$$
$$\vec{v}(t) = (3t + C_{vx}, t + C_{vy})$$
Use the initial condition $\vec{v}(0) = (1, -1)$ to find the constants:
* $v_x(0) = C_{vx} = 1$
* $v_y(0) = C_{vy} = -1$

$$\vec{v}(t) = (3t + 1, t - 1)\ \mathrm{m/s}$$

**Step 3: Determine $\vec{r}(t)$**
Position is the integral of velocity with respect to time.
$$\vec{r}(t) = \int \vec{v}(t) \, dt = \left( \int (3t + 1) dt, \int (t - 1) dt \right)$$
$$\vec{r}(t) = \left( \frac{3}{2}t^2 + t + C_{rx}, \frac{1}{2}t^2 - t + C_{ry} \right)$$
Use the initial condition $\vec{r}(0) = (0, 0)$ to find the constants. Both are $0$:
$$\vec{r}(t) = (1.5t^2 + t, 0.5t^2 - t)\ \mathrm{m}$$

**Step 4: Draw the trajectory of the motion**
Because both $x(t)$ and $y(t)$ are quadratic equations in $t$, the path traced by the particle is a parabola. Here is a short Python script using `matplotlib` to draw the exact trajectory from $t=0$ to $t=3$:

```python
import numpy as np
import matplotlib.pyplot as plt

# Time vector from 0 to 3 seconds
t = np.linspace(0, 3, 100)

# Parametric equations for position
x = 1.5 * t**2 + t
y = 0.5 * t**2 - t

# Plotting the trajectory
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='Trajectory', color='purple', linewidth=2)
plt.scatter([x[0]], [y[0]], color='green', zorder=5, label='Start (t=0)')
plt.scatter([x[-1]], [y[-1]], color='red', zorder=5, label='End (t=3)')

plt.title('Trajectory of the Particle (t=0 to 3s)')
plt.xlabel('x position (m)')
plt.ylabel('y position (m)')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle='--')
plt.legend()
plt.show()
```

**Step 5: Calculate the work done by the force at time $t=3\ \mathrm{s}$**
For a constant force, work is the dot product of the force vector and the displacement vector ($\Delta \vec{r}$).
First, find the position at $t=3$:
* $x(3) = 1.5(3)^2 + 3 = 13.5 + 3 = 16.5\ \mathrm{m}$
* $y(3) = 0.5(3)^2 - 3 = 4.5 - 3 = 1.5\ \mathrm{m}$
$$\vec{r}(3) = (16.5, 1.5)$$
Since the start was at $(0,0)$, the displacement $\Delta \vec{r}$ is $(16.5, 1.5)$.
$$W = \vec{F} \cdot \Delta \vec{r}$$
$$W = (6)(16.5) + (2)(1.5)$$
$$W = 99 + 3$$
$$W = 102\ \mathrm{J}$$

**Step 6: Check the consistency with the work-energy theorem**
The work-energy theorem states that the work done on an object equals its change in kinetic energy: $W = \Delta K = K_f - K_i$.
* **Initial Kinetic Energy ($K_i$):**
  At $t=0$, $\vec{v}(0) = (1, -1)$. The speed squared is $|\vec{v}|^2 = 1^2 + (-1)^2 = 2$.
  $$K_i = \frac{1}{2}mv_i^2 = \frac{1}{2}(2)(2) = 2\ \mathrm{J}$$
* **Final Kinetic Energy ($K_f$) at $t=3$:**
  Calculate velocity at $t=3$: $\vec{v}(3) = (3(3) + 1, 3 - 1) = (10, 2)$.
  The speed squared is $|\vec{v}|^2 = 10^2 + 2^2 = 100 + 4 = 104$.
  $$K_f = \frac{1}{2}mv_f^2 = \frac{1}{2}(2)(104) = 104\ \mathrm{J}$$
* **Change in Kinetic Energy ($\Delta K$):**
  $$\Delta K = 104\ \mathrm{J} - 2\ \mathrm{J} = 102\ \mathrm{J}$$

**Conclusion:** The work done ($102\ \mathrm{J}$) exactly matches the change in kinetic energy ($102\ \mathrm{J}$). The calculations are perfectly consistent with the work-energy theorem.

---
That concludes the list of problems you shared in the markdown code! Let me know if you have any questions on these or if you have another assignment ready to go.
