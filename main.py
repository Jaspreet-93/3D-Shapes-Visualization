import tkinter as tk
from tkinter import ttk, messagebox
from solver import calculate
from visualizer import visualize

# Function called on button click
def solve_shape(shape):
    try:
        v1 = float(entry1.get()) if entry1.get() else 0
        v2 = float(entry2.get()) if entry2.get() else 0
        v3 = float(entry3.get()) if entry3.get() else 0

        if shape in ["Cube", "Sphere", "Hemisphere"]:
            args = (v1,)
        elif shape in ["Cylinder", "Cone", "Square Pyramid"]:
            args = (v1, v2)
        elif shape == "Rectangular Prism":
            args = (v1, v2, v3)
        else:
            args = (v1, v2, v3)

        result = calculate(shape, *args)
        if result:
            visualize(shape, *args)
            messagebox.showinfo(
                "Result",
                f"{shape}\n\nFormula: {result['formula']}\n"
                f"Volume = {round(result['volume'], 2)}\n"
                f"Surface Area = {round(result['surface'], 2)}\n\n"
                f"Example: {result['example']}"
            )
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def reset():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)

# Main Window
root = tk.Tk()
root.title("3D Shapes Explorer & Solver")
root.geometry("1000x600")
root.configure(bg="#f0f2f5")

# Main layout: Left Panel (inputs) | Right Panel (visualization)
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# ================= LEFT PANEL =================
left_frame = tk.Frame(root, bg="#ffffff", bd=2, relief="groove")
left_frame.grid(row=0, column=0, sticky="nswe", padx=10, pady=10)
left_frame.grid_rowconfigure(6, weight=1)

title = tk.Label(left_frame, text="Shape Input Panel", font=("Arial", 16, "bold"), bg="white", fg="#333")
title.pack(pady=10)

# Input fields
tk.Label(left_frame, text="Value 1 (Side/Radius/Length):", bg="white", anchor="w").pack(fill="x", padx=10)
entry1 = ttk.Entry(left_frame)
entry1.pack(fill="x", padx=10, pady=5)

tk.Label(left_frame, text="Value 2 (Height/Width):", bg="white", anchor="w").pack(fill="x", padx=10)
entry2 = ttk.Entry(left_frame)
entry2.pack(fill="x", padx=10, pady=5)

tk.Label(left_frame, text="Value 3 (Breadth if needed):", bg="white", anchor="w").pack(fill="x", padx=10)
entry3 = ttk.Entry(left_frame)
entry3.pack(fill="x", padx=10, pady=5)

# Shape Buttons
button_frame = tk.LabelFrame(left_frame, text="Choose Shape", bg="white", fg="#444")
button_frame.pack(fill="both", expand=True, padx=10, pady=10)

shapes = ["Cube", "Sphere", "Cylinder", "Cone", "Square Pyramid", "Rectangular Prism", "Hemisphere"]
for s in shapes:
    ttk.Button(button_frame, text=s, command=lambda shape=s: solve_shape(shape)).pack(fill="x", pady=3, padx=10)

# Reset button
ttk.Button(left_frame, text="Reset", command=reset).pack(pady=10)

# ================= RIGHT PANEL =================
right_frame = tk.Frame(root, bg="#e9ecef", bd=2, relief="groove")
right_frame.grid(row=0, column=1, sticky="nswe", padx=10, pady=10)

right_label = tk.Label(right_frame, text="3D Visualization Area", font=("Arial", 16, "bold"), bg="#e9ecef", fg="#222")
right_label.pack(pady=20)

# Placeholder for visualization
canvas = tk.Canvas(right_frame, bg="white")
canvas.pack(fill="both", expand=True, padx=20, pady=20)

# Run App
root.mainloop()
