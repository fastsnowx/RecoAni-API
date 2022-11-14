from pydantic import BaseModel
from typing import Optional
from decouple import config

class SuccessMsg(BaseModel):
    message: str