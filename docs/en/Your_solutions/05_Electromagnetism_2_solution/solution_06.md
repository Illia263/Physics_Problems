Got it. Here is just the detailed and correctly formatted solution for problem number 6.

### **6. EM Wave Analysis**

**Given Equation:**


$$E_y(x,t) = 100\sin(10^7x - \omega t) \text{ V/m}$$

To extract the wave's properties, we compare this given equation to the standard general form of a traveling electromagnetic wave:


$$E(x,t) = E_{max}\sin(kx \pm \omega t)$$

By direct comparison, we identify the following parameters:

* **Amplitude ($E_{max}$):** The maximum electric field strength is **$100 \text{ V/m}$**.
* **Wave number ($k$):** The spatial frequency of the wave is **$10^7 \text{ rad/m}$**.
* **Polarization:** The $E_y$ notation indicates the electric field oscillates entirely along the **y-axis**.

---

**1. Direction of Propagation**

* **Reasoning:** The phase argument of the sine function is $(10^7x - \omega t)$. The presence of the variable $x$ indicates the wave is traveling along the x-axis. The negative sign between the spatial term ($kx$) and the temporal term ($\omega t$) indicates that the wave is moving in the positive direction.
* **Answer:** The direction of propagation is the **positive x-direction ($+x$)**.

**2. Wavelength ($\lambda$)**

* **Reasoning:** The wave number $k$ represents the number of radians per unit distance. It is related to the spatial period (wavelength, $\lambda$) by the equation $k = \frac{2\pi}{\lambda}$.
* **Calculation:**

$$\lambda = \frac{2\pi}{k} = \frac{2\pi}{10^7}$$


* **Answer:** The wavelength is **$2\pi \times 10^{-7} \text{ m}$** (approximately $6.28 \times 10^{-7} \text{ m}$, or $628 \text{ nm}$, which is in the visible light spectrum).

**3. Angular Frequency ($\omega$)**

* **Reasoning:** Assuming the wave travels in a vacuum (or air), its propagation speed is the speed of light, $c \approx 3 \times 10^8 \text{ m/s}$. The speed of a wave relates its angular frequency to its wave number via the equation $c = \frac{\omega}{k}$.
* **Calculation:**

$$\omega = c \cdot k$$


$$\omega = (3 \times 10^8 \text{ m/s}) \cdot (10^7 \text{ rad/m})$$


* **Answer:** The angular frequency is **$3 \times 10^{15} \text{ rad/s}$**.

**4. Equation for the Magnetic Field Component**

* **Reasoning (Amplitude):** In an electromagnetic wave, the magnitudes of the electric and magnetic fields are related by the speed of light: $E_{max} = c B_{max}$.

$$B_{max} = \frac{E_{max}}{c} = \frac{100}{3 \times 10^8} = \frac{1}{3} \times 10^{-6} \text{ T}$$


* **Reasoning (Phase):** In a vacuum, the oscillating electric and magnetic fields are perfectly in phase. Therefore, the sine argument remains exactly the same: $\sin(10^7x - 3 \times 10^{15}t)$.
* **Reasoning (Direction):** Electromagnetic waves are transverse. The direction of wave propagation (the Poynting vector) is given by the cross product of the electric and magnetic field unit vectors: $\hat{E} \times \hat{B} = \hat{S}$.
* We know propagation is in the $+x$ direction ($\hat{i}$).
* We know the E-field is in the $+y$ direction ($\hat{j}$).
* Therefore: $\hat{j} \times \hat{B} = \hat{i}$.
* Using standard cross-product rules, $\hat{j} \times \hat{k} = \hat{i}$. Thus, the magnetic field must oscillate in the **$+z$ direction ($\hat{k}$)**.


* **Answer:** The full equation for the magnetic field is:

$$B_z(x,t) = \left(\frac{1}{3} \times 10^{-6}\right) \sin(10^7x - 3 \times 10^{15}t) \text{ T}$$
