import logging
from typing import Dict

import httpx
from src.config import Settings

logger = logging.getLogger(__name__)


class OllamaClient:
    """Minimal Ollama client for Week 1 health checks."""

    def __init__(self, settings: Settings):
        self.base_url = settings.ollama_host

    async def health_check(self) -> Dict[str, str]:
        """Check if Ollama service is available."""
        try:
            async with httpx.AsyncClient(timeout=5.0) as client:
                response = await client.get(f"{self.base_url}/api/tags")
                if response.status_code == 200:
                    return {"status": "healthy", "message": "Ollama service is running"}
                else:
                    return {"status": "unhealthy", "message": f"HTTP {response.status_code}"}
        except Exception as e:
            logger.error(f"Ollama health check failed: {e}")
            return {"status": "unhealthy", "message": str(e)}
