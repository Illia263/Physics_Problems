
### **Given Values**

* **Battery Voltage ($V$):** 12 V
* **Resistor 1 ($R_1$):** $15\,\Omega$
* **Resistor 2 ($R_2$):** $30\,\Omega$
* **Resistor 3 ($R_3$):** $50\,\Omega$

---

### **Case 1: All Resistors in Series**

**1. Equivalent Resistance ($R_s$)**
In a series circuit, the total equivalent resistance is simply the sum of all individual resistances:


$$R_s = R_1 + R_2 + R_3$$

$$R_s = 15 + 30 + 50$$

$$R_s = 95\,\Omega$$

**2. Total Current ($I_s$)**
Using Ohm's Law ($I = \frac{V}{R}$), the current flowing from the battery is:


$$I_s = \frac{V}{R_s}$$

$$I_s = \frac{12}{95}$$

$$I_s \approx 0.126\text{ A}$$

---

### **Case 2: All Resistors in Parallel**

**1. Equivalent Resistance ($R_p$)**
In a parallel circuit, the reciprocal of the total equivalent resistance is the sum of the reciprocals of the individual resistances:


$$\frac{1}{R_p} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3}$$

$$\frac{1}{R_p} = \frac{1}{15} + \frac{1}{30} + \frac{1}{50}$$

To add these fractions, we find the common denominator, which is 150:


$$\frac{1}{R_p} = \frac{10}{150} + \frac{5}{150} + \frac{3}{150}$$

$$\frac{1}{R_p} = \frac{18}{150}$$

Now, flip the fraction to solve for $R_p$:


$$R_p = \frac{150}{18}$$

$$R_p \approx 8.33\,\Omega$$

**2. Total Current ($I_p$)**
Using Ohm's Law again with our exact fractional resistance to prevent rounding errors:


$$I_p = \frac{V}{R_p}$$

$$I_p = \frac{12}{\frac{150}{18}}$$

$$I_p = 12 \times \frac{18}{150}$$

$$I_p = \frac{216}{150}$$

$$I_p = 1.44\text{ A}$$

These theoretical calculations provide a reliable baseline for the assignment, making it much easier to spot any discrepancies if you end up comparing these numbers against actual laboratory experiment results with your classmate later on.
