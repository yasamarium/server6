import os
from pathlib import Path
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

class Settings:
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "8000"))
    API_KEY: str = os.getenv("API_KEY", "qwen3-direct-access")
    MODEL_NAME: str = os.getenv("MODEL_NAME", "qwen-0.5b")
    MODEL_FILE: str = os.getenv("MODEL_FILE", "qwen2.5-0.5b-instruct-q4_k_m.gguf")
    MODEL_PATH: str = os.getenv(
        "MODEL_PATH",
        str(Path(__file__).resolve().parent.parent / "models" / os.getenv("MODEL_FILE", "qwen2.5-0.5b-instruct-q4_k_m.gguf")),
    )
    MODEL_URL: str = os.getenv("MODEL_URL", "https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF/resolve/main/qwen2.5-0.5b-instruct-q4_k_m.gguf")
    MODEL_SHA256: Optional[str] = os.getenv("MODEL_SHA256", None)
    THREADS: int = int(os.getenv("THREADS", str(os.cpu_count() or 2)))
    CONTEXT_SIZE: int = int(os.getenv("CONTEXT_SIZE", "2048"))
    BATCH_SIZE: int = int(os.getenv("BATCH_SIZE", "512"))
    MAX_TOKENS: int = int(os.getenv("MAX_TOKENS", "512"))
    TEMPERATURE: float = float(os.getenv("TEMPERATURE", "0.7"))
    MOCK_MODEL: bool = os.getenv("MOCK_MODEL", "false").lower() in ("true", "1", "yes")
    RESTART_INTERVAL_SECONDS: int = int(os.getenv("RESTART_INTERVAL_SECONDS", "18000"))

settings = Settings()
