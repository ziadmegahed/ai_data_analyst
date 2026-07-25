from dataclasses import dataclass
from uuid import UUID
from datetime import datetime
from app.domain.enums.analysis_status import AnalysisStatus

@dataclass
class AnalysisJob:
    id: UUID
    filename: str
    status: AnalysisStatus
    created_at: datetime
