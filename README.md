# One time Setup
$ source scripts/setup.sh 

# Run the webserver that reloads automatically
Syntax  : uvicorn module_name:instance_name --reload
Example : uvicorn app.main:app --reload

The server will be up on 0.0.0.0:8000

# Documentation
Swagger UI  : http://0.0.0.0:8000/docs
ReDoc UI    : http://0.0.0.0:8000/redoc

# Reference
Official Documentation  : https://fastapi.tiangolo.com/
Youtube Tutorial        : https://www.youtube.com/watch?v=7t2alSnE2-I

# Terminology
@app.get('/about')
def about():
    return {'data': 'about page'}

'/about' is called path
'get' is called operation
'def about()' function is called path operation function
'@app' is called path operation decorator