### Problem 3: Path Intersection

**Given:**

- Alice's position: $A(t) = (2 + t, 8 - 3t)$
- Bob's position: $B(t) = (2t - 1, 2t + 2)$

**Step 1: Check for a collision**
A collision means they are at the exact same $x$ and $y$ coordinates at the exact same time $t$.

Set their $x$-coordinates equal to find a potential collision time:
$$2 + t = 2t - 1$$
$$t = 3$$

Now, check if their $y$-coordinates match at $t = 3$:

- Alice's $y$ at $t=3$: $8 - 3(3) = -1$
- Bob's $y$ at $t=3$: $2(3) + 2 = 8$

Since $-1 \neq 8$, they **do not collide**. _(Note: Their paths do technically cross, but since they arrive at the intersection point at different times, there is no collision)._

**Step 2: Set up the distance equation**
Since they don't collide, we need to find the minimum distance between them. The distance $D$ at any time $t$ is found using the distance formula. To make the calculus easier, we will optimize the squared distance $D^2(t)$.
$$D^2(t) = (x_A - x_B)^2 + (y_A - y_B)^2$$
$$D^2(t) = ((2 + t) - (2t - 1))^2 + ((8 - 3t) - (2t + 2))^2$$
$$D^2(t) = (3 - t)^2 + (6 - 5t)^2$$

**Step 3: Expand and simplify**
$$D^2(t) = (9 - 6t + t^2) + (36 - 60t + 25t^2)$$
$$D^2(t) = 26t^2 - 66t + 45$$

**Step 4: Find the time ($t$) of minimum distance**
To find the minimum, take the first derivative with respect to $t$ and set it to $0$.
$$\frac{d}{dt} D^2(t) = 52t - 66$$
$$52t - 66 = 0$$
$$52t = 66$$
$$t = \frac{66}{52} = \frac{33}{26}$$

**Step 5: Calculate the minimum distance**
Substitute $t = \frac{33}{26}$ back into our $D^2(t)$ equation:
$$D^2\left(\frac{33}{26}\right) = 26\left(\frac{33}{26}\right)^2 - 66\left(\frac{33}{26}\right) + 45$$
$$D^2\left(\frac{33}{26}\right) = \frac{1089}{26} - \frac{2178}{26} + \frac{1170}{26}$$ _(Note: $45 = \frac{1170}{26}$)_
$$D^2\left(\frac{33}{26}\right) = \frac{81}{26}$$

Take the square root to find the actual distance $D$:
$$D = \sqrt{\frac{81}{26}} = \frac{9}{\sqrt{26}}$$

**Final Answer:**

- **Collision:** No.
- **Time of minimum distance:** $t = \frac{33}{26}$ (approx. $1.27$)
- **Minimum distance:** $\frac{9}{\sqrt{26}}$ (approx. $1.76$)

Would you like me to solve the next one?
