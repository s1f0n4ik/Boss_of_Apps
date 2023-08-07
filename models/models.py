from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, Boolean

metadata = MetaData()

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("hashed_password", String(length=1024), nullable=False),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False),
    )

roles = Table(
    "windows",
    metadata,
    Column("user_id", Integer, ForeignKey(user.c.id)),
    Column("id", Integer, primary_key=True),
    Column("name", String, primary_key=True, nullable=False),
    Column("status", String),
    Column("create_time", TIMESTAMP),
)


