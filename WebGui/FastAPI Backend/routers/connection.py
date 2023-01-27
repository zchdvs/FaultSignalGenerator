from fastapi import APIRouter
from . import signal
router = APIRouter(
    prefix="/connection",
    tags=["connection"],
    responses={404: {"description": "Not found"}},
)

@router.post("/slave/play")
async def slave_play():
    return signal.signal_play()
