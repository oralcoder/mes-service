# 베이스 이미지 설정
FROM python:3.11

# 컨테이너 내부의 메인 디렉토리 설정
WORKDIR /app

# Python package 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# app 폴더(Host의 app 디렉토리를 컨테이너의 app 디렉토리로 복사)
# 주석 처리된 이유: Docker Compose에서 volume으로 마운트하기 때문에 불필요
# COPY ./app /app

# 서버 실행 명령
# 개발 환경에서는 --reload 옵션을 사용하여 코드 변경 시 자동 재시작
CMD ["python",  "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]