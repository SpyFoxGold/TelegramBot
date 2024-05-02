from pydantic import BaseModel


class UserCreate(BaseModel):
    id: int
    username: str
    request: str

class UserUpdate(BaseModel):
    id: int
    username: str
    request: str