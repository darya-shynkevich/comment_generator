from uuid import UUID

from fastapi import APIRouter

from app.api.deps import CurrentUser, SessionDep
from app.crud import item
from app.models.comment import Comment, CommentCreate, CommentUpdate

router = APIRouter(prefix="/items", tags=["items"])


@router.post("/create-item")
async def create_item(
    item_in: CommentCreate, user: CurrentUser, session: SessionDep
) -> Comment:
    return item.create(session, owner_id=UUID(user.id), obj_in=item_in)


@router.get("/get-item/{id}")
async def read_item_by_id(id: str, session: SessionDep) -> Comment | None:
    return item.get(session, id=UUID(id))


@router.get("/get-items")
async def read_items(
    session: SessionDep, skip: int = 0, limit: int = 100
) -> list[Comment]:
    return list(item.get_multi(session, skip=skip, limit=limit))


# @router.put("/update-item/{id}")
# async def update_item(id: str, item_in: CommentUpdate, session: SessionDep) -> Comment | None:
#     return item.update(session, id=UUID(id), obj_in=item_in)
#
#
# @router.delete("/delete/{id}")
# async def delete_item(id: str, session: SessionDep) -> Comment | None:
#     return item.remove(session, id=UUID(id))
