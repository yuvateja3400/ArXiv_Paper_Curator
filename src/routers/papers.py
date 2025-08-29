from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from src.dependencies import SessionDep
from src.repositories.paper import PaperRepository
from src.schemas.paper import PaperResponse

router = APIRouter(prefix="/papers", tags=["papers"])


@router.get("/{arxiv_id}", response_model=PaperResponse)
def get_paper_details(
    db: SessionDep,
    arxiv_id: str = Path(
        ..., description="arXiv paper ID (e.g., '2401.00001' or '2401.00001v1')", regex=r"^\d{4}\.\d{4,5}(v\d+)?$"
    ),
) -> PaperResponse:
    """Get details of a specific paper by arXiv ID."""
    paper_repo = PaperRepository(db)
    paper = paper_repo.get_by_arxiv_id(arxiv_id)

    if not paper:
        raise HTTPException(status_code=404, detail="Paper not found")

    return PaperResponse.model_validate(paper)
