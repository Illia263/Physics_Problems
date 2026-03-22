# Solutions goes here

### Problem 1: Projectile Motion

**Given:**

- Initial velocity: $v_0 = 100 \text{ m/s}$
- Angle: $\theta = 37^\circ$ _(Note: Standard approximation uses $\sin(37^\circ) \approx 0.6$ and $\cos(37^\circ) \approx 0.8$)_
- Acceleration due to gravity: $g \approx 9.8 \text{ m/s}^2$

**Step 1: Calculate Initial Velocity Components**
$$v_{0x} = v_0 \cos(37^\circ) = 100 \cdot 0.8 = 80 \text{ m/s}$$
$$v_{0y} = v_0 \sin(37^\circ) = 100 \cdot 0.6 = 60 \text{ m/s}$$

**Step 2: Derive differential equations of motion**
With no air resistance, gravity is the only force acting on the projectile.

- **Horizontal:** No acceleration.
  $$\frac{d^2x}{dt^2} = 0$$
- **Vertical:** Acceleration is downward due to gravity.
  $$\frac{d^2y}{dt^2} = -g$$

**Step 3: Determine the time of flight ($t$)**
The time of flight is when the vertical position $y$ returns to $0$.
$$y(t) = v_{0y}t - \frac{1}{2}gt^2 = 0$$
$$t = \frac{2v_{0y}}{g}$$
$$t = \frac{2 \cdot 60}{9.8}$$
$$t \approx 12.24 \text{ s}$$

**Step 4: Determine the maximum height ($H$)**
Maximum height is reached when vertical velocity $v_y = 0$.
$$H = \frac{v_{0y}^2}{2g}$$
$$H = \frac{60^2}{2 \cdot 9.8}$$
$$H = \frac{3600}{19.6}$$
$$H \approx 183.67 \text{ m}$$

**Step 5: Determine the range ($R$)**
Range is the total horizontal distance covered during the time of flight.
$$R = v_{0x} \cdot t$$
$$R = 80 \cdot 12.24$$
$$R \approx 979.2 \text{ m}$$ _(using exact fraction $\frac{120}{9.8}$ yields $\approx 979.59 \text{ m}$)_

---

**Final Answer:**

- **Differential Equations:** $\frac{d^2x}{dt^2} = 0$ and $\frac{d^2y}{dt^2} = -g$
- **Time of flight:** $\approx 12.24 \text{ s}$
- **Maximum height:** $\approx 183.67 \text{ m}$
- **Range:** $\approx 979.59 \text{ m}$

Would you like to move to the next mechanics problem?

...
