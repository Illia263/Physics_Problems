### Problem 10: Animation: Wave Sources

**Given:**
* The wave equation for a point source:
  $$u(\vec{r},t) = \frac{A}{|\vec{r}-\vec{r_0}|^\alpha} \sin(k |\vec{r} - \vec{r_0}| - \omega t)$$
* $\vec{r_0}$ is the dot position.
* $\alpha$ is an adjustable parameter in the range $[0, 2]$.
* The resulting displacement is the superposition (sum) of all active sources.

**Goal:** Write an interactive HTML/JS animation.

**Implementation Details:**
The following code creates a canvas where every pixel's intensity is calculated based on its distance to all placed sources. It uses the `ImageData` API for pixel-level manipulation to ensure the animation runs smoothly. The mathematical superposition is calculated by summing the $u$ value for each wave source at every $(x,y)$ coordinate.

Save the code below as an `.html` file and open it in a web browser. Click anywhere on the black canvas to drop a wave source. 

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wave Sources Superposition</title>
    <style>
        body { 
            font-family: sans-serif; 
            display: flex; 
            flex-direction: column; 
            align-items: center; 
            background-color: #1a1a1a; 
            color: #fff;
            margin-top: 20px;
        }
        .controls { 
            margin-bottom: 15px; 
            background: #2a2a2a; 
            padding: 15px; 
            border-radius: 8px; 
            box-shadow: 0 4px 6px rgba(0,0,0,0.3);
            text-align: center;
        }
        /* The canvas is scaled up via CSS for performance. 
           Internal resolution is 250x250, displayed at 500x500 */
        canvas { 
            background: #000; 
            box-shadow: 0 0 15px rgba(0,0,0,0.5); 
            cursor: crosshair;
            width: 500px; 
            height: 500px; 
            image-rendering: pixelated;
            border-radius: 4px;
        }
        input[type="range"] { width: 250px; }
    </style>
</head>
<body>
    <div class="controls">
        <h2>Interactive Wave Sources</h2>
        <p>Click on the canvas below to place wave sources.</p>
        <label for="alphaSlider"><strong>Attenuation Parameter (&alpha;): </strong><span id="alphaVal">0.5</span></label><br>
        <input type="range" id="alphaSlider" min="0" max="2" step="0.1" value="0.5">
        <br><br>
        <button onclick="clearSources()" style="padding: 5px 15px; cursor: pointer;">Clear Sources</button>
    </div>
    
    <canvas id="waveCanvas" width="250" height="250"></canvas>
    
    <script>
        const canvas = document.getElementById('waveCanvas');
        const ctx = canvas.getContext('2d');
        const alphaSlider = document.getElementById('alphaSlider');
        const alphaVal = document.getElementById('alphaVal');

        let sources = [];
        let time = 0;
        
        // Wave properties
        const A = 15;        // Amplitude scalar
        const k = 0.3;       // Wave number (spatial frequency)
        const omega = 0.5;   // Angular frequency (temporal speed)

        // Listen for clicks to add sources
        canvas.addEventListener('mousedown', (e) => {
            const rect = canvas.getBoundingClientRect();
            // Map the mouse coordinates to the internal canvas resolution
            const scaleX = canvas.width / rect.width;
            const scaleY = canvas.height / rect.height;
            sources.push({
                x: (e.clientX - rect.left) * scaleX,
                y: (e.clientY - rect.top) * scaleY
            });
        });

        // Update slider label
        alphaSlider.addEventListener('input', () => {
            alphaVal.innerText = parseFloat(alphaSlider.value).toFixed(1);
        });

        // Clear button functionality
        function clearSources() {
            sources = [];
        }

        // Main rendering loop
        function render() {
            const width = canvas.width;
            const height = canvas.height;
            const imgData = ctx.createImageData(width, height);
            const data = imgData.data;
            const alpha = parseFloat(alphaSlider.value);

            // Calculate wave amplitude for every pixel
            for (let y = 0; y < height; y++) {
                for (let x = 0; x < width; x++) {
                    let uTotal = 0;
                    
                    // Superposition: Sum the contribution from all sources
                    for (let s of sources) {
                        const dx = x - s.x;
                        const dy = y - s.y;
                        let r = Math.sqrt(dx*dx + dy*dy);
                        if (r < 0.1) r = 0.1; // Prevent division by zero
                        
                        uTotal += (A / Math.pow(r, alpha)) * Math.sin(k * r - omega * time);
                    }
                    
                    // Map the mathematical amplitude uTotal (-1 to 1 roughly) to an RGB color (0-255)
                    // Base brightness is 128 (gray), waves swing it to white (255) or black (0)
                    let intensity = Math.max(0, Math.min(255, 128 + uTotal * 40));
                    
                    const index = (y * width + x) * 4;
                    // Draw in a monochromatic blue-ish steel color
                    data[index] = intensity * 0.8;       // Red
                    data[index+1] = intensity * 0.9;     // Green
                    data[index+2] = intensity;           // Blue
                    data[index+3] = 255;                 // Alpha (Opaque)
                }
            }
            
            // Push pixel data to canvas
            ctx.putImageData(imgData, 0, 0);
            
            // Advance time and request next frame
            time += 0.5;
            requestAnimationFrame(render);
        }
        
        // Start animation loop
        render();
    </script>
</body>
</html>
```
