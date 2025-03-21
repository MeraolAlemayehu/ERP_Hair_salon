from pydantic import BaseModel
from typing import Optional
from bson import ObjectId

class User(BaseModel):
    id: Optional[str]  # MongoDB's `_id` is usually an ObjectId
    username: str
    email: str
    password: str  # Ensure hashed passwords
