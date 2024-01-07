import tkinter as tk
from abc import ABC


class RoutedFrame(tk.Frame, ABC):
    def __init__(self, master: tk.Misc, *args, **kwargs) -> None:
        super().__init__(master, *args, **kwargs)

    def uiUpdate(self) -> None:
        pass

    def setRouter(self, router) -> None:
        self.router = router