### Problem 3: Superposition Principle

**Given:**
* Wave 1: $y_1(x, t) = A \sin(kx - \omega t)$
* Wave 2: $y_2(x, t) = A \sin(kx + \omega t)$

**Goal:** Find the equation of the resulting standing wave and identify the positions of the nodes.

**Step 1: Apply the Superposition Principle**
The principle of superposition states that the resultant wave $y(x,t)$ is the algebraic sum of the individual waves.
$$y(x,t) = y_1(x,t) + y_2(x,t)$$
$$y(x,t) = A \sin(kx - \omega t) + A \sin(kx + \omega t)$$

**Step 2: Use the trigonometric sum-to-product identity**
To simplify the sum of two sines, use the identity:
$$\sin(\alpha) + \sin(\beta) = 2 \sin\left(\frac{\alpha + \beta}{2}\right) \cos\left(\frac{\alpha - \beta}{2}\right)$$
Let $\alpha = kx - \omega t$ and $\beta = kx + \omega t$:
* Sum term: $\frac{(kx - \omega t) + (kx + \omega t)}{2} = \frac{2kx}{2} = kx$
* Difference term: $\frac{(kx - \omega t) - (kx + \omega t)}{2} = \frac{-2\omega t}{2} = -\omega t$

Substitute these back into the equation:
$$y(x,t) = 2A \sin(kx) \cos(-\omega t)$$

**Step 3: Simplify the standing wave equation**
Because the cosine function is even, $\cos(-\theta) = \cos(\theta)$. We can drop the negative sign to get the final standing wave equation:
$$y(x,t) = 2A \sin(kx) \cos(\omega t)$$
*(Note: The amplitude of the new standing wave is $2A \sin(kx)$, which depends on position $x$, while the oscillation over time is governed by $\cos(\omega t)$).*

**Step 4: Identify the positions of the nodes**
Nodes are points on the standing wave that never move. This happens when the spatial amplitude is equal to zero, regardless of time $t$.
$$\sin(kx) = 0$$
The sine function is zero at integer multiples of $\pi$:
$$kx = n\pi \quad \text{for } n = 0, 1, 2, \dots$$

**Step 5: Express node positions in terms of wavelength ($\lambda$)**
Recall that the wave number $k$ is defined as $k = \frac{2\pi}{\lambda}$. Substitute this into the equation:
$$\left(\frac{2\pi}{\lambda}\right)x = n\pi$$
Divide both sides by $\pi$ and solve for $x$:
$$\frac{2x}{\lambda} = n$$
$$x = \frac{n\lambda}{2} \quad \text{for } n = 0, 1, 2, \dots$$

---

**Final Answer:**
* **Standing wave equation:** $y(x,t) = 2A \sin(kx) \cos(\omega t)$
* **Positions of the nodes:** $x = \frac{n\lambda}{2}$ (where $n = 0, 1, 2, \dots$). Nodes occur every half-wavelength.
