### Problem 8: Work of a Variable Force

**Given:**
A one-dimensional force: $$F(x) = -kx$$
*(Note: This is the standard equation for Hooke's Law, representing a restoring force like a spring).*

---

**Step 1: Write down the equation of motion and solve it**
Using Newton's Second Law ($F = ma$), we can write the equation of motion by replacing acceleration ($a$) with the second derivative of position with respect to time ($\frac{d^2x}{dt^2}$):
$$m\frac{d^2x}{dt^2} = -kx$$
$$\frac{d^2x}{dt^2} + \frac{k}{m}x = 0$$

**Solution:** This is the classic differential equation for a Simple Harmonic Oscillator. By defining the angular frequency as $\omega = \sqrt{\frac{k}{m}}$, the general solution is:
$$x(t) = A\cos(\omega t + \phi)$$
*(Where $A$ is the amplitude and $\phi$ is the initial phase, both determined by initial conditions).*

**Step 2: Calculate the work done during the displacement from $0$ to $x_0$**
The work done by a variable force is the integral of the force over the displacement.
$$W = \int_{x_i}^{x_f} F(x) dx$$
$$W = \int_{0}^{x_0} -kx \, dx$$
$$W = \left[ -\frac{1}{2}kx^2 \right]_{0}^{x_0}$$
$$W = \left(-\frac{1}{2}kx_0^2\right) - (0)$$
$$W = -\frac{1}{2}kx_0^2$$

**Step 3: Interpret the result as potential energy**
The work done by a conservative force (like this spring force) is equal to the negative change in potential energy ($\Delta U$).
$$W = -\Delta U = -(U_{final} - U_{initial})$$
Assuming the potential energy at the equilibrium position is zero ($U(0) = 0$):
$$-\frac{1}{2}kx_0^2 = -U(x_0)$$
$$U(x_0) = \frac{1}{2}kx_0^2$$
**Interpretation:** The negative work done *by* the force means that energy is being stored *into* the system as **elastic potential energy**. If you stretch or compress a spring by a distance $x_0$, the system stores $\frac{1}{2}kx_0^2$ Joules of energy.

**Step 4: Verify the relationship $F = -\frac{dU}{dx}$**
We now have our potential energy function: $U(x) = \frac{1}{2}kx^2$. Let's take the negative derivative with respect to $x$:
$$-\frac{dU}{dx} = -\frac{d}{dx} \left(\frac{1}{2}kx^2\right)$$
Using the power rule (bring down the 2, subtract 1 from the exponent):
$$-\frac{dU}{dx} = -\frac{1}{2}k(2x)$$
$$-\frac{dU}{dx} = -kx$$
Since $-kx$ is exactly our initial force $F(x)$, the relationship is verified!

**Step 5: Draw the graph of $F(x)$ and $U(x)$**
* **$F(x) = -kx$:** This is a straight line passing through the origin $(0,0)$ with a negative slope of $-k$. It goes down from top-left to bottom-right.
* **$U(x) = \frac{1}{2}kx^2$:** This is a parabola opening upwards with its lowest point (vertex) resting exactly at the origin $(0,0)$.

---

Ready for Problem 9?
