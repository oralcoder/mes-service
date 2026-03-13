from fastapi import FastAPI, Depends, HTTPException, Request 
from sqlalchemy import text
from sqlalchemy.orm import Session
from core.database import get_db 
from fastapi.responses import HTMLResponse    # HTML 응답을 반환하기 위한 클래스
from core.templates import templates          # Jinja2 템플릿 설정 불러오기
from core.init_database import create_tables
from core.init_master_data import seed_master_data
from routers import work
from routers import quality
from routers import equipment

app = FastAPI()

@app.on_event("startup")
def startup_event():
    create_tables()
    seed_master_data() 
    print("데이터베이스 테이블 초기화 완료")

@app.get("/", response_class=HTMLResponse)     # HTMLResponse를 사용하여 HTML 페이지 반환  
def read_root(request: Request):               # Request 객체를 매개변수로 받음
    return templates.TemplateResponse(         # 템플릿 렌더링
	    "main.html",                             # 사용할 템플릿 파일명
	    {"request": request, "title":"메인", "message":"FastAPI with Jinja2!"} # 템플릿에 전달할 데이터
    )

app.include_router(work.router, prefix="/work")
app.include_router(quality.router, prefix="/quality")
app.include_router(equipment.router, prefix="/equipment")