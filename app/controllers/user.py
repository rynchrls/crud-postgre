from app.schemas.user import createUser, LoginUser
from app.services.user import UserService
from sqlalchemy.orm import Session


class UserController:

    def __init__(self):
        self.service = UserService()

    def user_create(self, data: createUser, db: Session):
        return self.service.create_user(data, db)

    def login_user(self, data: LoginUser, db: Session):
        return self.service.login_user(data, db)


user_controller = UserController()
