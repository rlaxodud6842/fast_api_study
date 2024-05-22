from fastapi import FastAPI, Form
from fastapi.responses import FileResponse

app = FastAPI()

#html 파일 전송법
@app.get("/")
def main():
    return FileResponse('main.html')
from pydantic import BaseModel

class Model(BaseModel):
    id : str
    passwd : str

@app.post("/login")
async def login(userName: str = Form(...), userPassword: str = Form(...)):
    print(f"Username: {userName}, Password: {userPassword}")
    # 실제 인증 로직을 여기에 추가할 수 있습니다.
    return {"message": "로그인 완료"}