from fastapi import FastAPI
from .routers import authenticate
from fastapi.middleware.cors import CORSMiddleware
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


app = FastAPI()

# allowed origins
origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Routers
app.include_router(authenticate.router, prefix="/auth",tags=["Auth"])



@app.get("/")
def root_of_app():
    return {"status":200}