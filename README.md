# FastAPI 기본 틀

FastAPI를 사용하여 REST API를 구축하는 기본적인 틀

1. **명확한 데이터 모델링**: `Item` 클래스를 사용하여 API에서 사용할 데이터 구조를 명확하게 정의하고 데이터 검증을 자동으로 수행.

   ```python:main.py
   class Item(BaseModel):
       name: str
       price: float
       is_offer: bool = None
   ```

2. **비동기 처리**: `async` 키워드를 사용하여 비동기 처리를 지원하고 I/O 작업을 효율적으로 처리하여 높은 동시성을 제공.

   ```python:main.py
   @app.post("/items/")
   async def create_item(item: Item):
       return item
   ```

3. **RESTful API 설계**: RESTful 원칙에 따라 POST 및 GET 요청을 처리하는 엔드포인트를 제공하고 API의 일관성을 유지.

   ```python:main.py
   @app.get("/")
   async def read_root():
       return {"Hello": "World"}
   ```

4. **자동 문서화**: FastAPI는 OpenAPI를 기반으로 API 문서를 자동으로 생성

5. **유연한 확장성**: 이 코드는 기본적인 틀을 제공하므로, 필요에 따라 추가적인 기능이나 엔드포인트를 쉽게 확장.

## 실행 방법

1. **환경 설정**: Python 3.7 이상이 설치되어 있어야 합니다. 가상 환경을 설정하는 것이 좋습니다.

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows
   ```

2. **필요한 패키지 설치**:

   ```bash
   pip install fastapi uvicorn
   ```

3. **애플리케이션 실행**:

   ```bash
   uvicorn main:app --reload
   ```

   여기서 `main`은 Python 파일의 이름이며, `app`은 FastAPI 인스턴스의 이름입니다. `--reload` 플래그는 코드 변경 시 자동으로 서버를 재시작합니다.

4. **API 문서 확인**: 브라우저에서 `http://127.0.0.1:8000/docs`에 접속하여 Swagger UI를 통해 API를 테스트할 수 있습니다.
