from fastapi import APIRouter, HTTPException
from app.backend.db_config import settings
from app.backend.restoplace import get_restaurant_info
import httpx
import json

router = APIRouter(prefix='/restaurant')


@router.get("/{restaurant_id}", summary='Получить информацию о ресторане')
async def restaurant_info(restaurant_id: str):
    restaurant = await get_restaurant_info(restaurant_id)
    if "error" in restaurant:
        raise HTTPException(status_code=400, detail=restaurant["error"])
    return restaurant


