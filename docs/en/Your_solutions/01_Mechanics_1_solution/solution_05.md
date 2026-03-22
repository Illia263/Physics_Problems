# 6. Variable Velocity — Step-by-step Solution

## Most useful definitions and formulas

### 1) Position, velocity, acceleration (1D motion)

- **Position**: $x(t)$ — where the object is on a line at time $t$.
- **Velocity**: $v(t)$ — how fast and in which direction position changes.

$$
v(t)=\frac{dx}{dt}
$$

- **Acceleration**: $a(t)$ — how fast velocity changes.

$$
a(t)=\frac{dv}{dt}=\frac{d^2x}{dt^2}
$$

### 2) How to get position from velocity

If you know $v(t)$, then $x(t)$ is an antiderivative of $v(t)$:

$$
x(t)=\int v(t)\,dt + C
$$

You find the constant $C$ using an **initial condition**, e.g. $x(0)=x_0$.

### 3) How to get acceleration from velocity

Differentiate velocity:

$$
a(t)=\frac{dv}{dt}
$$

---

## Problem statement

Velocity:

$$
v(t)=t^2+2t-5
$$

Initial condition:

$$
x(0)=4
$$

Find:

- the **position** at $t=3$, i.e. $x(3)$
- the **acceleration** at $t=3$, i.e. $a(3)$

---

## Step 1 — Find acceleration from velocity

By definition:

$$
a(t)=\frac{dv}{dt}
$$

Differentiate $v(t)$ term-by-term:

$$
a(t)=\frac{d}{dt}(t^2+2t-5)=2t+2
$$

Now evaluate at $t=3$:

$$
a(3)=2\cdot 3 + 2 = 8
$$

**Result:**

$$
a(3)=8
$$

---

## Step 2 — Find the position function $x(t)$

Velocity is the derivative of position:

$$
v(t)=\frac{dx}{dt}
$$

So position is the integral of velocity:

$$
x(t)=\int (t^2+2t-5)\,dt
$$

Integrate term-by-term:

- $\int t^2\,dt=\frac{t^3}{3}$
- $\int 2t\,dt=t^2$
- $\int (-5)\,dt=-5t$

So:

$$
x(t)=\frac{t^3}{3}+t^2-5t+C
$$

---

## Step 3 — Use the initial condition to find $C$

We know:

$$
x(0)=4
$$

Substitute $t=0$ into the formula for $x(t)$:

$$
x(0)=\frac{0^3}{3}+0^2-5\cdot 0 + C = C
$$

So:

$$
C=4
$$

Therefore the **position function** is:

$$
x(t)=\frac{t^3}{3}+t^2-5t+4
$$

---

## Step 4 — Evaluate position at $t=3$

Substitute $t=3$:

$$
x(3)=\frac{3^3}{3}+3^2-5\cdot 3+4
$$

Compute step-by-step:

$$
x(3)=\frac{27}{3}+9-15+4
$$

$$
x(3)=9+9-15+4
$$

$$
x(3)=18-15+4
$$

$$
x(3)=3+4=7
$$

**Result:**

$$
x(3)=7
$$

---

## Final answers

Position at $t=3$:

$$
x(3)=7
$$

Acceleration at $t=3$:

$$
a(3)=8
$$
