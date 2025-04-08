from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.security import get_password_hash
from app.db import base  # noqa: F401
from app.models.models import User

def init_db(db: Session) -> None:
    # Create superuser
    user = db.query(User).filter(User.email == settings.FIRST_SUPERUSER).first()
    if not user:
        user = User(
            email=settings.FIRST_SUPERUSER,
            hashed_password=get_password_hash(settings.FIRST_SUPERUSER_PASSWORD),
            is_superuser=True,
        )
        db.add(user)
        db.commit()
        db.refresh(user) 