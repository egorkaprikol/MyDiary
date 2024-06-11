from fastapi import APIRouter
from fastapi_users import fastapi_users, FastAPIUsers

from src.auth.config import auth_backend
from src.auth.manager import get_user_manager
from src.auth.models import User
from src.auth.schemas import UserRead, UserCreate


router = APIRouter(
    prefix="/Auth",
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)
router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)

router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)

current_user = fastapi_users.current_user()