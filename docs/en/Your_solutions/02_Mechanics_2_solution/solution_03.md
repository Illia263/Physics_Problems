### Problem 3: Conservation of Energy

**Given:**
* Length of pendulum ($L$): $1.0 \text{ m}$
* Initial angle ($\theta$): $15^\circ$
* Acceleration due to gravity ($g$): $\approx 9.8 \text{ m/s}^2$
* Initial velocity: $0 \text{ m/s}$ (it is "released")

**Goal:** Find the speed of the bob at the bottom of its swing ($v$).

**Step 1: Understand the energy transfer**
By the Law of Conservation of Energy, the gravitational potential energy ($PE$) the pendulum has at its highest point will be completely converted into kinetic energy ($KE$) at its lowest point. 
$$PE_{top} = KE_{bottom}$$
$$mgh = \frac{1}{2}mv^2$$
Notice that the mass ($m$) cancels out on both sides:
$$gh = \frac{1}{2}v^2$$

**Step 2: Calculate the change in height ($h$)**
To find the height the pendulum falls, we need to find the difference between the full length of the string and the vertical component of the string when it is held at $15^\circ$.
$$h = L - L\cos(\theta)$$
$$h = L(1 - \cos(\theta))$$

Substitute the known values:
$$h = 1.0 \cdot (1 - \cos(15^\circ))$$
$$h = 1.0 \cdot (1 - 0.9659)$$
$$h \approx 0.0341 \text{ m}$$

**Step 3: Calculate the speed ($v$)**
Now, substitute the height back into our simplified energy equation and solve for $v$.
$$gh = \frac{1}{2}v^2$$
$$v = \sqrt{2gh}$$
$$v = \sqrt{2 \cdot 9.8 \cdot 0.0341}$$
$$v = \sqrt{0.66836}$$
$$v \approx 0.817 \text{ m/s}$$

---

**Final Answer:**
The speed of the pendulum bob at the bottom of its swing is approximately **$0.817 \text{ m/s}$**.

Shall we proceed to Problem 4?
