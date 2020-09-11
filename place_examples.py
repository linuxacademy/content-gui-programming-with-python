import tkinter as tk
import inspect
import sys

# Run the various example versions of the application by passing the example number
# to the script:
#
# Usage:
# python3 place_examples.py [example_number]
#
# Example to run the first example:
# python3 place_examples.py 1

root = tk.Tk()

root.minsize(550, 400)


def x_and_y_example(master):
    label1 = tk.Label(master, text="Label 1", bg="blue")
    label1.place(x=5, y=5)

    label2 = tk.Label(master, text="Label 2", bg="red")
    label2.place(x=40, y=40)

    label3 = tk.Label(master, text="Label 3", bg="green")
    label3.place(x=80, y=80)


def height_and_width_example(master):
    label1 = tk.Label(master, text="Label 1", bg="blue")
    label1.place(x=5, y=5, width=400)

    label2 = tk.Label(master, text="Label 2", bg="red")
    label2.place(x=40, y=40, height=30)

    label3 = tk.Label(master, text="Label 3", bg="green")
    label3.place(x=80, y=80, height=300)


def anchor_example1(master):
    label1 = tk.Label(master, text="Label 1", bg="blue")
    label1.place(height=60, width=100, anchor=tk.NW)


def anchor_example2(master):
    label1 = tk.Label(master, text="Label 1", bg="blue")
    label1.place(height=60, width=100, anchor=tk.CENTER)


def anchor_example3(master):
    label1 = tk.Label(master, text="Label 1", bg="red")
    label1.place(x=100, y=30, height=60, width=200, anchor=tk.CENTER)


def relx_rely_example(master):
    label1 = tk.Label(master, text="Label 1", bg="red")
    label1.place(relx=0.0, rely=0.5)


def relwidth_relheight_example(master):
    label1 = tk.Label(master, text="Label 1", bg="red")
    label1.place(relx=0.5, rely=0.5, relheight=0.3, relwidth=0.3, anchor=tk.CENTER)


def bordermode_example(master):
    frame = tk.Frame(master, borderwidth=40, relief=tk.SUNKEN)
    frame.pack(fill=tk.BOTH, expand=True)

    label1 = tk.Label(frame, text="Label 1", bg="blue")
    label1.place(relx=0.0, rely=0.15, bordermode=tk.INSIDE)

    label2 = tk.Label(frame, text="Label 2", bg="red")
    label2.place(relx=0.0, rely=0.30, bordermode=tk.OUTSIDE)


# Utilize Example Method

examples = [
    x_and_y_example,
    height_and_width_example,
    anchor_example1,
    anchor_example2,
    anchor_example3,
    relx_rely_example,
    relwidth_relheight_example,
    bordermode_example,
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
