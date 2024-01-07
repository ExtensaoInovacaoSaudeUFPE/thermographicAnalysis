from src.comments.Comment import Comment


class CommentRepository:
    data: [Comment] = []

    def insertComment(self, comment: Comment) -> None:
        self.data.append(comment)

    def getComments(self) -> [Comment]:
        return self.data

    def deleteAllComments(self) -> None:
        self.data = []