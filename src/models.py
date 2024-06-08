from datetime import datetime

from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, Boolean

metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("login", String, nullable=False),
    Column("hashed_password", String, nullable=False),
    Column("nickname", String, nullable=False),
    Column("created_at", TIMESTAMP, default=datetime.now, nullable=False),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is superuser", Boolean, default=False, nullable=False),
    Column("is verified", Boolean, default=False, nullable=False)
)

diaries = Table(
    "diaries",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("author_id", Integer, ForeignKey("users.id"), nullable=False),
    Column("title", String, nullable=False),
    Column("content", String),
    Column("created_at", TIMESTAMP, default=datetime.now, nullable=False)
)

notes = Table(
    "notes",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("dairy_id", Integer, ForeignKey("diaries.id"), nullable=False),
    Column("author_id", Integer, ForeignKey("users.id"), nullable=False),
    Column("title", String, nullable=False),
    Column("content", String, nullable=False),
    Column("created_at", TIMESTAMP, default=datetime.now, nullable=False)
)

