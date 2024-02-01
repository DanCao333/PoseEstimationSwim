import tkinter as tk

class Sidebar(tk.Frame):
    def __init__(self, parent, change_screen_callback, **kwargs):
        super().__init__(parent, **kwargs)
        self.change_screen = change_screen_callback

        btn_home_screen = tk.Button(self, text="Home", command=lambda: self.change_screen("HomeScreen"))
        btn_home_screen.pack(fill="x")

        btn_gallery_screen = tk.Button(self, text="Gallery", command=lambda: self.change_screen("GalleryScreen"))
        btn_gallery_screen.pack(fill="x")

        # btn_home_screen = tk.Button(self, text="Home", command=lambda: self.change_screen("HomeScreen"))
        # btn_home_screen.pack(fill="x")

        # btn_home_screen = tk.Button(self, text="Home", command=lambda: self.change_screen("HomeScreen"))
        # btn_home_screen.pack(fill="x")
