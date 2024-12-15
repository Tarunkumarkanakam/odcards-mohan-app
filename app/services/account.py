from sqlalchemy.orm import Session
from fastapi import Request, Depends
from app.models import models, schemas
from app.db import database

get_db = database.get_db


def add_user(request, db: Session):
    account = db.query(models.Account).filter(
        models.Account.gmail_id == request.get('userinfo').get('email')).first()
    if not account:
        new_account = models.Account(
            gmail_id=request.get('userinfo').get('email'),
            access_token=request.get('access_token'),
            refresh_token=request.get('refresh_token'),
            user_id=1
        )
        db.add(new_account)
        db.commit()
    else:
        account.access_token = request.get('access_token')
        account.refresh_token = request.get('refresh_token')
        db.commit()
