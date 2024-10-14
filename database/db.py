from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import datetime
from . import restart_db


class Posts(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    content: str
    created: datetime = Field(default_factory=datetime.now)




#EOF

restart_db()