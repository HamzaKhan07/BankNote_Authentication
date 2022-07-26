import uvicorn
from fastapi import FastAPI

app=FastAPI()

# home
@app.get('/')
def index():
    return {'message': 'Hello World'}

# welcome url
@app.get('/Welcome')
def get_name(name: str):
    return {'Welcome to FastAPI: ' : f'{name}'}

if __name__ == '__main__':
    uvicorn.run(app, '127.0.0.1', port=8000)

# uvicorn app:app --reload

