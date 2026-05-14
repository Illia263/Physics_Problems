# Physics Problem Solution: Biot-Savart Law

**Problem Statement:**
A small segment of a line wire of length $0.1 \text{ m}$ carries a current of $3 \text{ A}$. The segment is located at a distance of $0.2 \text{ m}$ from a point $P$. Calculate the magnetic field at point $P$ due to this current segment (assume the segment is perpendicular to the line connecting it to point $P$).

---

## 1. Given Data

*   **Length of the wire segment ($dl$):** $0.1 \text{ m}$
*   **Current ($I$):** $3 \text{ A}$
*   **Distance to point $P$ ($r$):** $0.2 \text{ m}$
*   **Angle between segment and position vector ($\theta$):** $90^\circ$ (the problem states the segment is perpendicular to the line connecting it to point $P$).
*   **Vacuum permeability constant ($\mu_0$):** $4\pi \times 10^{-7} \text{ T}\cdot\text{m/A}$

## 2. Relevant Formula

To find the magnetic field created by a small, finite segment of wire, we use the magnitude form of the **Biot-Savart Law**:

$$dB = \frac{\mu_0}{4\pi} \frac{I \cdot dl \cdot \sin(\theta)}{r^2}$$

Where:
*   $dB$ is the infinitesimally small magnetic field.
*   $\frac{\mu_0}{4\pi}$ is the magnetic constant, which simplifies exactly to $10^{-7} \text{ T}\cdot\text{m/A}$.

## 3. Step-by-Step Calculation

**Step 1: Determine the value of the sine term.**
Since the current segment is perpendicular to the radial distance $r$, $\theta = 90^\circ$.
$$\sin(90^\circ) = 1$$

**Step 2: Substitute the known values into the equation.**
$$dB = (10^{-7}) \cdot \frac{3 \cdot 0.1 \cdot 1}{(0.2)^2}$$

**Step 3: Simplify the numerator and denominator.**
*   Numerator: $3 \cdot 0.1 = 0.3 \text{ A}\cdot\text{m}$
*   Denominator: $(0.2)^2 = 0.04 \text{ m}^2$

$$dB = 10^{-7} \cdot \frac{0.3}{0.04}$$

**Step 4: Calculate the final value.**
$$\frac{0.3}{0.04} = 7.5$$

$$dB = 7.5 \times 10^{-7} \text{ T}$$

## 4. Final Answer

The magnetic field at point $P$ due to the current segment is:

**$$dB = 7.5 \times 10^{-7} \text{ T}$$** *(or $0.75 \text{ \mu T}$)*
