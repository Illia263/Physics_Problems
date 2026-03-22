### Problem 5: Relative Velocity

**Given:**

- River velocity ($v_r$): $2 \text{ m/s}$ (East)
- Boat speed in still water ($v_b$): $5 \text{ m/s}$
- Desired path: Directly North
- River width ($d$): $200 \text{ m}$

**Goal:** Find the heading direction (angle $\theta$) and the time to cross ($t$).

**Step 1: Determine the heading angle**
To travel directly North, the boat must steer West of North to completely cancel out the river's Eastward current. This forms a right-angled triangle with the velocity vectors:

- Hypotenuse = $5 \text{ m/s}$ (boat's engine speed)
- Opposite side = $2 \text{ m/s}$ (river's speed to cancel)

$$\sin(\theta) = \frac{\text{Opposite}}{\text{Hypotenuse}}$$
$$\sin(\theta) = \frac{2}{5} = 0.4$$
$$\theta = \arcsin(0.4) \approx 23.58^\circ$$

**Step 2: Calculate the net velocity directly North ($v_{net}$)**
Use the Pythagorean theorem to find the adjacent side of the triangle, which represents the boat's actual progress straight across the river.
$$v_{net}^2 + v_r^2 = v_b^2$$
$$v_{net}^2 + 2^2 = 5^2$$
$$v_{net}^2 + 4 = 25$$
$$v_{net}^2 = 21$$
$$v_{net} = \sqrt{21} \approx 4.58 \text{ m/s}$$

**Step 3: Calculate the time to cross ($t$)**
Divide the total river width by the net northward velocity.
$$t = \frac{\text{Distance}}{v_{net}}$$
$$t = \frac{200}{\sqrt{21}}$$
$$t \approx 43.64 \text{ s}$$

**Final Answer:**

- **Direction:** $\approx 23.58^\circ$ West of North
- **Time to cross:** $\approx 43.64 \text{ s}$

Would you like to review any of the other problems you uploaded?
