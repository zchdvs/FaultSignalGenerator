from fastapi import APIRouter
from .FSGFunctions import comtrade_functions

router = APIRouter(
    prefix="/comtrade",
    tags=["comtrade"],
    responses={404: {"description": "Not found"}},
)

@router.post("/info")
async def signal_info(reductionFactor: int):
    return [x[0::reductionFactor] for x in comtrade_functions.test()]

@router.post("/play")
async def signal_play():
    ''' 
    Used to play a comtrade file.
    '''
    return 'not yet implemented'