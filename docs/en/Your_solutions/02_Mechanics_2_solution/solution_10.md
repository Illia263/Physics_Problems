### Problem 10: Force Field and Power

**Given:**
* Mass of the particle ($m$): $0.5 \text{ kg}$
* Position equations: 
  * $x(t) = 5t^2 - t$
  * $y(t) = 2t^3$
  * $z(t) = -3t + 2$

We can write the position as a vector: 
$$\vec{r}(t) = (5t^2 - t, 2t^3, -3t + 2)$$

**Goal:** Find time-dependent equations for velocity ($\vec{v}$), momentum ($\vec{p}$), acceleration ($\vec{a}$), force ($\vec{F}$), and power ($P$).

---

**Step 1: Find the particle's velocity ($\vec{v}$)**
Velocity is the first derivative of position with respect to time ($\vec{v} = \frac{d\vec{r}}{dt}$). We take the derivative of each component individually.
* $v_x = \frac{d}{dt}(5t^2 - t) = 10t - 1$
* $v_y = \frac{d}{dt}(2t^3) = 6t^2$
* $v_z = \frac{d}{dt}(-3t + 2) = -3$

$$\vec{v}(t) = (10t - 1, 6t^2, -3)$$

**Step 2: Find the particle's momentum ($\vec{p}$)**
Momentum is mass times velocity ($\vec{p} = m\vec{v}$).
$$\vec{p}(t) = 0.5 \cdot (10t - 1, 6t^2, -3)$$
Multiply each component by $0.5$:
$$\vec{p}(t) = (5t - 0.5, 3t^2, -1.5)$$

**Step 3: Find the particle's acceleration ($\vec{a}$)**
Acceleration is the derivative of velocity with respect to time ($\vec{a} = \frac{d\vec{v}}{dt}$).
* $a_x = \frac{d}{dt}(10t - 1) = 10$
* $a_y = \frac{d}{dt}(6t^2) = 12t$
* $a_z = \frac{d}{dt}(-3) = 0$

$$\vec{a}(t) = (10, 12t, 0)$$

**Step 4: Find the force acting on the particle ($\vec{F}$)**
Using Newton's Second Law ($\vec{F} = m\vec{a}$):
$$\vec{F}(t) = 0.5 \cdot (10, 12t, 0)$$
Multiply each component by $0.5$:
$$\vec{F}(t) = (5, 6t, 0)$$

**Step 5: Find the power transferred by the field ($P$)**
Power is the dot product of the force vector and the velocity vector ($P = \vec{F} \cdot \vec{v}$). 
To calculate the dot product, multiply the matching components and add them all together:
$$P(t) = (F_x \cdot v_x) + (F_y \cdot v_y) + (F_z \cdot v_z)$$
$$P(t) = (5)(10t - 1) + (6t)(6t^2) + (0)(-3)$$
$$P(t) = (50t - 5) + (36t^3) + 0$$

Rearranging into standard polynomial order:
$$P(t) = 36t^3 + 50t - 5$$

---

**Final Answer Summary:**
* **Velocity:** $\vec{v}(t) = (10t - 1, 6t^2, -3) \text{ m/s}$
* **Momentum:** $\vec{p}(t) = (5t - 0.5, 3t^2, -1.5) \text{ kg}\cdot\text{m/s}$
* **Acceleration:** $\vec{a}(t) = (10, 12t, 0) \text{ m/s}^2$
* **Force:** $\vec{F}(t) = (5, 6t, 0) \text{ N}$
* **Power:** $P(t) = 36t^3 + 50t - 5 \text{ W}$

Ready to tackle Problem 11?
