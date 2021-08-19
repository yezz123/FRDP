from datetime import datetime, timedelta
from typing import Optional
from jose import jwt
from core.config import settings


def generate_password_reset_token(email: str) -> str:
    delta = timedelta(hours=settings.EMAIL_RESET_TOKEN_EXPIRE_HOURS)
    now = datetime.utcnow()
    expires = now + delta
    exp = expires.timestamp()
    return jwt.encode(
        {
            "exp": exp,
            "nbf": now,
            "sub": email
        },
        settings.SECRET_KEY,
        algorithm="HS256",
    )


def verify_password_reset_token(token: str) -> Optional[str]:
    try:
        return jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
    except jwt.JWTError:
        return None
