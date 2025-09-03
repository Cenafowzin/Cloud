from fastapi import FastAPI, Body

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello world!"}

@app.post("/auth/me")
def auth_me(user: str = Body(..., embed=True)):
    return {"user": user, "ping": "pong"}
