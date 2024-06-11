from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, Boolean, func, ForeignKey

metadata = MetaData()

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("hashed_password", String, nullable=False),
    Column("nickname", String, nullable=False),
    Column("created_at", TIMESTAMP, server_default=func.now(), nullable=False),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False)
)

diary = Table(
    "diary",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("author_id", Integer, ForeignKey("user.id"), nullable=False),
    Column("title", String, nullable=False),
    Column("content", String),
    Column("created_at", TIMESTAMP, server_default=func.now(), nullable=False)
)

note = Table(
    "note",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("root_diary_id", Integer, ForeignKey("diary.id"), nullable=False),
    Column("author_id", Integer, ForeignKey("user.id"), nullable=False),
    Column("title", String, nullable=False),
    Column("content", String, nullable=False),
    Column("created_at", TIMESTAMP, server_default=func.now(), nullable=False)
)
