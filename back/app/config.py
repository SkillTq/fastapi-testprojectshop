from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str  = "FastAPI Shop"
    debug: bool = True
    database_ulr = "sqlite:///./shop.db"
    cors_origins: list = [
        "http://localhost:5173",
        "http://localhost:3000",
        "http://localhost:5173",
        "http://localhost:3000",
    ]
    static_dir: str = "static"
    image_dir: str = "static/image"
    
    class Config:
        env_file = ".env"

settings = Settings()