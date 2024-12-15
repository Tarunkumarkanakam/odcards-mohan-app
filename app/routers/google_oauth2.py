from app.config.config import CLIENT_ID, CLIENT_SECRET
from fastapi import APIRouter, Request, status, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.oauth2 import oauth
from app.services import account
from app.db import database
from app.models import models
import json

router = APIRouter(
    prefix="/oauth",
    tags=['Google Oauth']
)

get_db = database.get_db


@router.get("/login/google")
async def login_via_google(request: Request):
    redirect_uri = request.url_for('auth_via_google')
    return await oauth.google.authorize_redirect(request, redirect_uri)


@router.get("/auth/google", status_code=status.HTTP_204_NO_CONTENT)
async def auth_via_google(request: Request, db: Session = Depends(get_db)):
    try:
        token = await oauth.google.authorize_access_token(request)
        account.add_user(token, db)
    except:
        raise HTTPException(500, detail="Internal Server Error")
