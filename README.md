# 3D Shapes Explorer & Solver

An interactive desktop application built using Python, Tkinter, and VPython. This application serves as an educational tool to calculate the Volume and Surface Area of various 3D geometric shapes, display real-world examples, and render an interactive, fully-realized 3D visualization.

---

## 🚀 Features

*   **Comprehensive Solver:** Calculate Volume and Surface Area for 7 different 3D shapes.
*   **Interactive 3D Visualization:** Render shapes in real-time on a WebGL-based canvas.
*   **Dynamic Controls:** Pan, zoom, and rotate the camera using mouse gestures.
*   **Keyboard Controls:** Move the rendered 3D objects along the X, Y, and Z axes in real-time.
*   **Real-world Context:** Shows typical real-world examples of each shape (e.g., Rubik's Cube for Cube, Egyptian Pyramid for Square Pyramid).

---

## 🛠️ Project Structure

The project is structured logically across modular Python files:

*   **[main.py](file:///d:/PROJECTS/3d%20shapes/main.py):** The primary entry point. Coordinates the Tkinter GUI, user input handling, and links the calculation solver with the 3D visualizer.
*   **[solver.py](file:///d:/PROJECTS/3d%20shapes/solver.py):** Implements the mathematical formulas to calculate volume and surface area for each shape, and provides real-world example mappings.
*   **[visualizer.py](file:///d:/PROJECTS/3d%20shapes/visualizer.py):** Controls the VPython-based 3D scene, registers event listeners, and handles shape rendering and keyboard movement.
*   **[utils.py](file:///d:/PROJECTS/3d%20shapes/utils.py):** Contains utility helper functions, such as random RGB color vector generation for the shapes.

---

## 📐 Supported Shapes & Formulas

| Shape | Volume Formula | Surface Area Formula | Example |
| :--- | :--- | :--- | :--- |
| **Cube** | $V = a^3$ | $SA = 6a^2$ | Rubik's Cube, Dice |
| **Sphere** | $V = \frac{4}{3}\pi r^3$ | $SA = 4\pi r^2$ | Football, Ball |
| **Cylinder** | $V = \pi r^2 h$ | $SA = 2\pi r(h+r)$ | Water Tank, Candle |
| **Cone** | $V = \frac{1}{3}\pi r^2 h$ | $SA = \pi r(r + \sqrt{r^2+h^2})$ | Ice Cream Cone |
| **Square Pyramid** | $V = \frac{1}{3}a^2 h$ | $SA = a^2 + 2a\sqrt{(\frac{a}{2})^2 + h^2}$ | Egyptian Pyramid |
| **Rectangular Prism** | $V = l \cdot w \cdot h$ | $SA = 2(lw + wh + lh)$ | Bricks, Boxes |
| **Hemisphere** | $V = \frac{2}{3}\pi r^3$ | $SA = 3\pi r^2$ | Dome |

---

## 💻 Installation & Setup

### Prerequisites

*   Python 3.8 or higher.
*   Pip (Python Package Installer).

### Steps

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Jaspreet-93/3D-Shapes-Visualization.git
    cd 3D-Shapes-Visualization
    ```

2.  **Install dependencies:**
    This project requires `vpython` for 3D visualization. Tkinter comes pre-installed with standard Python distributions.
    ```bash
    pip install vpython
    ```

3.  **Run the application:**
    ```bash
    python main.py
    ```

---

## 🎮 How to Use & Controls

1.  Enter the required dimensions in the left **Shape Input Panel** (only the parameters required for your chosen shape need to be filled).
2.  Click the button corresponding to your shape (e.g., **Cube**).
3.  A calculation results modal will pop up, and a VPython interactive canvas will open in your default web browser displaying the shape.

### Camera Controls (Mouse)
*   **Rotate:** Left-click and drag.
*   **Zoom:** Scroll the mouse wheel up/down.
*   **Pan:** Right-click and drag.

### Object Movement (Keyboard)
Click on the browser canvas to focus, then use these keys to move the shape:
*   `A` / `D` or `Left Arrow` / `Right Arrow`: Move Left / Right (X-axis)
*   `R` / `F`: Move Up / Down (Y-axis)
*   `W` / `S` or `Up Arrow` / `Down Arrow`: Move Forward / Backward (Z-axis)
*   `Shift` (Hold): Speed up movement
*   `Spacebar`: Reset the object's position to the origin $(0, 0, 0)$
