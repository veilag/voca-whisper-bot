from sqlalchemy import Column, Integer, String, Time, DateTime, ForeignKey
from uuid import uuid4
from typing import Optional, List
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from datetime import time, datetime, timezone


class DBUser(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    telegram_id: Mapped[int]
    notify_accepted: Mapped[bool] = mapped_column(default=True)
    gender: Mapped[Optional[str]]
    timezone: Mapped[str] = mapped_column(default="Europe/Moscow")

    habits: Mapped[List["Habit"]] = relationship(back_populates="db_user")


class HabitTask(Base):
    __tablename__ = "habit_tasks"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    task_id: Mapped[str] = mapped_column(default=uuid4())
    habit_id: Mapped[int] = mapped_column(ForeignKey("habits.id"))

    time: Mapped[time]
    start_date: Mapped[datetime]
    end_date: Mapped[datetime]

    habit: Mapped["Habit"] = relationship(back_populates="habits")


class Habit(Base):
    __tablename__ = "habits"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(default="Безымянное")
    db_user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    habits: Mapped[List["HabitTask"]] = relationship(back_populates="habit")
    db_user: Mapped["DBUser"] = relationship(back_populates="habits")
