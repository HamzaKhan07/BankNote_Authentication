import uvicorn
from fastapi import FastAPI
import joblib
from BankNotes import BankNote

app=FastAPI()
classifier=joblib.load('classifier.pkl')

@app.get('/')
def index():
    return {'message': 'Hello World'}

@app.get('/Welcome')
def get_name(name: str):
    return {'Welcome to FastAPI: ': f'{name}'}

@app.post('/Predict')
def predict(data:BankNote):
    data=data.dict()
    variance=data['variance']
    skewness=data['skewness']
    curtosis=data['curtosis']
    entropy=data['entropy']

    prediction=classifier.predict([[variance, skewness, curtosis, entropy]])
    print(prediction)

    if prediction[0] < 0.5:
        res='Its a Bank Note'
    else:
        res='Fake note'

    return {
        'prediction': res
    }

if __name__ == '__main__':
    uvicorn.run(app, '127.0.0.1', port=8000)

# uvicorn main:app --reload





