Here is the step-by-step breakdown for the third problem. 

### 3. Electrostatic Equilibrium

**Given:**
* Charge 1: $q_1 = +4 \text{ C}$
* Charge 2: $q_2 = +9 \text{ C}$
* Test charge: $q_3 = +1 \text{ C}$
* Distance between $q_1$ and $q_2$: $d = 2 \text{ m}$

**Goal:** Find the exact position where $q_3$ experiences zero net force.

---

#### Step 1: Understand the Physics of Equilibrium
"Equilibrium" means the net force acting on the object is exactly zero. 

Because $q_1$ and $q_2$ are both positive, they will both try to repel the positive test charge $q_3$. 
* If you place $q_3$ to the left of $q_1$, both charges push it to the left.
* If you place $q_3$ to the right of $q_2$, both charges push it to the right. 
* Therefore, the only way the forces can push in opposite directions and cancel out is if $q_3$ is placed **somewhere on the line between them**.

#### Step 2: Set up the Geometry
Let's place $q_1$ at the origin ($x = 0$) and $q_2$ at $x = 2.00 \text{ m}$.
Let $x$ be the unknown distance from $q_1$ to our test charge $q_3$.
This means the distance from $q_2$ to $q_3$ will be the remaining distance: $(2.00 - x)$.

#### Step 3: Set up the Equation
For $q_3$ to be in equilibrium, the magnitude of the force pushing it to the right (from $q_1$) must perfectly equal the magnitude of the force pushing it to the left (from $q_2$).

$$F_1 = F_2$$

Using Coulomb's Law for both sides:
$$k \frac{q_1 q_3}{x^2} = k \frac{q_2 q_3}{(2.00 - x)^2}$$

Notice that Coulomb's constant ($k$) and the test charge ($q_3$) appear on both sides of the equation. We can completely divide them out! This reveals a cool physics fact: *the equilibrium position doesn't depend on the size or sign of the test charge $q_3$*.

$$\frac{q_1}{x^2} = \frac{q_2}{(2.00 - x)^2}$$

#### Step 4: Solve the Algebra
Now, plug in the values for $q_1$ and $q_2$:
$$\frac{4.00}{x^2} = \frac{9.00}{(2.00 - x)^2}$$

To avoid a messy quadratic equation, we can simply take the square root of both sides. Since we know $x$ must be a positive distance between the two charges, we don't need to worry about negative roots:
$$\frac{\sqrt{4.00}}{\sqrt{x^2}} = \frac{\sqrt{9.00}}{\sqrt{(2.00 - x)^2}}$$
$$\frac{2.00}{x} = \frac{3.00}{2.00 - x}$$

Now, cross-multiply to solve for $x$:
$$2.00 \cdot (2.00 - x) = 3.00 \cdot x$$
$$4.00 - 2.00x = 3.00x$$

Add $2.00x$ to both sides:
$$4.00 = 5.00x$$

Divide by 5:
$$x = \frac{4.00}{5.00} = 0.80 \text{ m}$$

---

**Final Answer:**
The equilibrium position is **$0.80 \text{ m}$ away from the $+4\text{C}$ charge** (which means it is $1.20 \text{ m}$ away from the $+9\text{C}$ charge). It makes sense that it sits closer to the smaller charge, as it needs to be closer to make up for the smaller charge's weaker push!

Ready for Problem 4 (Force Comparison)?