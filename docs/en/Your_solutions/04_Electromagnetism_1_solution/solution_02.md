Here is the step-by-step breakdown for the second problem. 

### 2. Electric Potential

**Given:**
* Four corner charges: $q_1 = +1.00 \text{ C}$, $q_2 = -2.00 \text{ C}$, $q_3 = +3.00 \text{ C}$, $q_4 = -4.00 \text{ C}$
* Side length of the square: $a = 1.00 \text{ m}$
* Coulomb's constant: $k = 8.99 \times 10^9 \text{ N}\cdot\text{m}^2/\text{C}^2$

**Goal:** Calculate the total electric potential ($V$) at the exact center of the square.

---

#### Step 1: Understand the difference between Force and Potential
In the previous problem, we calculated Electric *Force*, which is a **vector** (it has direction, and arrows can cancel each other out). 

Electric *Potential* (Voltage), however, is a **scalar** quantity. It has no direction, only a magnitude and a sign (positive or negative). To find the total electric potential at a point, you simply calculate the potential from each individual charge and add them together like normal numbers.

#### Step 2: Find the distance to the center ($r$)
First, we need to know the distance from the corners to the center. 
* The diagonal of a square with side $a$ is given by the Pythagorean theorem: $\text{Diagonal} = \sqrt{a^2 + a^2} = a\sqrt{2}$.
* For our square, the diagonal is $1.00\sqrt{2} \approx 1.414 \text{ m}$.
* The center is exactly halfway along the diagonal. So, the distance $r$ from any corner to the center is:
$$r = \frac{1.00\sqrt{2}}{2} = \frac{1.00}{\sqrt{2}} \approx 0.707 \text{ m}$$

#### Step 3: Set up the equation
The formula for the electric potential from a single point charge is $V = \frac{kq}{r}$. 
Since all four charges are the exact same distance ($r$) from the center, we can factor out the $\frac{k}{r}$ part to make the math much easier:

$$V_{total} = V_1 + V_2 + V_3 + V_4$$
$$V_{total} = \frac{k q_1}{r} + \frac{k q_2}{r} + \frac{k q_3}{r} + \frac{k q_4}{r}$$
$$V_{total} = \frac{k}{r} (q_1 + q_2 + q_3 + q_4)$$

#### Step 4: Calculate the final value
Now, we just plug in our numbers. Note how the positive and negative charges partially cancel each other out algebraically inside the parentheses:

$$V_{total} = \frac{8.99 \times 10^9}{0.707} (1.00 - 2.00 + 3.00 - 4.00)$$
$$V_{total} = \frac{8.99 \times 10^9}{0.707} (-2.00)$$
$$V_{total} \approx 1.27 \times 10^{10} \cdot (-2.00)$$
$$V_{total} = -25.4 \times 10^9 \text{ V}$$

*(Or $-2.54 \times 10^{10} \text{ Volts}$. The negative sign indicates that the center of the square is at a lower electric potential than a point infinitely far away, entirely due to the fact that the negative charges at the corners outnumber/outweigh the positive ones).*

---
Ready for Problem 3 (Electrostatic Equilibrium)?