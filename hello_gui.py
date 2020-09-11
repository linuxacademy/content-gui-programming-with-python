import tkinter as tk

# Global Greeting Count
greeting_count = 1

# Create Application, Label, and Button
root = tk.Tk()
label = tk.Label(root, text="")

# Define a command to run on button click
def set_message():
    global greeting_count
    label["text"] = f"Hello! ({greeting_count})"
    greeting_count += 1


button = tk.Button(root, text="Greet", command=set_message)

# Add widgets to application to display.
button.pack()
label.pack()

# Start the GUI application.
root.mainloop()
