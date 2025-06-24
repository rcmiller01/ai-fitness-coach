from fastapi import FastAPI

app = FastAPI(title='MIA Backend API', version='0.1')

@app.get('/')
def root():
    return {'message': 'MIA backend running'}
