import customtkinter as ctk
from abc import ABC


class RoutedFrame(ctk.CTkFrame, ABC):
    def __init__(self, master, *args, **kwargs) -> None:
        super().__init__(master, *args, **kwargs)

    def uiUpdate(self) -> None:
        pass

    def setRouter(self, router) -> None:
        self.router = router