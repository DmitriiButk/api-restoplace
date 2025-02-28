from pydantic import BaseModel, EmailStr, constr, Field, StringConstraints
from typing import List, Optional, Annotated
from datetime import datetime


class ReserveCreate(BaseModel):
    from_time: datetime = Field(..., alias='from', description='Начало резерва')
    to: datetime = Field(..., description='Конец резерва')
    name: constr(min_length=1) = Field(..., description='Имя гостя')
    phone: Optional[Annotated[str, StringConstraints(pattern=r'^7\d{10}$')]] = Field(
        None, description='Телефон гостя в формате 79876543210'
    )
    email: Optional[EmailStr] = Field(None, description='Почта гостя')
    count: Optional[int] = Field(None, description='Количество человек')
    text: Optional[str] = Field(None, description='Комментарий к резерву')
    source: Optional[str] = Field(None, description='Источник бронирования (домен)')
    item_ids: Optional[List[int]] = Field(None, description='ID бронируемого стола или столов')
    waitlist: Optional[bool] = Field(False, description='Заявка попадет в Лист ожидания')
    deposit: Optional[bool] = Field(True, description='Учитывать депозит при бронировании')

    class Config:
        allow_population_by_field_name = True
        json_encoders = {
            datetime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }
