from typing import Optional
from fastapi import Depends, Request
from fastapi_users import BaseUserManager, IntegerIDMixin
from src.database import User, get_user_db

SECRET_KEY_USERMANAGER = "dfqpd34DG54fddf1sdfsd76ds1324dsdfs43fdgDFGDFG43645dfa8HFSdf6gFfah"


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = SECRET_KEY_USERMANAGER
    verification_token_secret = SECRET_KEY_USERMANAGER


async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.nickname} has registered.")


async def get_user_manager(user_db=Depends(get_user_db)):
        yield UserManager(user_db)