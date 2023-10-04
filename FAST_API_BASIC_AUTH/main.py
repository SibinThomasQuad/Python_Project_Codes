from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()

# Hardcoded username and password
USERNAME = "username"
PASSWORD = "password"

security = HTTPBasic()

# Define a protected route that requires basic authentication
@app.get("/protected")
async def protected_resource(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username == USERNAME and credentials.password == PASSWORD:
        return {"message": "This is a protected resource."}
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
