from app.database import db
from app.models.user_model import User

class UserRepository:
    collection = db.get_collection("users")

    @staticmethod
    async def find_by_email(email: str):
        return await UserRepository.collection.find_one({"email": email})

    @staticmethod
    async def create_user(user_data: dict):
        return await UserRepository.collection.insert_one(user_data)
