import tkinter as tk


class App:
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.temp_value = tk.DoubleVar(master, 0.0)
        self.format_value = tk.IntVar(master, 0)
        self.calc_on_return = tk.BooleanVar(master, True)
        self.calc_on_return.trace("w", self.bind_calc_on_return)

        temp_frame = tk.Frame(self.master)
        temp_frame.pack()
        self.temp_label = tk.Label(temp_frame, text="Temperature:")
        self.temp_label.pack(side="left")
        self.temp_entry = tk.Entry(temp_frame, textvariable=self.temp_value)
        self.temp_entry.bind("<Return>", self.convert_temp)
        self.temp_entry.pack(side="right")

        format_frame = tk.Frame(self.master)
        format_frame.pack()
        self.format_label = tk.Label(format_frame, text="Output Format:")
        self.format_label.pack(side="left")

        radio_frame = tk.Frame(format_frame)
        radio_frame.pack(side="right")

        self.format_celcius = tk.Radiobutton(
            radio_frame, variable=self.format_value, text="Celsius", value=0
        )
        self.format_celcius.pack(side="left")
        self.format_fahr = tk.Radiobutton(
            radio_frame, variable=self.format_value, text="Fahrenheit", value=1
        )
        self.format_fahr.pack(side="left")

        calc_on_return_checkbox = tk.Checkbutton(
            self.master, text="Calculate on Return/Enter", variable=self.calc_on_return,
        )
        calc_on_return_checkbox.pack()

        self.button = tk.Button(
            self.master, text="Calculate", command=self.convert_temp
        )
        self.button.pack()

        self.results = tk.Label(self.master)
        self.results.pack()

    def start(self):
        self.master.mainloop()

    def convert_temp(self, event=None):
        try:
            input_value = self.temp_value.get()
        except tk.TclError:
            self.results["text"] = "Invalid temperature value"
        else:
            if self.format_value.get() == 0:
                # Convert to Celsius
                self.results["text"] = f"{round((input_value - 32) * 5 / 9, 2)}ºC"
            else:
                # Convert to Fahrenheit
                self.results["text"] = f"{round(input_value * 9 / 5 + 32, 2)}ºF"

    def bind_calc_on_return(self, *args):
        if self.calc_on_return.get():
            self.temp_entry.bind("<Return>", self.convert_temp)
        else:
            self.temp_entry.unbind("<Return>")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    app.start()
