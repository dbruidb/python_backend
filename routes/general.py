from fastapi import APIRouter

router = APIRouter()


@router.get("/users", tag=["general"])
async def get():
    return [{"test": "response"}]
