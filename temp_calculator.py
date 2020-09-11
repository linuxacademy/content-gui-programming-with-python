import tkinter as tk


class App:
    def __init__(self, master):
        super().__init__()
        self.master = master

        temp_frame = tk.Frame(self.master)
        temp_frame.pack()
        self.temp_label = tk.Label(temp_frame, text="Temperature:")
        self.temp_label.pack(side="left")
        self.temp_entry = tk.Entry(temp_frame)
        self.temp_entry.pack(side="right")

        format_frame = tk.Frame(self.master)
        format_frame.pack()
        self.format_label = tk.Label(format_frame, text="Output Format:")
        self.format_label.pack(side="left")

        radio_frame = tk.Frame(format_frame)
        radio_frame.pack(side="right")

        self.format_celsius = tk.Radiobutton(radio_frame, text="Celsius")
        self.format_celsius.pack(side="left")
        self.format_fahr = tk.Radiobutton(radio_frame, text="Fahrenheit")
        self.format_fahr.pack(side="left")

        self.button = tk.Button(self.master, text="Calculate")
        self.button.pack()

        self.results = tk.Label(self.master, text="")
        self.results.pack()

    def start(self):
        self.master.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    app.start()
