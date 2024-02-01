import tkinter as tk
from components.sidebar import Sidebar
from screens.home_screen import HomeScreen
from screens.gallery_screen import GalleryScreen

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aqua AI")
        self.geometry("800x600")
        
        self.sidebar = Sidebar(self, self.change_screen)
        self.sidebar.pack(side="left", fill="y")

        self.screen_container = tk.Frame(self)
        self.screen_container.pack(side="right", fill="both", expand=True)

        self.screens = {
            "HomeScreen": HomeScreen(self.screen_container),
            "GalleryScreen": GalleryScreen(self.screen_container),
        }

        for screen in self.screens.values():
            screen.place(relwidth=1, relheight=1)

        self.change_screen("HomeScreen")

    def change_screen(self, screen_name):
        print(f"Changing to screen: {screen_name}")
        screen = self.screens[screen_name]
        screen.tkraise()