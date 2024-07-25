from typing import Literal

from pydantic import BaseModel

from datetime import datetime


class TelegramUserBase(BaseModel):
    tgId: str
    status: str


class SendMessage(TelegramUserBase):
    lang: Literal['uz', 'ru', 'en'] = 'uz'


class SuccessResponse(BaseModel):
    message: str
