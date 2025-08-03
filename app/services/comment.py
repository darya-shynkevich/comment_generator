from transformers import pipeline

from app.models.comment import Comment
from app.services.base import BaseService


class CommentService(BaseService[Comment]):
    def __init__(self, model: type[Comment]):
        self.pipeline = pipeline(task="text-generation", model="gpt2")

        super().__init__(model)

    def generate(self, keywords: list[str]) -> Comment:
        prompt = f"Write a short comment about: {', '.join(keywords)}\n\nComment:"

        outputs = self.pipeline(prompt)

        text = outputs[0]["generated_text"]
        if "Comment:" in text:
            description = text.split("Comment:")[1].strip()
        else:
            description = text.strip()

        comment = Comment.objects.create(
            title=f"Comment: {keywords}"[:255], description=description.split("\n")[0]
        )

        return comment


item = CommentService(Comment)
