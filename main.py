import tkinter as tk
import re
import tkinter.messagebox
import webbrowser

root = tk.Tk()

root.title("My GUI Program")

root.geometry("400x400")

label = tk.Label(root, text="Enter domain:")
label.grid(row=0, column=0)

entry = tk.Entry(root)
entry.grid(row=0, column=1)


def submit():
    domain = entry.get()
    if re.match("^[a-z]+://[^\s]+", domain):
        webbrowser.open(domain)
    else:
        tk.messagebox.showerror("Error", "Invalid domain address.")


submit = tk.Button(root, text="Submit", command=submit)
submit.grid(row=1, column=1)

root.mainloop()