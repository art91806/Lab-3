import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk


def generate_key():
    number = entry.get()
    if not number.isdigit() or len(number) != 6:
        messagebox.showerror("Ошибка", "Введите шестизначное число.")
        return


    block1_digits = number[3:6]
    block2_digits = number[0:3]


    let1 = ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=2))
    let2 = ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=2))


    block1 = str(block1_digits) + let1
    block2 = str(block2_digits) + let2


    block3 = int(block1_digits) + int(block2_digits)


    key = f"{block1}-{block2}-{block3:04d}"
    

    result.config(text=f"Ключ: {key}")


root = tk.Tk()
root.title("TASK")
root.geometry("500x400")

image = Image.open("C:/python/Lab-3/vrgl.jpg")
image = image.resize((500, 400), Image.LANCZOS)
bg_image = ImageTk.PhotoImage(image)
label = tk.Label(root, image=bg_image)
label.place(x=0, y=0, relwidth=1, relheight=1)



instruction = tk.Label(root, text="Введите шестизначное число:", bg="white", font=("times new roman", 14))
instruction.pack(pady=10)


entry = tk.Entry(root, font=("times new roman", 14), width=10)
entry.pack(pady=5)


button = tk.Button(root, text="Генерировать ключ", command=generate_key, font=("times new roman", 14), bg="red", fg="black")
button.pack(pady=10)


result = tk.Label(root, text="", bg="white", font=("times new roman", 14))
result.pack(pady=10)


root.mainloop()