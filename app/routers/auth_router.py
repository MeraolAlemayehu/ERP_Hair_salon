from fastapi import APIRouter, HTTPException, Depends
from app.schemas.user_schema import UserCreate, UserLogin, UserResponse
from app.services.auth_service import AuthService
from app.repositories.user_repository import UserRepository

router = APIRouter()

@router.post("/register", response_model=UserResponse)
async def register(user: UserCreate):
    existing_user = await UserRepository.find_by_email(user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = AuthService.hash_password(user.password)
    user_data = {"email": user.email, "hashed_password": hashed_password, "is_active": True}
    await UserRepository.create_user(user_data)
    return UserResponse(email=user.email, is_active=True)

@router.post("/login")
async def login(user: UserLogin):
    authenticated_user = await AuthService.authenticate_user(user.email, user.password)
    if not authenticated_user:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    access_token = AuthService.create_access_token({"sub": authenticated_user["email"]})
    return {"access_token": access_token, "token_type": "bearer"}
