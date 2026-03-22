### Problem 4: Vector Calculus

**Given:**
Position vector:
$$\vec{r}(t) = (3t^2)\hat{i} + (5t - 8t^2)\hat{j}$$

**Goal:** Find the velocity ($\vec{v}(t)$) and acceleration ($\vec{a}(t)$) vectors as a function of time.

**Step 1: Find the velocity vector ($\vec{v}(t)$)**
Velocity is the first derivative of the position vector with respect to time ($t$). To find it, we simply take the derivative of the $\hat{i}$ (x-axis) and $\hat{j}$ (y-axis) components separately.
$$\vec{v}(t) = \frac{d}{dt} \vec{r}(t)$$

- Derivative of the $\hat{i}$ component ($3t^2$): $6t$
- Derivative of the $\hat{j}$ component ($5t - 8t^2$): $5 - 16t$

Put them back together:
$$\vec{v}(t) = (6t)\hat{i} + (5 - 16t)\hat{j}$$

**Step 2: Find the acceleration vector ($\vec{a}(t)$)**
Acceleration is the rate of change of velocity, which means it is the first derivative of the velocity vector with respect to time.
$$\vec{a}(t) = \frac{d}{dt} \vec{v}(t)$$

- Derivative of the $\hat{i}$ component ($6t$): $6$
- Derivative of the $\hat{j}$ component ($5 - 16t$): $-16$

Put them back together:
$$\vec{a}(t) = 6\hat{i} - 16\hat{j}$$

---

**Final Answer:**

- **Velocity:** $\vec{v}(t) = (6t)\hat{i} + (5 - 16t)\hat{j}$
- **Acceleration:** $\vec{a}(t) = 6\hat{i} - 16\hat{j}$

Would you like to move on to the next problem?
