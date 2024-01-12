import tkinter as tk
from PIL import Image, ImageTk
import time

window = tk.Tk()
# textbox = tk.Entry(window, background = "blue", foreground = "white", width = 10, )


# frame1 = tk.Frame(window, width=30, height=10, bg="red")
# frame1.pack(fill=tk.Y, side=tk.LEFT)

# frame2 = tk.Frame(window, width=30, height=10, bg="blue")
# frame2.pack()


# def foo():
#     print("Hi")
#     print(textbox.insert(2, "Hello"))

# greeting = tk.Label(frame2, background = "red", foreground="blue", height=10, text="Hello World", width=10)
# start = tk.Button(frame1, text = "Start", width = 10, height = 10, background = "orange", foreground = "blue", command=foo)
# texttext = tk.Text(window, background = "pink", foreground = "orange", height = 10, width = 10)

# # .get() .insert() .delete()
# texttext.pack()
# textbox.pack()
# greeting.pack()
# start.pack()





# frame1 = tk.Frame(master=window, width=200, height=100, bg="red")
# frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

# frame2 = tk.Frame(master=window, width=100, bg="yellow")
# frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

# frame3 = tk.Frame(master=window, width=50, bg="blue")
# frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

# widget = tk.Label(frame2, background = "red", foreground="blue", height=10, text="Hello World", width=10)
# widget.place(x=50, y=50)


# for i in range(3):
#     window.columnconfigure(i, weight=i+1, minsize=75)
#     window.rowconfigure(i, weight=1, minsize=50)
#     for j in range(3):
#         frame = tk.Frame(
#             master=window,
#             relief=tk.RAISED,
#             borderwidth=1
#         )
#         frame.grid(row=i, column=j)
#         label = tk.Label(master=frame, text=f"Row {i+1}\nColumn {j+1}")
#         label.pack(fill=tk.BOTH, side=tk.RIGHT, expand = True)

window.geometry("680x382")


mike = Image.open("cover3.jpg")

mike = mike.resize((680, 382))
tk_img = ImageTk.PhotoImage(mike)

canvas = tk.Canvas(window, width=mike.width, height=mike.height)
canvas.pack(fill="both", expand=True)

canvas.create_image(0,0, image=tk_img, anchor="nw")

# widget = tk.Label(window, background = "red", foreground="blue", height=300, text="Hello World", width=300, image=tk_img)
# widget.pack()

window.mainloop()