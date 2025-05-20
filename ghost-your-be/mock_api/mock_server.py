from fastapi import FastAPI, HTTPException
from .api_generator import APIGenerator
import uvicorn
import os

app = FastAPI(title="Mockmatic API", description="Mock API cho dữ liệu giả", version="0.1.0")

@app.get("/mock/{endpoint}")
async def mock_endpoint(endpoint: str, count: int = 5):
    """Tạo dữ liệu giả cho endpoint được chỉ định."""
    schema_path = os.environ.get("SCHEMA_PATH")
    if not schema_path:
        raise HTTPException(status_code=500, detail="SCHEMA_PATH không được thiết lập")
    
    try:
        generator = APIGenerator(schema_path)
        response = generator.generate_response(endpoint, count)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi khi tạo dữ liệu: {str(e)}")

def run_mock_server(host="0.0.0.0", port=8000):
    """Chạy mock API server."""
    uvicorn.run(app, host=host, port=port)