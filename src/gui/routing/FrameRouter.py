import tkinter as tk

from src.gui.routing.RoutedFrame import RoutedFrame

class FrameRouter:
    screens: dict[str, RoutedFrame]
    currentScreen: str | None = None

    def attachToScreens(self, screens: dict[str, RoutedFrame]) -> None:
        self.screens = screens
        for screen in self.screens.values():
            screen.setRouter(self)

    def switchScreen(self, screen: str) -> None:
        if screen not in self.screens:
            raise ValueError(f"Screen {screen} not found")
        if screen == self.currentScreen:
            return

        if self.currentScreen is not None:
            self.screens[self.currentScreen].pack_forget()

        self.currentScreen = screen
        self.screens[self.currentScreen].pack(fill=tk.BOTH, expand=True)
        self.screens[self.currentScreen].uiUpdate()