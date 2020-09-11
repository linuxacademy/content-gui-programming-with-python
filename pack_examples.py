import tkinter as tk
import inspect
import sys

# Run the various example versions of the application by passing the example number
# to the script:
#
# Usage:
# python3 pack_examples.py [example_number]
#
# Example to run the first example:
# python3 pack_examples.py 1

root = tk.Tk()

root.minsize(550, 400)


def side_and_ipad_example(master):
    label1 = tk.Label(master, text="Label 1", bg="blue")
    label1.pack(ipadx=30, ipady=30)

    label2 = tk.Label(master, text="Label 2", bg="red")
    label2.pack(ipadx=30, ipady=30, side=tk.LEFT)

    label3 = tk.Label(master, text="Label 3", bg="green")
    label3.pack(ipadx=30, ipady=30, side=tk.RIGHT)


def expand_example_1(master):
    label1 = tk.Label(master, text="Label 1", bg="blue")
    label1.pack(ipadx=30, ipady=30, side=tk.LEFT, fill=None, expand=True)

    label2 = tk.Label(master, text="Label 2", bg="red")
    label2.pack(ipadx=30, ipady=30, side=tk.LEFT, fill=None, expand=True)

    label3 = tk.Label(master, text="Label 3", bg="green")
    label3.pack(ipadx=30, ipady=30, side=tk.LEFT, fill=None, expand=True)


def expand_example_2(master):
    label1 = tk.Label(master, text="Label 1", bg="blue")
    label1.pack(ipadx=30, ipady=30, side=tk.LEFT, fill=None, expand=False)

    label2 = tk.Label(master, text="Label 2", bg="red")
    label2.pack(ipadx=30, ipady=30, side=tk.LEFT, fill=None, expand=True)

    label3 = tk.Label(master, text="Label 3", bg="green")
    label3.pack(ipadx=30, ipady=30, side=tk.LEFT, fill=None, expand=False)


def fill_example(master):
    label1 = tk.Label(master, text="Label 1", bg="blue")
    label1.pack(ipadx=30, ipady=30, side=tk.LEFT, fill=None, expand=False)

    label2 = tk.Label(master, text="Label 2", bg="red")
    label2.pack(ipadx=30, ipady=30, side=tk.LEFT, fill=tk.BOTH, expand=True)

    label3 = tk.Label(master, text="Label 3", bg="green")
    label3.pack(ipadx=30, ipady=30, side=tk.LEFT, fill=tk.BOTH, expand=False)


def pad_example(master):
    label1 = tk.Label(master, text="Label 1", bg="blue")
    label1.pack(ipadx=30, ipady=30, side=tk.LEFT, fill=None, expand=False)

    label2 = tk.Label(master, text="Label 2", bg="red")
    label2.pack(
        padx=20, pady=20, ipadx=30, ipady=30, side=tk.LEFT, fill=tk.BOTH, expand=True
    )

    label3 = tk.Label(master, text="Label 3", bg="green")
    label3.pack(ipadx=30, ipady=30, side=tk.LEFT, fill=tk.BOTH, expand=False)


def anchor_example(master):
    label1 = tk.Label(master, text="Label 1", bg="blue")
    label1.pack(ipadx=30, ipady=30, side=tk.LEFT, fill=None, expand=False, anchor=tk.NW)

    label2 = tk.Label(master, text="Label 2", bg="red")
    label2.pack(
        padx=20, pady=20, ipadx=30, ipady=30, side=tk.LEFT, fill=tk.BOTH, expand=True
    )

    label3 = tk.Label(master, text="Label 3", bg="green")
    label3.pack(ipadx=30, ipady=30, side=tk.LEFT, fill=tk.BOTH, expand=False)


def all_anchors(master):
    master.maxsize(550, 400)

    rows = [
        ["tk.NW", "tk.N", "tk.NE"],
        ["tk.W", "tk.CENTER", "tk.E"],
        ["tk.SW", "tk.S", "tk.SE"],
    ]

    for row_index, row in enumerate(rows):
        frame = tk.Frame(master)
        frame.pack(fill=tk.BOTH, expand=row_index == 1)
        for index, item in enumerate(row):
            label = tk.Label(frame, text=item, bg="blue")
            label.pack(ipadx=30, ipady=30, side=tk.LEFT, fill=None, expand=index == 1)


# Utilize Example Method

examples = [
    # 1) Side and ipad example
    side_and_ipad_example,
    # 2) Expand example 1
    expand_example_1,
    # 3) Expand example 2
    expand_example_2,
    # 4) Fill example
    fill_example,
    # 5) Pad example
    pad_example,
    # 6) Anchor example
    anchor_example,
    # 7) All anchors
    all_anchors,
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
