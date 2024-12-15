from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from starlette.middleware.sessions import SessionMiddleware
from sqlalchemy.orm import Session
from app.routers import google_oauth2
from app.models import models
from app.db.database import engine, get_db


models.Base.metadata.create_all(bind=engine)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # db: Session = get_db()
    # try:
    #     admin_user = db.query(models.User).filter(models.User.id == 1).first()
    #     if not admin_user:
    #         new_admin = models.User(id=1, name="Mohan")
    #         db.add(new_admin)
    #         db.commit()
    #         print(f"Admin user created")
    #     else:
    #         print(f"Admin user already exists")
    # except Exception as e:
    #     print("Error: ", e)
    print("App started")
    yield
    print("App closed")

app = FastAPI(lifespan=lifespan)
app.add_middleware(
    SessionMiddleware, secret_key="secretkey....")

app.include_router(google_oauth2.router)
