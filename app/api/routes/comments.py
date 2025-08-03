from fastapi import APIRouter

from app.models.comment import Comment
from app.schemas.comment import CommentRequest
from app.services.comment import item

router = APIRouter(prefix="/comments", tags=["items"])


@router.post("/")
async def generate_comment(request: CommentRequest) -> Comment:
    return item.generate(keywords=request.keywords)


@router.get("/")
async def list_comments(offset: int = 0, limit: int = 100) -> list[Comment]:
    return list(item.list(offset=offset, limit=limit))
