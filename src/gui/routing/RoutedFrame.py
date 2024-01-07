import tkinter as tk
from abc import ABC


class RoutedFrame(tk.Frame, ABC):
    def __init__(self, parent: tk.Misc, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

    def uiUpdate(self) -> None:
        pass

    def setRouter(self, router) -> None:
        self.router = router