from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from server.core.database import get_db
from server.core.validators import validate_email, validate_password
from server.core.responses import success_response, error_response
from server.schemas.user import UserCreate, UserLogin, UserResponse
from server.services.user_service import get_user_by_email, create_user
from server.services.auth_service import hash_password, verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/signup", status_code=status.HTTP_201_CREATED)
async def signup(user_in: UserCreate, db: AsyncSession = Depends(get_db)):
    """
    Register a new user.
    """
    # 1. Validation
    if not validate_email(user_in.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error_response("VALIDATION_ERROR", "Invalid email format")
        )
    
    if not validate_password(user_in.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error_response("VALIDATION_ERROR", "Password must be at least 8 characters, include uppercase, lowercase, and a special character")
        )
    
    # 2. Check if user exists
    existing_user = await get_user_by_email(db, user_in.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=error_response("CONFLICT_ERROR", "User with this email already exists")
        )
    
    # 3. Hash password and create user
    hashed_pwd = hash_password(user_in.password)
    user_data = user_in.model_dump()
    user_data["password"] = hashed_pwd
    
    new_user = await create_user(db, user_data)
    
    return success_response(
        data=UserResponse.model_validate(new_user).model_dump(),
        message="User registered successfully"
    )

@router.post("/login")
async def login(login_in: UserLogin, db: AsyncSession = Depends(get_db)):
    """
    Authenticate a user and return a JWT token.
    """
    # 1. Check if user exists
    user = await get_user_by_email(db, login_in.email)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=error_response("NOT_FOUND", "User does not exist")
        )
    
    # 2. Verify password
    if not verify_password(login_in.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=error_response("UNAUTHORIZED", "Invalid password")
        )
    
    # 3. Generate token
    access_token = create_access_token(data={"sub": str(user.id)})
    
    return success_response(
        data={
            "access_token": access_token,
            "token_type": "bearer",
            "user": UserResponse.model_validate(user).model_dump()
        },
        message="Login successful"
    )
