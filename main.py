import tkinter as tk
from tkinter import Button
from recognizer import recognize
from PIL import Image, ImageTk


def say_something():
    s = recognize()
    print(s)
    output_text_area.delete(1.0, tk.END)
    output_text_area.insert(1.0, s)


root = tk.Tk()
root.title("Gender Identification by Voice")
root.state('zoomed')

image = Image.open("images/android_mic.jpg")
photo = ImageTk.PhotoImage(image)

project_name_label = tk.Label(root, text="Gender Identification by Voice", fg="black", font="Times 30 bold")
project_name_label.place(x=10, y=10, height=50)

mic_button = Button(root, image=photo, bg="white", command=say_something)
mic_button.place(x=10, y=60, width=500, height=236)

say_something_button = Button(root, text='Say Something !', bg="green", fg="white", font="Times 20 bold", width=25, height=2, command=say_something)
say_something_button.place(x=10, y=310, width=500, height=50)

text_area_label = tk.Label(root, text="User Said", fg="black", font="Times 30 bold")
text_area_label.place(x=-110, y=370, width=400, height=60)

output_text_area = tk.Text(font="Times 16 bold")
output_text_area.place(x=10, y=440, width=500, height=200)

accept_button = Button(root, text='Identify', bg="green", fg="white", font="Times 20 bold", width=25, height=2)
accept_button.place(x=10, y=650, width=500, height=50)

sign_image_label = tk.Label(root, bg="white")
sign_image_label.place(x=540, y=61, width=800, height=637)

root.geometry("500x300+100+100")  # Width x Height
root.mainloop()
