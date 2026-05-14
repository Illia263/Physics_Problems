**Given Equation:**
$E_y(x,t) = 100\sin(10^7x - \omega t) \text{ V/m}$

Comparing this to the standard wave equation $E(x,t) = E_{max}\sin(kx - \omega t)$:

- Amplitude ($E_{max}$) = $100 \text{ V/m}$
- Wave number ($k$) = $10^7 \text{ rad/m}$

---

**1. Direction of Propagation:**
The phase term $(10^7x - \omega t)$ depends on $x$, indicating the wave travels along the x-axis. The negative sign between the position and time terms indicates propagation in the positive direction.
**Answer:** The direction of propagation is the **positive x-direction ($+x$)**.

---

**2. Wavelength ($\lambda$):**
$$ \lambda = \frac{2\pi}{k} $$
$$ \lambda = \frac{2\pi}{10^7} $$
**Answer:** The wavelength is **$2\pi \times 10^{-7} \text{ m}$\*\* (or $\approx 6.28 \times 10^{-7} \text{ m}$).

---

**3. Angular Frequency ($\omega$):**
Assuming the wave travels in a vacuum, its speed is the speed of light ($c \approx 3 \times 10^8 \text{ m/s}$).
$$ \omega = c \cdot k $$
$$ \omega = (3 \times 10^8) \cdot (10^7) $$
**Answer:** The angular frequency is **$3 \times 10^{15} \text{ rad/s}$\*\*.

---

**4. Equation for the Magnetic Field Component:**
First, find the amplitude of the magnetic field ($B_{max}$):
$$ B*{max} = \frac{E*{max}}{c} = \frac{100}{3 \times 10^8} = \frac{1}{3} \times 10^{-6} \text{ T} $$

Next, determine the direction. The direction of propagation ($\hat{i}$) is given by the cross product of the electric and magnetic field unit vectors ($\hat{E} \times \hat{B}$).
Since $\vec{E}$ is in the $+y$ direction ($\hat{j}$) and propagation is in the $+x$ direction ($\hat{i}$):
$$ \hat{j} \times \hat{B} = \hat{i} $$
Because $\hat{j} \times \hat{k} = \hat{i}$, the magnetic field must oscillate in the **$+z$ direction ($\hat{k}$)**.

**Answer:**
The equation for the magnetic field is:
$$ B_z(x,t) = \left(\frac{1}{3} \times 10^{-6}\right) \sin(10^7x - 3 \times 10^{15}t) \text{ T} $$
