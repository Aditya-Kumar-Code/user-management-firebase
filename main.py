from fastapi.exceptions import HTTPException
import uvicorn
import pyrebase
from fastapi import FastAPI
from firebase_admin import firestore
from fastapi.requests import Request

from models import LoginSchema,SignUpSchema
from fastapi.responses import JSONResponse
app = FastAPI(
    description="Simple app to show firebase",
    title="firebase auth",
    docs_url='/'
)
import firebase_admin
from firebase_admin import credentials, auth
if not firebase_admin._apps:

    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred)
# Firebase configuration
firebase_config = {
    "apiKey": "",
    "authDomain": "",
    "projectId": "",
    "storageBucket": "",
    "messagingSenderId": "",
    "appId": "",
    "databaseURL":""
}
firebase=pyrebase.initialize_app(firebase_config)


@app.post('/signup')
async def create_an_account(user_data:SignUpSchema):
    username=user_data.username
    email = user_data.email
    full_name=user_data.full_name
    created_at=user_data.created_at

   
    password = user_data.password


    try:
        user = auth.create_user(
            uid = username,
            email = email,
            display_name = full_name,
            created_at=created_at,
            password = password
        )

        return JSONResponse(content={"message" : f"User account created successfuly for user {user.uid}"},
                            status_code= 201
               )
    except auth.EmailAlreadyExistsError:
        raise HTTPException(
            status_code=400,
            detail= f"Account already created for the email {email}"
        )





@app.post('/login')
async def create_access_token(user_data:LoginSchema):
    email = user_data.email
    password = user_data.password

    try:
        user = firebase.auth().sign_in_with_email_and_password(
            email = email,
            password = password
        )

        token = user['idToken']

        return JSONResponse(
            content={
                "token":token
            },status_code=200
        )

    except:
        raise HTTPException(
            status_code=400,detail="Invalid Credentials"
        )



@app.route('/user/<int:user_id>', methods=['PUT'])
async  def update_user_profile(user_id):
    user = next((user for user in users if user["user_id"] == user_id), None)
    if user:
        # Update user profile fields (excluding password)
        data = request.get_json()
        for key, value in data.items():
            if key != 'password':
                user[key] = value
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route('/user/<int:user_id>', methods=['DELETE'])
async def delete_user_account(user_id):
    user = next((user for user in users if user["user_id"] == user_id), None)
    if user:
        users.remove(user)
        return jsonify({"message": "User account deleted"})
    return jsonify({"error": "User not found"}), 404


@app.post('/ping')
async def validate_token(request:Request):
    headers = request.headers
    jwt = headers.get('authorization')

    user = auth.verify_id_token(jwt)

    return user["user_id"]

if __name__ == "__main__":
    uvicorn.run("main:app",reload=True)
