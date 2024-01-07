import customtkinter as ctk
class NavButton(ctk.CTkButton):
    def __init__(self, parent, text: str, image: ctk.CTkImage, command, **kwargs) -> None:
        super().__init__(parent, text=text, image=image, command=command, **kwargs)
        self.configure(border_spacing=10, fg_color="transparent", text_color=("gray10", "gray90"),
                       hover_color=("gray70", "gray30"), corner_radius=0, height=40, anchor="w")