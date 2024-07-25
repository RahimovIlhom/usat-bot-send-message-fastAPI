from sqlalchemy import Integer, String, DateTime, Column, func
from .database import Base


class TelegramUser(Base):
    __tablename__ = 'telegram_users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    tgId = Column(String(255))
    status = Column(String(255), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
