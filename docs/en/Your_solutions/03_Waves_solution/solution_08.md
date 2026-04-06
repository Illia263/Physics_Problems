### Problem 8: Waves

**Given:**
* The 1D wave equation: 
  $$\frac{\partial^2 y}{\partial x^2} = \frac{1}{v^2} \frac{\partial^2 y}{\partial t^2}$$
* Three test functions:
  a) $y(x,t) = A \cos(kx^2 - \omega t)$
  b) $y(x,t) = A(x-vt)^2$
  c) $y(x,t) = A \log(x+vt)$

**Goal:** Check which of the given functions satisfy the wave equation and can therefore describe a traveling wave.

**Step 1: Test function (a) — $y(x,t) = A \cos(kx^2 - \omega t)$**
Find the second partial derivative with respect to $x$:
* First derivative: $\frac{\partial y}{\partial x} = -A \sin(kx^2 - \omega t) \cdot (2kx)$
* Second derivative (requires product rule): 
  $$\frac{\partial^2 y}{\partial x^2} = -2Ak \sin(kx^2 - \omega t) - 4Ak^2x^2 \cos(kx^2 - \omega t)$$

Find the second partial derivative with respect to $t$:
* First derivative: $\frac{\partial y}{\partial t} = A \omega \sin(kx^2 - \omega t)$
* Second derivative: $\frac{\partial^2 y}{\partial t^2} = -A \omega^2 \cos(kx^2 - \omega t)$

*Comparison:* If we plug these into the wave equation, the left side has a sine term and an $x^2$ term, while the right side only has a cosine term. They cannot be equal for all $x$ and $t$.
**(Fails the wave equation)**

**Step 2: Test function (b) — $y(x,t) = A(x-vt)^2$**
Find the second partial derivative with respect to $x$:
* First derivative: $\frac{\partial y}{\partial x} = 2A(x-vt) \cdot 1$
* Second derivative: $\frac{\partial^2 y}{\partial x^2} = 2A$

Find the second partial derivative with respect to $t$:
* First derivative: $\frac{\partial y}{\partial t} = 2A(x-vt) \cdot (-v) = -2Av(x-vt)$
* Second derivative: $\frac{\partial^2 y}{\partial t^2} = -2Av(-v) = 2Av^2$

*Comparison:* Substitute both second derivatives into the wave equation:
$$2A = \frac{1}{v^2} \left( 2Av^2 \right)$$
$$2A = 2A$$
**(Satisfies the wave equation)**

**Step 3: Test function (c) — $y(x,t) = A \log(x+vt)$**
Find the second partial derivative with respect to $x$:
* First derivative: $\frac{\partial y}{\partial x} = A \cdot \frac{1}{x+vt} \cdot 1 = \frac{A}{x+vt}$
* Second derivative: $\frac{\partial^2 y}{\partial x^2} = -\frac{A}{(x+vt)^2}$

Find the second partial derivative with respect to $t$:
* First derivative: $\frac{\partial y}{\partial t} = A \cdot \frac{1}{x+vt} \cdot v = \frac{Av}{x+vt}$
* Second derivative: $\frac{\partial^2 y}{\partial t^2} = - \frac{Av \cdot v}{(x+vt)^2} = -\frac{Av^2}{(x+vt)^2}$

*Comparison:* Substitute both second derivatives into the wave equation:
$$-\frac{A}{(x+vt)^2} = \frac{1}{v^2} \left( -\frac{Av^2}{(x+vt)^2} \right)$$
$$-\frac{A}{(x+vt)^2} = -\frac{A}{(x+vt)^2}$$
**(Satisfies the wave equation)**

---

**Final Answer:**
Functions **(b)** and **(c)** can describe a traveling wave because they satisfy the wave equation. Function (a) cannot.
