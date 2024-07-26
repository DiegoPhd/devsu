from pydantic import BaseModel


class CreateUser(BaseModel):
    id: int = 0
    username: str
    firtsName: str
    lastName: str
    email: str
    password: str
    phone: str
    userStatus: int = 0


class UpdateUser(CreateUser): ...
