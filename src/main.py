from fastapi import FastAPI, Depends
from fastapi_users import FastAPIUsers
from src.auth.config import auth_backend
from src.auth.database import User
from src.auth.manager import get_user_manager
from src.auth.schemas import UserRead, UserCreate

app = FastAPI(
    title="MyDiaryApp"
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}


current_user = fastapi_users.current_user()
@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.nickname}"
