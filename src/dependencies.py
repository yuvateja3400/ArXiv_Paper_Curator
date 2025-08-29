from functools import lru_cache
from typing import Annotated, Generator

from fastapi import Depends, Request

# Week 1: Removed API key authentication for simplicity
from sqlalchemy.orm import Session
from src.config import Settings
from src.db.interfaces.base import BaseDatabase

# Week 1: Simplified - no API key authentication needed for local learning

@lru_cache
def get_settings() -> Settings:
    """Get application settings."""
    return Settings()


def get_request_settings(request: Request) -> Settings:
    """Get settings from the request state."""
    return request.app.state.settings


def get_database(request: Request) -> BaseDatabase:
    """Get database from the request state."""
    return request.app.state.database


def get_db_session(database: Annotated[BaseDatabase, Depends(get_database)]) -> Generator[Session, None, None]:
    """Get database session dependency."""
    with database.get_session() as session:
        yield session


# Week 2+: PDF parser service (not implemented in Week 1)
def get_pdf_parser_service(request: Request):
    """Get PDF parser service from app state (Week 2+ - not implemented yet)."""
    return None


# Week 1: OpenSearch service (placeholder - full implementation in Week 3+)
def get_opensearch_service(request: Request):
    """Get OpenSearch service from app state (Week 3+ - placeholder for Week 1)."""
    return getattr(request.app.state, "opensearch_service", None)


# Phase 3: LLM service (skeleton only)
def get_llm_service(request: Request):
    """Get LLM service from app state (Phase 3 - not implemented yet)."""
    # Phase 3: Will return actual LLM service
    return None


# Dependency type aliases for better type hints
SettingsDep = Annotated[Settings, Depends(get_settings)]
DatabaseDep = Annotated[BaseDatabase, Depends(get_database)]
SessionDep = Annotated[Session, Depends(get_db_session)]
PDFParserServiceDep = Annotated[object, Depends(get_pdf_parser_service)]
OpenSearchServiceDep = Annotated[object, Depends(get_opensearch_service)]
# Phase 3: LLM service dependency (not used in Phase 2)
# LLMServiceDep = Annotated[object, Depends(get_llm_service)]
