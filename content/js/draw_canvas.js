const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
const strokeColorInput = document.getElementById('stroke-color');
const fillColorInput = document.getElementById('fill-color');

// Set canvas size
canvas.width = 600;
canvas.height = 400;

let drawing = false;

// Set initial context properties
ctx.lineWidth = 5;
ctx.strokeStyle = strokeColorInput.value;
ctx.fillStyle = fillColorInput.value;

// Update stroke color when input changes
strokeColorInput.addEventListener('change', (e) => {
    ctx.strokeStyle = e.target.value;
});

// Update fill color when input changes
fillColorInput.addEventListener('change', (e) => {
    ctx.fillStyle = e.target.value;
});

// Get canvas coordinates
function getCanvasCoordinates(e) {
    const rect = canvas.getBoundingClientRect();
    const scaleX = canvas.width / rect.width;
    const scaleY = canvas.height / rect.height;
    return {
        x: (e.clientX - rect.left) * scaleX,
        y: (e.clientY - rect.top) * scaleY,
    };
}

// Event listeners
canvas.addEventListener('mousedown', (e) => {
    drawing = true;
    const coords = getCanvasCoordinates(e);
    ctx.beginPath();
    ctx.moveTo(coords.x, coords.y);
});

canvas.addEventListener('mousemove', (e) => {
    if (!drawing) return;
    const coords = getCanvasCoordinates(e);

    // Draw the filled rectangle (body of the line)
    ctx.fillStyle = fillColorInput.value;
    ctx.fillRect(coords.x - ctx.lineWidth / 2, coords.y - ctx.lineWidth / 2, ctx.lineWidth, ctx.lineWidth);

    // Draw the border around the rectangle
    ctx.strokeStyle = strokeColorInput.value;
    ctx.strokeRect(coords.x - ctx.lineWidth / 2, coords.y - ctx.lineWidth / 2, ctx.lineWidth, ctx.lineWidth);
});

canvas.addEventListener('mouseup', () => {
    drawing = false;
});

canvas.addEventListener('mouseleave', () => {
    drawing = false;
});
