import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("My First Tkinter App")

# Add a label widget
label = tk.Label(root, text="Hello, Tkinter!")
label.pack(padx=20, pady=20)

# Add a button widget
button = tk.Button(root, text="Click Me", command=root.quit)
button.pack(pady=10)

# Start the event loop
root.mainloop()
