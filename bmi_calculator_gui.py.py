import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

        label_result.config(text=f"BMI: {bmi:.2f} ({category})")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# GUI setup
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x150")  # Optional: set window size

# Labels and input fields
tk.Label(root, text="Weight (kg):").grid(row=0, column=0, padx=10, pady=5)
entry_weight = tk.Entry(root)
entry_weight.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Height (m):").grid(row=1, column=0, padx=10, pady=5)
entry_height = tk.Entry(root)
entry_height.grid(row=1, column=1, padx=10, pady=5)

# Button
tk.Button(root, text="Calculate BMI", command=calculate_bmi).grid(row=2, column=0, columnspan=2, pady=10)

# Result label
label_result = tk.Label(root, text="", font=("Arial", 12))
label_result.grid(row=3, column=0, columnspan=2)

root.mainloop()