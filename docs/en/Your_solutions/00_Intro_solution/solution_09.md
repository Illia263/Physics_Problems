### Problem 9: Optimization Problem

**Given:**

- Curve:
  $$y = 3 - x^2$$

- Location: First quadrant ($x > 0$, $y > 0$)

**Goal:** Find the dimensions (width $x$ and height $y$) of the rectangle that yield the maximum area.

**Step 1: Set up the area equation**
The area of a rectangle is width times height. Since the rectangle is in the first quadrant with one corner at the origin and the opposite corner on the curve, its width is $x$ and its height is $y$.

$$\text{Area} = x \cdot y$$

Substitute the given equation for $y$ into the area formula to get it in terms of a single variable:

$$A(x) = x(3 - x^2)$$

$$A(x) = 3x - x^3$$

**Step 2: Find the first derivative**
To find the maximum area, take the derivative of the area function with respect to $x$.

$$A'(x) = 3 - 3x^2$$

**Step 3: Set the derivative to zero and solve for $x$**
Critical points occur where the derivative is zero.

$$3 - 3x^2 = 0$$

$$3x^2 = 3$$

$$x^2 = 1$$

$$x = 1$$

_(We only take the positive root because the rectangle is in the first quadrant)_

_Note: You can verify this is a maximum by taking the second derivative ($A''(x) = -6x$). Since $A''(1) = -6$, which is negative, the curve is concave down, confirming a maximum._

**Step 4: Find the corresponding $y$-value**
Plug the $x$-value back into the original curve equation to find the height.

$$y = 3 - (1)^2$$

$$y = 3 - 1$$

$$y = 2$$

**Final Answer:**
The dimensions of the rectangle with the maximum area are a **width of $1$** and a **height of $2$**.

---

Would you like to continue with more optimization problems, or is there another topic you want to cover?
