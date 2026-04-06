### Problem 11: Animation: Two-Slit Interference

**Given:**
* The resultant wave equation for two coherent point sources (slits):
  $$u(\vec{r},t) = \frac{A}{|\vec{r}-\vec{r_1}|} \sin(k |\vec{r} - \vec{r_1}| - \omega t) + \frac{A}{|\vec{r}-\vec{r_2}|} \sin(k |\vec{r} - \vec{r_2}| - \omega t)$$
* $\vec{r_1}$ and $\vec{r_2}$ are the positions of the two slits.
* Slit separation: $d = |\vec{r_1} - \vec{r_2}|$
* Wavelength: $\lambda$ (related to wave number by $k = \frac{2\pi}{\lambda}$)

**Goal:** Write an interactive HTML/JS animation simulating Young's double-slit experiment where the user can adjust $d$ and $\lambda$.

**Implementation Details:**
The code below uses an HTML5 Canvas to render the interference pattern. It calculates the physical distance from every pixel on the screen to both slit positions, computes the trigonometric wave sum defined by your equation, and maps that scalar value to a visible color intensity. Sliders dynamically update the state variables without pausing the animation.

Save the following code as an `.html` file and open it in a web browser to view the interactive simulation.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Two-Slit Interference Simulation</title>
    <style>
        body { 
            font-family: sans-serif; 
            display: flex; 
            flex-direction: column; 
            align-items: center; 
            background-color: #111; 
            color: #eee;
            margin-top: 20px;
        }
        .controls { 
            background: #222; 
            padding: 15px 30px; 
            border-radius: 8px; 
            box-shadow: 0 4px 10px rgba(0,0,0,0.5);
            text-align: center;
            margin-bottom: 20px;
        }
        /* Internal resolution is 300x300, displayed at 600x600 for performance */
        canvas { 
            background: #000; 
            box-shadow: 0 0 20px rgba(0,0,0,0.8); 
            width: 600px; 
            height: 600px; 
            image-rendering: pixelated;
            border-radius: 4px;
        }
        input[type="range"] { width: 200px; margin: 5px 15px; vertical-align: middle;}
        .val-display { display: inline-block; width: 30px; font-weight: bold; color: #4facfe; }
    </style>
</head>
<body>
    <div class="controls">
        <h2>Young's Double-Slit Experiment</h2>
        
        <label for="dSlider">Slit Separation ($d$): </label>
        <input type="range" id="dSlider" min="10" max="150" step="2" value="40">
        <span class="val-display" id="dVal">40</span><br>
        
        <label for="wSlider">Wavelength (&lambda;): </label>
        <input type="range" id="wSlider" min="4" max="40" step="1" value="15">
        <span class="val-display" id="wVal">15</span>
    </div>
    
    <canvas id="slitCanvas" width="300" height="300"></canvas>
    
    <script>
        const canvas = document.getElementById('slitCanvas');
        const ctx = canvas.getContext('2d');
        const dSlider = document.getElementById('dSlider');
        const dVal = document.getElementById('dVal');
        const wSlider = document.getElementById('wSlider');
        const wVal = document.getElementById('wVal');

        let time = 0;
        const A = 25;       // Base amplitude scalar
        const omega = 0.8;  // Angular frequency (speed of animation)
        const slitX = 20;   // X-coordinate for both slits (placed on the left side)

        // Event listeners to update UI labels
        dSlider.addEventListener('input', () => dVal.innerText = dSlider.value);
        wSlider.addEventListener('input', () => wVal.innerText = wSlider.value);

        function render() {
            const width = canvas.width;
            const height = canvas.height;
            const imgData = ctx.createImageData(width, height);
            const data = imgData.data;
            
            // Read interactive parameters
            const d = parseFloat(dSlider.value);
            const lambda = parseFloat(wSlider.value);
            const k = (2 * Math.PI) / lambda;

            // Define slit vectors based on separation distance d
            const centerY = height / 2;
            const r1 = { x: slitX, y: centerY - d / 2 };
            const r2 = { x: slitX, y: centerY + d / 2 };

            // Render wave intensities per pixel
            for (let y = 0; y < height; y++) {
                for (let x = 0; x < width; x++) {
                    // Distance from current pixel to slit 1 and slit 2
                    let dist1 = Math.sqrt((x - r1.x)**2 + (y - r1.y)**2);
                    let dist2 = Math.sqrt((x - r2.x)**2 + (y - r2.y)**2);
                    
                    // Prevent division by zero at the exact slit coordinates
                    if (dist1 < 0.1) dist1 = 0.1;
                    if (dist2 < 0.1) dist2 = 0.1;
                    
                    // Calculate wave displacement equations
                    let u1 = (A / dist1) * Math.sin(k * dist1 - omega * time);
                    let u2 = (A / dist2) * Math.sin(k * dist2 - omega * time);
                    
                    // Superposition principle
                    let uTotal = u1 + u2;

                    // Map displacement (-1 to 1) to color intensity (0 to 255)
                    let intensity = Math.max(0, Math.min(255, 128 + uTotal * 120));
                    
                    const index = (y * width + x) * 4;
                    // Tint the waves a vibrant cyan/blue color
                    data[index] = intensity * 0.1;       // R
                    data[index+1] = intensity * 0.6;     // G
                    data[index+2] = intensity;           // B
                    data[index+3] = 255;                 // Alpha
                }
            }
            
            // Explicitly draw the slits as bright white markers
            for(let i = -2; i <= 2; i++) {
                let idx1 = (Math.floor(r1.y + i) * width + r1.x) * 4;
                let idx2 = (Math.floor(r2.y + i) * width + r2.x) * 4;
                if (data[idx1] !== undefined) {
                    data[idx1] = data[idx1+1] = data[idx1+2] = 255; // Slit 1
                }
                if (data[idx2] !== undefined) {
                    data[idx2] = data[idx2+1] = data[idx2+2] = 255; // Slit 2
                }
            }

            ctx.putImageData(imgData, 0, 0);
            
            time += 0.5;
            requestAnimationFrame(render);
        }
        
        render();
    </script>
</body>
</html>
```
