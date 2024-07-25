import asyncio

from fastapi import APIRouter, Depends

from . import schemas, crud
from .database import engine, Session
from .models import Base
from .utils import send_message_via_tg_api

Base.metadata.create_all(bind=engine)

message_router = APIRouter(
    prefix='/api/v1/message'
)


async def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()


@message_router.post("/send", response_model=schemas.SuccessResponse)
async def send_message(telegram_user: schemas.SendMessage, db: Session = Depends(get_db)):
    response = await crud.create_user(db=db, telegram_user=telegram_user)

    # Trigger the Telegram API call in the background
    asyncio.create_task(send_message_via_tg_api(telegram_user=telegram_user))

    return response
