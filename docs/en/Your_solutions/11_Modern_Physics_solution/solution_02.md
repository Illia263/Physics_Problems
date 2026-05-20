Here is the step-by-step breakdown of all possible equivalent resistances using exactly three $1\,\Omega$ resistors.

To find all unique values, we need to look at the four different ways to physically wire three identical components together.

### **Given Value**

* **Resistors ($R_1, R_2, R_3$):** $1\,\Omega$ each

---

### **Configuration 1: All Three in Series**

When all three resistors are connected end-to-end, the current must pass through each one sequentially. The equivalent resistance is the sum of all three.

$$R_{eq} = R_1 + R_2 + R_3$$

$$R_{eq} = 1 + 1 + 1$$

$$R_{eq} = 3\,\Omega$$

---

### **Configuration 2: All Three in Parallel**

When all three resistors are connected side-by-side, the current splits across three paths. The reciprocal of the equivalent resistance is the sum of their reciprocals.

$$\frac{1}{R_{eq}} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3}$$

$$\frac{1}{R_{eq}} = \frac{1}{1} + \frac{1}{1} + \frac{1}{1}$$

$$\frac{1}{R_{eq}} = 3$$

$$R_{eq} = \frac{1}{3}\,\Omega$$

---

### **Configuration 3: Two in Parallel, Series with the Third**

In this mixed circuit, two resistors are in parallel, and that parallel block is in series with the final resistor.

**Step 1: Calculate the parallel block ($R_p$)**


$$\frac{1}{R_p} = \frac{1}{1} + \frac{1}{1} = 2$$

$$R_p = \frac{1}{2}\,\Omega$$

**Step 2: Add the series resistor**


$$R_{eq} = R_p + R_3$$

$$R_{eq} = \frac{1}{2} + 1$$

$$R_{eq} = 1.5\,\Omega \text{ (or } \frac{3}{2}\,\Omega)$$

---

### **Configuration 4: Two in Series, Parallel with the Third**

In this mixed circuit, two resistors are in series, and that whole series block is wired in parallel with the final resistor.

**Step 1: Calculate the series block ($R_s$)**


$$R_s = R_1 + R_2$$

$$R_s = 1 + 1 = 2\,\Omega$$

**Step 2: Calculate the parallel equivalent**


$$\frac{1}{R_{eq}} = \frac{1}{R_s} + \frac{1}{R_3}$$

$$\frac{1}{R_{eq}} = \frac{1}{2} + \frac{1}{1}$$

$$\frac{1}{R_{eq}} = \frac{3}{2}$$

$$R_{eq} = \frac{2}{3}\,\Omega$$

---

### **Final Answer**

By combining exactly three $1\,\Omega$ resistors, you can create four unique equivalent resistances. Listed from lowest to highest, they are:

* **$1/3\,\Omega$**
* **$2/3\,\Omega$**
* **$1.5\,\Omega$**
* **$3\,\Omega$**
