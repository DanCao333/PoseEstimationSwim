import tkinter as tk

class GalleryScreen(tk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        label = tk.Label(self, text="This is gallery")
        label.pack()