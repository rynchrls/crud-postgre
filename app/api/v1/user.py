from fastapi import APIRouter, Depends, Response
from app.controllers.user import user_controller
from ...schemas.user import createUser, LoginUser
from ...schemas.auth import TokenData
from ...core.oauth2 import get_current_user


from sqlalchemy.orm import Session
from ...db.session import db_session


class UserRouter:
    def __init__(self):
        self.router = APIRouter()
        self.controller = user_controller

        # Routes
        self.router.post(
            "",
            status_code=201,
        )(self.create_user)
        self.router.post("/login", status_code=200)(self.login_user)
        self.router.get("", response_model=TokenData)(self.get_user)

    def create_user(self, request_data: createUser, db: Session = Depends(db_session)):
        return self.controller.user_create(request_data, db)

    def login_user(
        self, res: Response, data: LoginUser, db: Session = Depends(db_session)
    ):
        access_token = self.controller.login_user(data, db)

        res.set_cookie(
            key="token",  # Cookie name
            value=access_token,  # JWT token or session value
            httponly=True,  # Prevents JS access to the cookie (protects against XSS)
            samesite="lax",  # Lax is good for basic CSRF protection while allowing links
            secure=False,  # ❌ Only set to True in production with HTTPS
            max_age=60 * 60 * 24,  # 1 day in seconds (optional, adjust as needed)
            path="/",  # Cookie valid for all paths
        )
        return {
            "message": "Login successful",
            "access_token": access_token,
            "token_type": "bearer",
        }

    def get_user(self, user: TokenData = Depends(get_current_user)):
        return user


router = UserRouter().router
