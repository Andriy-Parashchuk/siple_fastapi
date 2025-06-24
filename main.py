from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    id: int
    username: str
    email: str


users = [{
    'id': 1,
    'username': 'tvbmkl.',
    'email': 'udaw@dawj.com'
}]


@app.get('/users')
def get_all_users():
    return users


@app.get('/users/{user_id}')
def get_all_users(user_id):
    for user in users:
        if user['id'] == user_id:
            return user


# @app.post('/users/create')
# def create_user():
#     return