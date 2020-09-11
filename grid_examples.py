import tkinter as tk
import inspect
import sys

# Run the various example versions of the application by passing the example number
# to the script:
#
# Usage:
# python3 grid_examples.py [example_number]
#
# Example to run the first example:
# python3 grid_examples.py 1

root = tk.Tk()

root.minsize(550, 400)


def ipad_example(master):
    label1 = tk.Label(master, text="Label 1", bg="blue")
    label1.grid(ipadx=30, ipady=30)

    label2 = tk.Label(master, text="Label 2", bg="red")
    label2.grid(ipadx=30, ipady=30)

    label3 = tk.Label(master, text="Label 3", bg="green")
    label3.grid(ipadx=30, ipady=30)


def column_example1(master):
    label1 = tk.Label(master, text="Label 1", bg="blue")
    label1.grid(column=1, ipadx=30, ipady=30)

    label2 = tk.Label(master, text="Label 2", bg="red")
    label2.grid(column=1, ipadx=30, ipady=30)

    label3 = tk.Label(master, text="Label 3", bg="green")
    label3.grid(column=1, ipadx=30, ipady=30)


def column_example2(master):
    # Demonstrate that the row increments by default
    label1 = tk.Label(master, text="Label 1", bg="blue")
    label1.grid(column=1, ipadx=30, ipady=30)

    label2 = tk.Label(master, text="Label 2", bg="red")
    label2.grid(column=2, ipadx=30, ipady=30)

    label3 = tk.Label(master, text="Label 3", bg="green")
    label3.grid(column=3, ipadx=30, ipady=30)


def row_example1(master):
    label1 = tk.Label(master, text="Label 1", bg="blue")
    label1.grid(column=1, row=1, ipadx=30, ipady=30)

    label2 = tk.Label(master, text="Label 2", bg="red")
    label2.grid(column=2, row=1, ipadx=30, ipady=30)

    label3 = tk.Label(master, text="Label 3", bg="green")
    label3.grid(column=3, row=1, ipadx=30, ipady=30)


def row_example2(master):
    label1 = tk.Label(master, text="Label 1", bg="blue")
    label1.grid(column=1, row=1, ipadx=30, ipady=30)

    label2 = tk.Label(master, text="Label 2", bg="red")
    label2.grid(column=2, row=3, ipadx=30, ipady=30)

    label3 = tk.Label(master, text="Label 3", bg="green")
    label3.grid(column=3, row=1, ipadx=30, ipady=30)


def columnspan_example1(master):
    label1 = tk.Label(master, text="Label 1", bg="blue")
    label1.grid(column=1, row=1, ipadx=30, ipady=30)

    label2 = tk.Label(master, text="Label 2", bg="red")
    label2.grid(column=1, columnspan=3, row=2, ipadx=30, ipady=30)

    label3 = tk.Label(master, text="Label 3", bg="green")
    label3.grid(column=3, row=1, ipadx=30, ipady=30)


def sticky_example1(master):
    label1 = tk.Label(master, text="Label 1", bg="blue")
    label1.grid(column=1, row=1, ipadx=30, ipady=30)

    label2 = tk.Label(master, text="Label 2", bg="red")
    label2.grid(sticky=tk.E, column=1, columnspan=3, row=2, ipadx=30, ipady=30)

    label3 = tk.Label(master, text="Label 3", bg="green")
    label3.grid(column=3, row=1, ipadx=30, ipady=30)


def sticky_example2(master):
    label1 = tk.Label(master, text="Label 1", bg="blue")
    label1.grid(column=1, row=1, ipadx=30, ipady=30)

    label2 = tk.Label(master, text="Label 2", bg="red")
    label2.grid(sticky=tk.E + tk.W, column=1, columnspan=3, row=2, ipadx=30, ipady=30)

    label3 = tk.Label(master, text="Label 3", bg="green")
    label3.grid(column=3, row=1, ipadx=30, ipady=30)


def rowspan_example(master):
    label1 = tk.Label(master, text="Label 1", bg="blue")
    label1.grid(column=1, row=1, ipadx=30, ipady=30)

    label2 = tk.Label(master, text="Label 2", bg="red")
    label2.grid(column=1, columnspan=3, row=2, ipadx=30, ipady=30)

    label3 = tk.Label(master, text="Label 3", bg="green")
    label3.grid(column=3, row=1, rowspan=3, ipadx=30, ipady=30)


def combined_example(master):
    frame = tk.Frame(master, borderwidth=5, relief=tk.SUNKEN, bg="#999")
    frame.pack(fill=tk.BOTH, expand=True, anchor=tk.CENTER)

    label1 = tk.Label(frame, text="Label 1", bg="blue")
    label1.grid(column=1, row=1, ipadx=30, ipady=30)

    label2 = tk.Label(frame, text="Label 2", bg="red")
    label2.grid(column=1, columnspan=2, row=2, ipadx=30, ipady=30)

    label3 = tk.Label(frame, text="Label 3", bg="green")
    label3.grid(column=2, row=1, ipadx=30, ipady=30)


# Utilize Example Method

examples = [
    ipad_example,
    column_example1,
    column_example2,
    row_example1,
    row_example2,
    columnspan_example1,
    sticky_example1,
    sticky_example2,
    rowspan_example,
    combined_example,
]

if len(sys.argv) > 1:
    example_number = int(sys.argv[1])
else:
    example_number = 1

example = examples[example_number - 1]
source = "".join(inspect.getsourcelines(example)[0][1:])
source = source.replace("master", "root").replace("    ", "")
print(source)
example(root)

root.mainloop()
