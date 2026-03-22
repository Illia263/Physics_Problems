### Problem 10: Kinematics

**Given:**
$$\vec{r}(t) = (a\cos(\omega t), b\sin(\omega t), bt)$$
where $a, b, \omega$ are positive constants.

---

#### a) Find the equation of the point's trajectory

**Step 1: Separate the position vector into $x$, $y$, and $z$ parametric equations**
$$x = a\cos(\omega t)$$
$$y = b\sin(\omega t)$$
$$z = bt$$

**Step 2: Eliminate time ($t$) to find the geometric shape**
Divide $x$ by $a$ and $y$ by $b$, then square and add them together to use the trigonometric identity $\cos^2(\theta) + \sin^2(\theta) = 1$:
$$\left(\frac{x}{a}\right)^2 + \left(\frac{y}{b}\right)^2 = \cos^2(\omega t) + \sin^2(\omega t)$$
$$\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$$

**Answer:** The trajectory lies on the surface of an elliptical cylinder defined by $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$. Because $z$ increases linearly with time ($z = bt$), the resulting 3D path is an **elliptical helix**.

---

#### b) Compute the path length from $t = 0$ to $t = t_0$

**Step 1: Find the velocity vector $\vec{v}(t)$**
Take the derivative of the position vector $\vec{r}(t)$.
$$\vec{v}(t) = \frac{d\vec{r}}{dt} = (-a\omega\sin(\omega t), b\omega\cos(\omega t), b)$$

**Step 2: Find the magnitude of the velocity (speed) $|\vec{v}(t)|$**
$$|\vec{v}(t)| = \sqrt{(-a\omega\sin(\omega t))^2 + (b\omega\cos(\omega t))^2 + b^2}$$
$$|\vec{v}(t)| = \sqrt{a^2\omega^2\sin^2(\omega t) + b^2\omega^2\cos^2(\omega t) + b^2}$$

**Step 3: Integrate speed over time to get path length ($S$)**
$$S = \int_{0}^{t_0} |\vec{v}(t)| dt$$
$$S = \int_{0}^{t_0} \sqrt{a^2\omega^2\sin^2(\omega t) + b^2\omega^2\cos^2(\omega t) + b^2} dt$$
_(Note for your teacher: In the general case where $a \neq b$, this does not have a simple analytical solution and requires solving an incomplete elliptic integral of the second kind)._

---

#### c) Special Cases and Python Trajectory

**Discussion of Special Cases:**
The most important special case is when **$a = b$**.
If $a = b$, the base equation $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ simplifies to $x^2 + y^2 = a^2$ (a circle). The trajectory becomes a perfect **circular helix**.
In this case, the path length integral from part (b) simplifies dramatically because $\sin^2(\omega t) + \cos^2(\omega t) = 1$:
$$|\vec{v}(t)| = \sqrt{a^2\omega^2(\sin^2(\omega t) + \cos^2(\omega t)) + b^2} = \sqrt{a^2\omega^2 + b^2}$$
Since the speed is now a constant, the path length is simply:
$$S = t_0\sqrt{a^2\omega^2 + b^2}$$
