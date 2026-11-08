import tkinter as tk
import secrets
import string

root = tk.Tk()
root.title("Password Generator")
root.geometry("480x540")
root.resizable(False, False)
root.configure(bg="#f5f5f0")

length = tk.IntVar(value=16)

def generate():
    pool = string.ascii_letters + string.digits + "!@#$%^&*()-_=+?{}[]|\;:,.<>/"
    password = ''.join(secrets.choice(pool) for _ in range(length.get()))

    result.config(state="normal")
    result.delete(0, tk.END)
    result.insert(0, password)
    result.config(state="readonly")

    update_strength(password)

def update_strength(password):
    score = sum([
        len(password) >= 12,
        len(password) >=16,
        any(c.islower() for c in password),
        any(c.isupper() for c in password),
        any(c.isdigit() for c in password),
        any(c in "!@#$%^&*()-_=+?{}[]|\;:,.<>/" for c in password)
    ])

    if score <=2:
        strength.config(text="Weak", fg="#c65d5d")
    elif score <= 4:
        strength.config(text="Moderate", fg="#c49a43")
    else:
        strength.config(text="Strong", fg="#52796f")

def copy():
    password = result.get()

    if not password:
        return

    root.clipboard_clear()
    root.clipboard_append(password)
    copy_btn.config(text="Copied!!")
    root.after(1200, lambda: copy_btn.config(text="Copy"))

tk.Label(
    root,
    text="Password Generator",
    font=("Segoe UI", 22, "bold"),
    bg="#f5f5f0",
    fg="#252a28"
).pack(pady=(35, 5))

tk.Label(
    root,
    text="Generate a secure random password",
    font=("Segoes UI", 10),
    bg="#f5f5f0",
    fg="#858b87"
).pack(pady=(0, 25))

card = tk.Frame(
    root,
    bg="#ffffff",
    highlightbackground="#e5e8e4",
    highlightthickness=1
)
card.pack(fill="x", padx=30, pady=5)

tk.Label(
    card,
    text="YOUR PASSWORD",
    font=("Segoe UI", 9, "bold"),
    bg="#ffffff",
    fg="#858b87"
).pack(anchor="w", padx=20, pady=(20, 8))

result = tk.Entry(
    card,
    font=("Consolas", 15),
    bg="#e8f0ec",
    fg="#252a28",
    justify="center",
    relief="flat",
    readonlybackground="#e8f0ec"
)
result.pack(fill="x", padx=20, ipady=12)
result.config(state="readonly")

strength = tk.Label(
    card,
    text="Not generated",
    font=("Segoe UI", 10, "bold"),
    bg="#ffffff",
    fg="#858b87"
)
strength.pack(pady=15)

tk.Button(
    card,
    text="Generate Password",
    command=generate,
    bg="#52796f",
    fg="#ffffff",
    activebackground="#43675E",
    activeforeground="#ffffff",
    font=("Segoe UI", 10, "bold"),
    relief="flat",
    cursor="hand2",
    pady=10
).pack(fill="x", padx=20, pady=(0, 10))

copy_btn = tk.Button(
    card,
    text="Copy",
    command=copy,
    bg="#e8f0ec",
    fg="#52796f",
    activebackground="#dce9e1",
    font=("Segoe UI", 10, "bold"),
    relief="flat",
    cursor="hand2",
    pady=9
)
copy_btn.pack(fill="x", padx=20, pady=(0, 20))

settings = tk.Frame(root, bg="#f5f5f0")
settings.pack(fill="x", padx=45, pady=20)

tk.Label(
    settings,
    text="Password Length",
    font=("Segoe UI", 10, "bold"),
    bg="#f5f5f0",
    fg="#252a28"
).pack(anchor="w")

tk.Scale(
    settings,
    from_=4,
    to=64,
    variable=length,
    orient="horizontal",
    bg="#f5f5f0",
    fg="#252a28",
    troughcolor="#dce5df",
    activebackground="#52796f",
    highlightthickness=0,
    showvalue=True,
    font=("Segoe UI", 10),
    length=350,
    sliderlength=25,
    width=15
).pack(fill="x")

root.mainloop()