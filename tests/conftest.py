"""Main test configuration and fixtures."""

import pytest
from polyfactory.factories.pydantic_factory import ModelFactory
from src.config import Settings
from src.schemas.ask import AskRequest, PaperSource
from src.schemas.paper import PaperCreate, PaperResponse


@pytest.fixture
def settings() -> Settings:
    """Test settings fixture."""
    return Settings()


class PaperCreateFactory(ModelFactory[PaperCreate]): ...


class PaperResponseFactory(ModelFactory[PaperResponse]): ...


class AskRequestFactory(ModelFactory[AskRequest]): ...


class PaperSourceFactory(ModelFactory[PaperSource]): ...


@pytest.fixture
def paper_create_data() -> PaperCreate:
    """Mock paper creation data."""
    return PaperCreateFactory.build()


@pytest.fixture
def paper_response_data() -> PaperResponse:
    """Mock paper response data."""
    return PaperResponseFactory.build()


@pytest.fixture
def ask_request_data() -> AskRequest:
    """Mock ask request data."""
    return AskRequestFactory.build()


@pytest.fixture
def paper_source_data() -> PaperSource:
    """Mock paper source data."""
    return PaperSourceFactory.build()
