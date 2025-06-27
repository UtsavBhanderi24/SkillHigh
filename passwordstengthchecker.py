import tkinter as tk
import re
import math

def calculate_entropy(password):
    pool = 0
    if re.search(r'[a-z]', password): pool += 26
    if re.search(r'[A-Z]', password): pool += 26
    if re.search(r'\d', password): pool += 10
    if re.search(r'[\W_]', password): pool += 32  # Approx special chars
    entropy = len(password) * math.log2(pool) if pool else 0
    return round(entropy, 2)

def check_strength(password):
    length = len(password)
    entropy = calculate_entropy(password)

    score = 0
    if length >= 12: score += 2
    if re.search(r'[a-z]', password): score += 1
    if re.search(r'[A-Z]', password): score += 1
    if re.search(r'\d', password): score += 1
    if re.search(r'[\W_]', password): score += 1
    if entropy >= 60: score += 2
    elif entropy >= 40: score += 1

    if score <= 3:
        return f"Weak (Entropy: {entropy} bits)", "red"
    elif score <= 5:
        return f"Moderate (Entropy: {entropy} bits)", "orange"
    elif score == 6:
        return f"Strong (Entropy: {entropy} bits)", "green"
    else:
        return f"Very Strong (Entropy: {entropy} bits)", "darkgreen"

def on_check():
    pwd = entry.get()
    strength, color = check_strength(pwd)
    result_label.config(text=strength, fg=color)

# GUI setup
root = tk.Tk()
root.title("Password Strength Checker")

tk.Label(root, text="Enter your password:").pack(pady=5)
entry = tk.Entry(root, show="*", width=30)
entry.pack()

tk.Button(root, text="Check Strength", command=on_check).pack(pady=5)
result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=5)

root.mainloop()
