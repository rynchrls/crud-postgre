from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException, Request, status
from ..utils.security import JWTToken

oauth2 = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


def get_current_user(token: Request):
    jwt = token.cookies.get("token")

    if jwt is None:
        raise HTTPException(
            status_code=401,
            detail="Not authenticated",
            headers={"WWW-Authenticate": "Bearer"},
        )

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    return JWTToken().verify_token(jwt, credentials_exception)
