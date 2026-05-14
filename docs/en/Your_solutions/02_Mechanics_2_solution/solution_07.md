### Problem 7: Dynamics with Friction

**Given:**
* Mass of top block ($m_1$): **5 kg**
* Mass of bottom block ($m_2$): **10 kg**
* Applied horizontal force ($F$): **45 N**
* Coefficient of kinetic friction ($\mu_k$): **0.2**
* Acceleration due to gravity ($g$): $\approx 9.8$ m/s²

**Goal:** Find the acceleration ($a$) of the **10 kg** block.

**Step 1: Identify all forces acting on the 10 kg block**
Because the 5 kg block is tied to the wall, it remains stationary while the 10 kg block slides underneath it. This means the 10 kg block experiences kinetic friction from *two* surfaces:
1. Friction from the 5 kg block dragging on its top surface.
2. Friction from the floor dragging on its bottom surface.

**Step 2: Calculate the friction from the top block ($f_{k1}$)**
The normal force pressing down on the top of the 10 kg block is just the weight of the 5 kg block.
$$N_1 = m_1g$$
$$N_1 = 5 \cdot 9.8 = 49 \text{ N}$$

Now, calculate the kinetic friction for this surface:
$$f_{k1} = \mu_k N_1$$
$$f_{k1} = 0.2 \cdot 49 = 9.8 \text{ N}$$

**Step 3: Calculate the friction from the floor ($f_{k2}$)**
The normal force pressing down on the floor is the combined weight of *both* blocks.
$$N_2 = (m_1 + m_2)g$$
$$N_2 = (5 + 10) \cdot 9.8$$
$$N_2 = 15 \cdot 9.8 = 147 \text{ N}$$

Now, calculate the kinetic friction for the floor:
$$f_{k2} = \mu_k N_2$$
$$f_{k2} = 0.2 \cdot 147 = 29.4 \text{ N}$$

**Step 4: Apply Newton's Second Law**
The net horizontal force equals the mass of the moving block times its acceleration. The applied force pulls it forward, while both friction forces pull it backward.
$$\Sigma F = m_2a$$
$$F - f_{k1} - f_{k2} = m_2a$$

Substitute the known values:
$$45 - 9.8 - 29.4 = 10a$$
$$45 - 39.2 = 10a$$
$$5.8 = 10a$$
$$a = \frac{5.8}{10}$$
$$a = 0.58 \text{ m/s}^2$$

*(Note: If your course rounds gravity to **10 m/s²**, the frictions would be **10 N** and **30 N**, leaving a net force of **5 N**, which gives exactly **0.5 m/s²**).*

---

**Final Answer:**
The acceleration of the 10 kg block is **0.58 m/s²** (assuming $g = 9.8$ m/s²).

Ready for Problem 8?
