from src.comments.CommentService import commentService
from src.gui.routing.RoutedFrame import RoutedFrame
import customtkinter as ctk

class CommentFrame(RoutedFrame):
    def __init__(self, master) -> None:
        super().__init__(master)

        self.entry = ctk.CTkEntry(self)
        self.entry.pack()

        self.sendButton = ctk.CTkButton(self, text="Enviar", command=self.sendComment)
        self.sendButton.pack()

        self.commentsLabel = ctk.CTkLabel(self, text="")
        self.commentsLabel.pack()

    def sendComment(self) -> None:
        content = self.entry.get()
        commentService.insertComment(content)
        self.uiUpdate()

    def uiUpdate(self) -> None:
        comments = commentService.getComments()
        commentString = ""
        for comment in comments:
            commentString += comment.content + "\n"

        self.commentsLabel.configure(text=commentString)