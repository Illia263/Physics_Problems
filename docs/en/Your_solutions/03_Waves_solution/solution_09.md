### Problem 9: Damped Oscillator

**Given:**
The differential equation for a damped harmonic oscillator:
$$m \frac{d^2 x}{dt^2} + b \frac{dx}{dt} + k x = 0$$

#### 1. General Solution & 2. Classification of Cases
To solve this linear homogeneous differential equation, we assume a solution of the form $x(t) = e^{rt}$. Substituting this into the equation gives the characteristic equation:
$$mr^2 + br + k = 0$$
The roots are:
$$r_{1,2} = \frac{-b \pm \sqrt{b^2 - 4mk}}{2m}$$

We define the damping coefficient $\gamma = \frac{b}{2m}$ and the natural angular frequency $\omega_0 = \sqrt{\frac{k}{m}}$. The system's behavior depends on the discriminant ($b^2 - 4mk$):

* **Underdamped ($b^2 < 4mk$):** The roots are complex. The system oscillates with a decaying amplitude.
    $$x(t) = A e^{-\gamma t} \cos(\omega_d t + \phi)$$
    where $\omega_d = \sqrt{\omega_0^2 - \gamma^2}$ is the damped frequency.
* **Critically Damped ($b^2 = 4mk$):** The roots are real and repeated ($r_1 = r_2 = -\gamma$). The system returns to equilibrium as fast as possible without oscillating.
    $$x(t) = (C_1 + C_2 t) e^{-\gamma t}$$
* **Overdamped ($b^2 > 4mk$):** The roots are real and distinct. The system slowly returns to equilibrium without oscillating.
    $$x(t) = C_1 e^{r_1 t} + C_2 e^{r_2 t}$$

#### 3-6. Numerical Solution (RK4), Interaction, and Graphs
Below is the interactive HTML/JavaScript code that numerically solves the equation using the 4th Order Runge-Kutta (RK4) method. It includes a slider to investigate the effect of the parameter $b$ and generates both the $x(t)$ graph and the phase portrait ($v$ vs $x$).

Save the following code block as an `.html` file and open it in any web browser to interact with the animation.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Damped Harmonic Oscillator Simulation</title>
    <style>
        body { font-family: sans-serif; display: flex; flex-direction: column; align-items: center; background-color: #f4f4f9; }
        .container { background: white; padding: 20px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); text-align: center; }
        canvas { border: 1px solid #ccc; background: #fff; margin: 10px; }
        .controls { margin-bottom: 20px; padding: 10px; background: #eef; border-radius: 8px; }
        input[type="range"] { width: 300px; }
        .status { font-weight: bold; font-size: 1.2em; margin-top: 10px; }
        .underdamped { color: #d9534f; }
        .critical { color: #5cb85c; }
        .overdamped { color: #0275d8; }
        .canvas-container { display: flex; flex-wrap: wrap; justify-content: center; }
    </style>
</head>
<body>
    <div class="container">
        <h2>Damped Harmonic Oscillator (RK4 Method)</h2>
        <div class="controls">
            <label for="b_slider"><strong>Damping Parameter (b): </strong><span id="b_val">1.00</span></label><br>
            <input type="range" id="b_slider" min="0" max="10" step="0.1" value="1.0"><br>
            <div id="status_text" class="status underdamped">Underdamped</div>
        </div>
        
        <div class="canvas-container">
            <div>
                <h3>Displacement x(t)</h3>
                <canvas id="timeCanvas" width="400" height="300"></canvas>
            </div>
            <div>
                <h3>Phase Portrait (v vs x)</h3>
                <canvas id="phaseCanvas" width="400" height="300"></canvas>
            </div>
        </div>
    </div>

    <script>
        const bSlider = document.getElementById('b_slider');
        const bVal = document.getElementById('b_val');
        const statusText = document.getElementById('status_text');
        const timeCtx = document.getElementById('timeCanvas').getContext('2d');
        const phaseCtx = document.getElementById('phaseCanvas').getContext('2d');

        // System parameters
        const m = 1.0;  // Mass
        const k = 10.0; // Spring constant
        const criticalB = Math.sqrt(4 * m * k); // Critical damping boundary

        // ODE defined as a system of first-order equations
        // state = [x, v]
        function derivatives(t, state, b) {
            const x = state[0];
            const v = state[1];
            const dxdt = v;
            const dvdt = (-b * v - k * x) / m;
            return [dxdt, dvdt];
        }

        // 4th Order Runge-Kutta numerical solver
        function rk4Step(dt, state, t, b) {
            const k1 = derivatives(t, state, b);
            const k2 = derivatives(t + dt/2, [state[0] + k1[0]*dt/2, state[1] + k1[1]*dt/2], b);
            const k3 = derivatives(t + dt/2, [state[0] + k2[0]*dt/2, state[1] + k2[1]*dt/2], b);
            const k4 = derivatives(t + dt, [state[0] + k3[0]*dt, state[1] + k3[1]*dt], b);
            
            return [
                state[0] + (dt/6) * (k1[0] + 2*k2[0] + 2*k3[0] + k4[0]),
                state[1] + (dt/6) * (k1[1] + 2*k2[1] + 2*k3[1] + k4[1])
            ];
        }

        function drawAxes(ctx, width, height, isPhase) {
            ctx.beginPath();
            ctx.strokeStyle = "#888";
            ctx.lineWidth = 1;
            // X-axis
            ctx.moveTo(0, height / 2);
            ctx.lineTo(width, height / 2);
            // Y-axis
            if (isPhase) {
                ctx.moveTo(width / 2, 0);
                ctx.lineTo(width / 2, height);
            } else {
                ctx.moveTo(20, 0);
                ctx.lineTo(20, height);
            }
            ctx.stroke();
        }

        function simulateAndDraw() {
            const b = parseFloat(bSlider.value);
            bVal.innerText = b.toFixed(2);
            
            // Update classification text and colors
            if (b < criticalB - 0.1) {
                statusText.innerText = "Underdamped (b² < 4mk)";
                statusText.className = "status underdamped";
            } else if (Math.abs(b - criticalB) <= 0.1) {
                statusText.innerText = "Critically Damped (b² ≈ 4mk)";
                statusText.className = "status critical";
            } else {
                statusText.innerText = "Overdamped (b² > 4mk)";
                statusText.className = "status overdamped";
            }

            // Initial conditions
            let state = [10.0, 0.0]; // Initial position x=10, velocity v=0
            let t = 0;
            const dt = 0.05;
            const steps = 400; // Total simulation steps
            
            const history = [];

            // Run numerical integration
            for(let i = 0; i < steps; i++) {
                history.push({t: t, x: state[0], v: state[1]});
                state = rk4Step(dt, state, t, b);
                t += dt;
            }

            // Clear canvases
            timeCtx.clearRect(0, 0, 400, 300);
            phaseCtx.clearRect(0, 0, 400, 300);

            drawAxes(timeCtx, 400, 300, false);
            drawAxes(phaseCtx, 400, 300, true);

            // Draw Time Graph x(t)
            timeCtx.beginPath();
            timeCtx.strokeStyle = "#d9534f";
            timeCtx.lineWidth = 2;
            for(let i = 0; i < history.length; i++) {
                const px = 20 + (history[i].t / (steps * dt)) * 360; // Scale time to width
                const py = 150 - (history[i].x * 12); // Scale x to height
                if(i === 0) timeCtx.moveTo(px, py);
                else timeCtx.lineTo(px, py);
            }
            timeCtx.stroke();

            // Draw Phase Portrait (v vs x)
            phaseCtx.beginPath();
            phaseCtx.strokeStyle = "#0275d8";
            phaseCtx.lineWidth = 2;
            for(let i = 0; i < history.length; i++) {
                const px = 200 + (history[i].x * 15); // Scale x to width centered
                const py = 150 - (history[i].v * 8);  // Scale v to height centered
                if(i === 0) phaseCtx.moveTo(px, py);
                else phaseCtx.lineTo(px, py);
            }
            phaseCtx.stroke();
        }

        bSlider.addEventListener('input', simulateAndDraw);
        
        // Initial render
        simulateAndDraw();
    </script>
</body>
</html>
```
