from sqlalchemy.orm import Session
from . import models, schemas


async def create_user(db: Session, telegram_user: schemas.SendMessage):
    db_user = models.TelegramUser(tgId=telegram_user.tgId, status=telegram_user.status)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"message": "Message saved successfully"}
