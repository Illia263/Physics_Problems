Here is the step-by-step breakdown for the ninth problem. This is where we leave the simple 2D world behind and unleash the full mathematical power of 3D vectors!

### 9. Vector Lorentz Force

**Given:**
* Particle: Proton
* Charge of a proton: $q = 1.60 \times 10^{-19} \text{ C}$
* Velocity vector: $\vec{v} = (2\hat{i} - 4\hat{j} + \hat{k}) \text{ m/s}$
* Magnetic field vector: $\vec{B} = (\hat{i} + 2\hat{j} - \hat{k}) \text{ T}$

**Goal:** Find the magnitude of the magnetic force ($|\vec{F}|$) acting on the proton.

---

#### Step 1: The Vector Equation
In the previous problem, we used the simplified "magnitude only" formula ($F = qvB\sin\theta$). The *true* form of the Lorentz magnetic force equation is a 3D **cross product**:
$$\vec{F} = q(\vec{v} \times \vec{B})$$

The cross product ($\times$) is a mathematical operation that takes two 3D vectors and generates a brand new third vector that is perfectly perpendicular to both of them. 

#### Step 2: Calculate the Cross Product ($\vec{v} \times \vec{B}$)
To find the cross product, we set up a 3x3 matrix determinant using our $\hat{i}$ (x), $\hat{j}$ (y), and $\hat{k}$ (z) components:

$$\vec{v} \times \vec{B} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ v_x & v_y & v_z \\ B_x & B_y & B_z \end{vmatrix} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 2 & -4 & 1 \\ 1 & 2 & -1 \end{vmatrix}$$

Now, we expand it component by component:
* **$\hat{i}$ component:** $(-4)(-1) - (1)(2) = 4 - 2 = 2$
* **$\hat{j}$ component:** $-((2)(-1) - (1)(1)) = -(-2 - 1) = 3$ *(Don't forget the negative sign for the j-component!)*
* **$\hat{k}$ component:** $(2)(2) - (-4)(1) = 4 + 4 = 8$

Putting it all together, our cross product vector is:
$$\vec{v} \times \vec{B} = 2\hat{i} + 3\hat{j} + 8\hat{k}$$

#### Step 3: Find the Magnitude of the Cross Product
To find the physical "length" (magnitude) of this new vector, we use the 3D Pythagorean theorem:
$$|\vec{v} \times \vec{B}| = \sqrt{x^2 + y^2 + z^2}$$
$$|\vec{v} \times \vec{B}| = \sqrt{2^2 + 3^2 + 8^2}$$
$$|\vec{v} \times \vec{B}| = \sqrt{4 + 9 + 64}$$
$$|\vec{v} \times \vec{B}| = \sqrt{77} \approx 8.775 \text{ m}\cdot\text{T/s}$$

#### Step 4: Calculate the Final Force
Now we just multiply this magnitude by the charge of the proton ($q$) to get the total force in Newtons:
$$F = q |\vec{v} \times \vec{B}|$$
$$F = (1.60 \times 10^{-19}) \cdot (\sqrt{77})$$
$$F \approx (1.60 \times 10^{-19}) \cdot (8.775)$$
$$F \approx 1.40 \times 10^{-18} \text{ N}$$

---

**Final Answer:**
The magnitude of the magnetic force the proton experiences is **$1.40 \times 10^{-18} \text{ N}$**.



Are you ready to tackle the very last problem on your list? Problem 10 covers the magnetic force on a whole wire!