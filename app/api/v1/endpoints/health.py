from fastapi import APIRouter

router = APIRouter(tags=["Health"])

@router.get("/health")

async def health():

    return {

        "status": "healthy",

        "message": "AI Data Analyst API is running",

    }