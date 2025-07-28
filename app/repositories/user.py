from app.schemas.user import createUser, LoginUser
from sqlalchemy.orm import Session
from ..models.user import User
from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from ..utils.hash import Hash
from ..utils.security import JWTToken
from typing import Any


class UserRepository:
    def __init__(self):
        self.hash = Hash()
        self.jwt = JWTToken()
        pass

    def create_user(self, data: createUser, db: Session):
        try:
            hashed_password = self.hash.bcrypt(data.password)
            new_user = User(
                fullName=data.username,
                email=data.email,
                password=hashed_password,
                age=data.age,
            )
            db.add(new_user)
            db.commit()
            db.refresh(new_user)
            return new_user
        except IntegrityError:
            db.rollback()
            raise HTTPException(status_code=400, detail="Email already Exists.")
        except Exception:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Something went wrong.",
            )

    def login_user(self, data: LoginUser, db: Session):
        try:
            user = db.query(User).filter(User.email == data.email).first()
            if user is None:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND, detail="User not found."
                )
            password = str(user.password)
            is_pass_valid = self.hash.verify(data.password, password)
            if not is_pass_valid:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid credentials.",
                )
            token_args: dict[str, Any] = {
                "sub": user.email,
                "username": user.fullName,
                "id": user.id,
            }
            return self.jwt.create_access_token(data=token_args)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Something went wrong. " + str(e),
            )
