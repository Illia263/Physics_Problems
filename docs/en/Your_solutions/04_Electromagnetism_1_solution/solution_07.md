Here is the step-by-step breakdown for the seventh problem. This one is a classic two-part physics problem: first we speed the electron up using electricity, then we bend its path using magnetism!

### 7. Cyclotron Motion

**Given:**
* Particle: Electron
* Charge of an electron: $q = 1.60 \times 10^{-19} \text{ C}$
* Mass of an electron: $m_e = 9.11 \times 10^{-31} \text{ kg}$
* Accelerating potential (Voltage): $V = 5000 \text{ V}$
* Magnetic field strength: $B = 0.10 \text{ T}$

**Goal:** Find the radius ($r$) of the circular path.

---

#### Step 1: The "Electron Gun" (Acceleration Phase)
Before the electron enters the magnetic field, it is accelerated from rest by an electric field (created by the 5000 V potential difference). 

Due to the law of Conservation of Energy, the electric potential energy lost by the electron is entirely converted into its kinetic energy of motion.
$$E_{electric} = E_{kinetic}$$
$$qV = \frac{1}{2}m_e v^2$$

Let's rearrange this to find the speed ($v$) of the electron just as it leaves the "gun":
$$v^2 = \frac{2qV}{m_e}$$
$$v = \sqrt{\frac{2qV}{m_e}}$$

*(We could plug the numbers in right now to find the velocity, but physicists usually prefer to combine formulas algebraically first to prevent rounding errors!)*

#### Step 2: The Magnetic Field (Circular Motion Phase)
When a charged particle enters a uniform magnetic field perpendicular to its velocity, the magnetic force (Lorentz force) acts sideways, acting as a **centripetal force**. This forces the electron into a perfect circle.

We set the Magnetic Force equal to the Centripetal Force:
$$F_B = F_c$$
$$qvB = \frac{m_e v^2}{r}$$

We want to find the radius, $r$. Let's solve for it. First, cancel one $v$ from both sides:
$$qB = \frac{m_e v}{r}$$

Now, rearrange for $r$:
$$r = \frac{m_e v}{qB}$$

#### Step 3: Combine and Calculate
Now, substitute our velocity equation from Step 1 into our radius equation from Step 2:
$$r = \frac{m_e}{qB} \sqrt{\frac{2qV}{m_e}}$$

To make the math cleaner, bring the $m_e$ and $q$ outside the square root *inside* it (they become squared):
$$r = \frac{1}{B} \sqrt{\frac{2 m_e^2 q V}{m_e q^2}}$$
$$r = \frac{1}{B} \sqrt{\frac{2 m_e V}{q}}$$

Now, plug in our known values!
$$r = \frac{1}{0.10} \sqrt{\frac{2(9.11 \times 10^{-31})(5000)}{1.60 \times 10^{-19}}}$$
$$r = 10 \cdot \sqrt{\frac{9.11 \times 10^{-27}}{1.60 \times 10^{-19}}}$$
$$r = 10 \cdot \sqrt{5.69 \times 10^{-8}}$$
$$r = 10 \cdot (2.39 \times 10^{-4})$$
$$r = 2.39 \times 10^{-3} \text{ m}$$

---

**Final Answer:**
The radius of the electron's circular path will be **$2.39 \times 10^{-3} \text{ m}$** (or about **2.39 millimeters**).

To see how the accelerating voltage and the magnetic field strength battle it out to determine the radius, try playing with this interactive cyclotron simulator!

