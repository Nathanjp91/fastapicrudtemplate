""" Hello World Route handler """

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def hello_world():
    """Hello World route handler"""
    return {"hello": "world"}
