### Problem 2: Harmonic Motion

**Given:**
* Mass ($m$): $10 \text{ kg}$
* Equation of motion: $x(t) = 0.2 \cos(10\pi t)$ (in meters)

**Goal:** Find the spring constant ($k$) and the total mechanical energy of the system ($E$).

**Step 1: Extract parameters from the given equation**
The standard equation for simple harmonic motion is:
$$x(t) = A \cos(\omega t)$$
By comparing this to our given equation $x(t) = 0.2 \cos(10\pi t)$, we can identify:
* Amplitude ($A$) = $0.2 \text{ m}$
* Angular frequency ($\omega$) = $10\pi \text{ rad/s}$

**Step 2: Calculate the spring constant ($k$)**
The angular frequency $\omega$ is related to the mass and the spring constant by the formula:
$$\omega = \sqrt{\frac{k}{m}}$$
Squaring both sides and solving for $k$ gives:
$$k = m\omega^2$$
Substitute the known values:
$$k = 10 \cdot (10\pi)^2$$
$$k = 10 \cdot 100\pi^2$$
$$k = 1000\pi^2 \text{ N/m}$$ *(approx. $9869.6 \text{ N/m}$)*

**Step 3: Calculate the total mechanical energy ($E$)**
In simple harmonic motion, the total mechanical energy is conserved and is equal to the maximum potential energy stored in the spring (which occurs when the mass is at its maximum displacement, $A$).
$$E = \frac{1}{2}kA^2$$
Substitute the values for $k$ and $A$:
$$E = \frac{1}{2}(1000\pi^2)(0.2)^2$$
$$E = 500\pi^2 \cdot 0.04$$
$$E = 20\pi^2 \text{ J}$$ *(approx. $197.39 \text{ J}$)*

---

**Final Answer:**
* **Spring constant ($k$):** $1000\pi^2 \text{ N/m}$ (or $\approx 9869.6 \text{ N/m}$)
* **Total mechanical energy:** $20\pi^2 \text{ J}$ (or $\approx 197.4 \text{ J}$)
