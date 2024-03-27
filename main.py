import subprocess
import os
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage



def run_snake():
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the path to the snake.py file inside the games directory
    snake_path = os.path.join(current_dir, "games", "snake", "main.py")
    # Run the snake.py file using subprocess
    subprocess.Popen(["python", snake_path])


def run_spaceinvader():
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the path to the snake.py file inside the games directory
    spaceinvader_path = os.path.join(current_dir,"games", "spaceinvader", "main.py")
    # Run the snake.py file using subprocess
    subprocess.Popen(["python", spaceinvader_path])

def run_tictactoe():
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the path to the snake.py file inside the games directory
    tictactoe_path = os.path.join(current_dir,"games", "tictactoe", "main.py")
    # Run the snake.py file using subprocess
    subprocess.Popen(["python", tictactoe_path])

def run_pingpong():
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the path to the snake.py file inside the games directory
    pingpong_path = os.path.join(current_dir,"games", "pingpong", "main.py")
    # Run the snake.py file using subprocess
    subprocess.Popen(["python", pingpong_path])


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("665x450")
window.configure(bg = "#FFFFFF")

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x_position = (screen_width - 665) // 2
y_position = (screen_height - 450) // 2

window.geometry(f"665x450+{x_position}+{y_position}")

window.title("M3 - Games")
icon_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'logo.ico'))
window.iconbitmap(icon_path)


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 450,
    width = 665,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    665.0,
    70.0,
    fill="#800000",
    outline="")

canvas.create_rectangle(
    0.0,
    375.0,
    665.0,
    459.0,
    fill="#003C54",
    outline="")

canvas.create_text(
    193.0,
    152.0,
    anchor="nw",
    text="Snake",
    fill="#000000",
    font=("JosefinSansRoman Regular", 32 * -1)
)

canvas.create_text(
    13.0,
    152.0,
    anchor="nw",
    text="Shooter",
    fill="#000000",
    font=("JosefinSansRoman Regular", 32 * -1)
)

canvas.create_text(
    325.0,
    152.0,
    anchor="nw",
    text="Tic Tac Toe",
    fill="#000000",
    font=("JosefinSansRoman Regular", 32 * -1)
)

canvas.create_text(
    499.0,
    152.0,
    anchor="nw",
    text="Ping Pong",
    fill="#000000",
    font=("JosefinSansRoman Regular", 32 * -1)
)

canvas.create_text(
    5.0,
    399.0,
    anchor="nw",
    text="Gjin Prelvukaj",
    fill="#FFFFFF",
    font=("JosefinSansRoman Bold", 24 * -1)
)

canvas.create_text(
    194.0,
    399.0,
    anchor="nw",
    text="Lis Shala",
    fill="#FFFFFF",
    font=("JosefinSansRoman Bold", 24 * -1)
)

canvas.create_text(
    340.0,
    399.0,
    anchor="nw",
    text="Yll Morina\n",
    fill="#FFFFFF",
    font=("JosefinSansRoman Bold", 24 * -1)
)

canvas.create_text(
    499.0,
    399.0,
    anchor="nw",
    text="Orgesa Gashi",
    fill="#FFFFFF",
    font=("JosefinSansRoman Bold", 24 * -1)
)

canvas.create_rectangle(
    317.0,
    384.0,
    318.0,
    435.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    176.0,
    384.0,
    177.0,
    435.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    475.0,
    384.0,
    476.0,
    435.0,
    fill="#FFFFFF",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    325.0,
    39.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=run_snake,
    relief="flat"
)
button_1.place(
    x=187.0,
    y=197.0,
    width=100.0,
    height=100.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=run_spaceinvader,
    relief="flat"
)
button_2.place(
    x=19.0,
    y=197.0,
    width=100.0,
    height=100.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=run_tictactoe,
    relief="flat"
)
button_3.place(
    x=355.0,
    y=197.0,
    width=100.0,
    height=100.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=run_pingpong,
    relief="flat"
)
button_4.place(
    x=523.0,
    y=197.0,
    width=100.0,
    height=100.0
)
window.resizable(False, False)
window.mainloop()
