import httpx
from app.backend.db_config import settings


async def get_restaurant_info(restaurant_id: str):
    url = f"https://api.restoplace.com/v1/restaurants/{restaurant_id}"
    headers = {
        "Authorization": f"Bearer {settings.RESTO_API_KEY}"
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()  # Возвращаем данные о ресторане
        else:
            return {"error": "Не удалось получить информацию о ресторане"}


