from src.comments.Comment import Comment
from src.comments.CommentRepository import CommentRepository


class CommentService:
    def __init__(self, commentRepository: CommentRepository):
        self.commentRepository = commentRepository

    def getComments(self) -> [Comment]:
        return self.commentRepository.getComments()

    def insertComment(self, content: str) -> None:
        self.commentRepository.insertComment(Comment(content))

    def deleteAllComments(self) -> None:
        self.commentRepository.deleteAllComments()


commentService = CommentService(CommentRepository())