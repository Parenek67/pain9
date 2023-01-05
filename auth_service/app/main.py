from fastapi import FastAPI, HTTPException


class User:
    def __init__(self, id: int, name: str, login: str, password: str):
        self.id = id
        self.name = name
        self.login = login
        self.password = password


users_list = [
    User(0, "Petya", "petya123", "123"),
    User(1, "Vasya", "vasya456", "456"),
    User(2, "Anton", "anton789", "789")
]

app = FastAPI()


@app.get("/v1/users/{login}/{password}")
async def auth(login, password):
    for user in users_list:
        if user.login == login and user.password == password:
            return {"message": "Hello " + user.name}
    raise HTTPException(status_code=404, detail="Error")


@app.get("/v1/users/")
async def get_users():
    return users_list


@app.get("/v__health")
async def health_check():
    return
