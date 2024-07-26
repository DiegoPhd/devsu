from pydantic import BaseModel


class UserResponse(BaseModel):
    code: int
    type: str
    message: str
