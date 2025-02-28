import httpx
from fastapi import HTTPException


async def make_request(method: str, url: str, headers: dict = None, json: dict = None, params: dict = None):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.request(method, url, headers=headers, json=json, params=params)
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code, detail=f'API Restoplace error: {e.response.text}')
        except httpx.RequestError:
            raise HTTPException(status_code=500, detail='Ошибка подключения к API Restoplace')

        return response.json()
