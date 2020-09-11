import tkinter as tk
from tkinter import PhotoImage
import tkinter.scrolledtext as scrolled
import inspect
from PIL import ImageTk, Image

root = tk.Tk()

root.minsize(width=600, height=850)
root.geometry("600x850")

sidebar = tk.Frame(root, width=200, background="#999")
sidebar.pack(side=tk.LEFT, fill=tk.Y)

main_area = tk.Frame(root, width=400, height=600)
main_area.pack(side=tk.RIGHT, fill=tk.BOTH)

canvas = tk.Canvas(main_area, width=400, height=400, background="white")

code_output = scrolled.ScrolledText(
    main_area,
    width=400,
    height=200,
    foreground="black",
    background="white",
    font=("Monospaced", 24),
    wrap="word",
)


def run_code():
    user_code = code_output.get(1.0, tk.END)
    try:
        # Compile user code to allow for running multiline blocks of code.
        compiled = compile(user_code, "user_code", "exec")
        canvas.delete(tk.ALL)
        eval(compiled)
    except Exception as err:
        print(err)


run_button = tk.Button(main_area, text="Run Code", command=run_code)

run_button.pack()
canvas.pack(fill=tk.BOTH, expand=True)
code_output.pack(padx=10, pady=10)


def show_code(func):
    def handler():
        canvas.delete(tk.ALL)

        source = "".join(
            map(lambda l: l.replace("    ", "", 1), inspect.getsourcelines(func)[0][2:])
        )
        code_output.delete(1.0, tk.END)
        code_output.insert(tk.INSERT, source)

        func()

    return handler


@show_code
def render_rigid_line():
    canvas.create_line(
        30.0,
        30.0,
        300.0,
        300.0,
        200.0,
        100.0,
        width=4,
        fill="black",
        arrow=tk.LAST,
        smooth=False,
    )


@show_code
def render_smooth_line():
    canvas.create_line(
        30.0,
        30.0,
        300.0,
        300.0,
        200.0,
        100.0,
        width=4,
        fill="black",
        arrow=tk.LAST,
        smooth=True,
    )


@show_code
def render_polygon():
    canvas.create_polygon(
        30.0, 30.0, 300.0, 300.0, 200.0, 100.0, outline="red", width=4, fill="black"
    )


@show_code
def render_odd_polygon():
    canvas.create_polygon(
        30.0,
        30.0,
        300.0,
        300.0,
        200.0,
        100.0,
        30.0,
        170.0,
        outline="red",
        width=4,
        fill="black",
    )


@show_code
def render_normal_polygon():
    canvas.create_polygon(
        30.0,
        30.0,
        30.0,
        170.0,
        300.0,
        300.0,
        200.0,
        100.0,
        outline="red",
        width=4,
        fill="black",
    )


@show_code
def render_rectangle():
    canvas.create_rectangle(
        30.0, 30.0, 300.0, 300.0, outline="red", width=4, fill="black"
    )


@show_code
def render_circle():
    canvas.create_oval(30.0, 30.0, 300.0, 300.0, outline="red", width=4, fill="black")


@show_code
def render_oval():
    canvas.create_oval(30.0, 30.0, 200.0, 300.0, outline="red", width=4, fill="black")


@show_code
def render_arc_arc():
    canvas.create_arc(
        30.0, 30.0, 200.0, 300.0, style="arc", outline="red", width=4, fill="black"
    )


@show_code
def render_arc_pie():
    canvas.create_arc(
        30.0, 30.0, 200.0, 300.0, style="pieslice", outline="red", width=4, fill="black"
    )


@show_code
def render_arc_chord():
    canvas.create_arc(
        30.0, 30.0, 200.0, 300.0, style="chord", outline="red", width=4, fill="black"
    )


@show_code
def render_text():
    canvas.create_text(
        20,
        20,
        fill="red",
        text="A Quick Brown\nFox Jumped Over\nthe Lazy Dog",
        font=("Helvetica", 36),
    )


@show_code
def render_text_anchored():
    canvas.create_text(
        20,
        20,
        fill="red",
        text="A Quick Brown\nFox Jumped Over\nthe Lazy Dog",
        font=("Helvetica", 36),
        anchor=tk.NW,
    )


@show_code
def render_jpg():
    img = Image.open("./windows-tkinter-custom-icon.png")
    photo = ImageTk.PhotoImage(img)
    canvas.image = photo
    canvas.create_image(20, 20, anchor=tk.NW, image=photo)


buttons = [
    ("Draw Line", render_rigid_line),
    ("Draw Line (Smooth)", render_smooth_line),
    ("Draw Polygon", render_polygon),
    ("Draw Odd Polygon", render_odd_polygon),
    ("Draw Normal Polygon", render_normal_polygon),
    ("Draw Rectangle", render_rectangle),
    ("Draw Circle", render_circle),
    ("Draw Oval", render_oval),
    ("Draw Arc", render_arc_arc),
    ("Draw Arc (Pieslice)", render_arc_pie),
    ("Draw Arc (Chord)", render_arc_chord),
    ("Draw Text", render_text),
    ("Draw Text (Anchored)", render_text_anchored),
    ("Render JPG", render_jpg),
]

for text, func in buttons:
    button = tk.Button(sidebar, pady=5, padx=5, text=text, command=func)
    button.pack(fill=tk.X, padx=5, pady=10)

root.mainloop()
