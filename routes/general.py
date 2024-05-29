from fastapi import APIRouter

router = APIRouter()


@router.get("/users", tags=["general"])
async def get():
    return [{"test": "response"}]
