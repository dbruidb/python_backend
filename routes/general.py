from fastapi import APIRouter

router = APIRouter(prefix="general", tags = ["general"])


@router.get("/test")
async def get():
    return [{"test": "response"}]
