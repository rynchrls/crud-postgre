from app.schemas.user import createUser, LoginUser
from app.repositories.user import UserRepository
from sqlalchemy.orm import Session


class UserService:

    def __init__(self):
        self.repository = UserRepository()

    def create_user(self, data: createUser, db: Session):
        return self.repository.create_user(data, db)

    def login_user(self, data: LoginUser, db: Session):
        return self.repository.login_user(data, db)
