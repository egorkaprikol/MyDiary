from fastapi import FastAPI, Depends
# from fastapi_users import FastAPIUsers
# from src.auth.config import auth_backend
# from src.database import User
# from src.auth.manager import get_user_manager
# from src.auth.schemas import UserRead, UserCreate
from src.auth.router import router as router_auth
from src.diary.router import router as router_diary

app = FastAPI(
    title="MyDiaryApp"
)

app.include_router(router_auth)
app.include_router(router_diary)
@app.get("/")
async def root():
    return {"message": "Hello World"}

