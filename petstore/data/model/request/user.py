from pydantic import BaseModel


class CreateUserModel(BaseModel):
    id: int = 0
    username: str
    firstName: str
    lastName: str
    email: str
    password: str
    phone: str
    userStatus: int = 0


class UpdateUserModel(CreateUserModel): ...
