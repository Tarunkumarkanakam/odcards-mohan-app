from authlib.integrations.starlette_client import OAuth
from app.config.config import CLIENT_ID, CLIENT_SECRET

oauth = OAuth()
oauth.register(
    name='google',
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    client_kwargs={
        'scope': 'email openid profile https://www.googleapis.com/auth/gmail.readonly https://mail.google.com',
        'redirect_url': 'http://localhost:8000/oauth/auth/google'
    }
)
