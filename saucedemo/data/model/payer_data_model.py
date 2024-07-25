from pydantic import BaseModel


class PayerData(BaseModel):
    firts_name: str
    last_name: str
    zip_code: str
    