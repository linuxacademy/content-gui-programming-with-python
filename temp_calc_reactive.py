import tkinter as tk


class App:
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.temp_value = tk.DoubleVar(master)
        self.format_value = tk.IntVar(master)
        self.result_value = tk.StringVar(master)

        self.temp_value.trace("w", self.convert_temp)
        self.format_value.trace("w", self.convert_temp)

        temp_frame = tk.Frame(self.master)
        temp_frame.pack()
        self.temp_label = tk.Label(temp_frame, text="Temperature:")
        self.temp_label.pack(side="left")
        self.temp_entry = tk.Entry(temp_frame, textvariable=self.temp_value)
        self.temp_entry.pack(side="right")

        format_frame = tk.Frame(self.master)
        format_frame.pack()
        self.format_label = tk.Label(format_frame, text="Output Format:")
        self.format_label.pack(side="left")

        radio_frame = tk.Frame(format_frame)
        radio_frame.pack(side="right")

        self.format_celsius = tk.Radiobutton(
            radio_frame, variable=self.format_value, text="Celsius", value=0
        )
        self.format_celsius.pack(side="left")
        self.format_fahr = tk.Radiobutton(
            radio_frame, variable=self.format_value, text="Fahrenheit", value=1
        )
        self.format_fahr.pack(side="left")

        self.results = tk.Label(self.master, textvariable=self.result_value)
        self.results.pack()

        self.convert_temp()

    def start(self):
        self.master.mainloop()

    def convert_temp(self, *args):
        try:
            input_value = self.temp_value.get()
        except tk.TclError:
            self.result_value.set("Invalid temperature value")
        else:
            if self.format_value.get() == 0:
                # Convert to Celsius
                self.result_value.set(f"{round((input_value - 32) * 5 / 9, 2)}ºC")
            else:
                # Convert to Fahrenheit
                self.result_value.set(f"{round(input_value * 9 / 5 + 32, 2)}ºF")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    app.start()
