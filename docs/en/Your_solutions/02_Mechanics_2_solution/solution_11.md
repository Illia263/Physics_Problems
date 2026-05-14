### Problem 11: Dynamics with a time-dependent force

**Given:**
* Mass ($m$): 3 kg
* Force vector ($\vec{F}$): $(15t, 3t-12, -6t^2)$ N
* Initial position ($\vec{r}_0$): $(5, 2, -3)$ m
* Initial velocity ($\vec{v}_0$): $(2, 0, 1)$ m/s

**Goal:** Find the time-dependent equations for the particle's velocity ($\vec{v}(t)$) and position ($\vec{r}(t)$).

---

**Step 1: Find the acceleration vector ($\vec{a}(t)$)**
Using Newton's Second Law ($\vec{F} = m\vec{a}$), we can find acceleration by dividing the force vector by the mass.
$$\vec{a}(t) = \frac{\vec{F}(t)}{m}$$
$$\vec{a}(t) = \frac{1}{3} (15t, 3t-12, -6t^2)$$
$$\vec{a}(t) = (5t, t-4, -2t^2)$$

**Step 2: Find the velocity vector ($\vec{v}(t)$)**
Velocity is the integral of acceleration with respect to time ($\vec{v} = \int \vec{a} \, dt$). We integrate each component individually and add a constant of integration vector ($\vec{C}_v$).
* $v_x(t) = \int 5t \, dt = \frac{5}{2}t^2 + C_{vx}$
* $v_y(t) = \int (t - 4) \, dt = \frac{1}{2}t^2 - 4t + C_{vy}$
* $v_z(t) = \int -2t^2 \, dt = -\frac{2}{3}t^3 + C_{vz}$

To find the constants, use the initial velocity condition $\vec{v}(0) = (2, 0, 1)$. Plugging in $t = 0$:
* $v_x(0) = C_{vx} = 2$
* $v_y(0) = C_{vy} = 0$
* $v_z(0) = C_{vz} = 1$

Substitute the constants back into the equations:
$$\vec{v}(t) = \left( \frac{5}{2}t^2 + 2, \, \frac{1}{2}t^2 - 4t, \, -\frac{2}{3}t^3 + 1 \right)$$

**Step 3: Find the position vector ($\vec{r}(t)$)**
Position is the integral of velocity with respect to time ($\vec{r} = \int \vec{v} \, dt$). Again, integrate each component and add a constant of integration vector ($\vec{C}_r$).
* $x(t) = \int \left(\frac{5}{2}t^2 + 2\right) dt = \frac{5}{6}t^3 + 2t + C_{rx}$
* $y(t) = \int \left(\frac{1}{2}t^2 - 4t\right) dt = \frac{1}{6}t^3 - 2t^2 + C_{ry}$
* $z(t) = \int \left(-\frac{2}{3}t^3 + 1\right) dt = -\frac{2}{12}t^4 + t + C_{rz} = -\frac{1}{6}t^4 + t + C_{rz}$

To find the constants, use the initial position condition $\vec{r}(0) = (5, 2, -3)$. Plugging in $t = 0$:
* $x(0) = C_{rx} = 5$
* $y(0) = C_{ry} = 2$
* $z(0) = C_{rz} = -3$

Substitute the constants back into the equations:
$$\vec{r}(t) = \left( \frac{5}{6}t^3 + 2t + 5, \, \frac{1}{6}t^3 - 2t^2 + 2, \, -\frac{1}{6}t^4 + t - 3 \right)$$

---

**Final Answer:**
* **Velocity dependence:** $\vec{v}(t) = \left( \frac{5}{2}t^2 + 2, \, \frac{1}{2}t^2 - 4t, \, -\frac{2}{3}t^3 + 1 \right) \text{ m/s}$
* **Position dependence:** $\vec{r}(t) = \left( \frac{5}{6}t^3 + 2t + 5, \, \frac{1}{6}t^3 - 2t^2 + 2, \, -\frac{1}{6}t^4 + t - 3 \right) \text{ m}$
