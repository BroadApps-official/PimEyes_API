from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel

from app.application.clients.openai.http_openai_client import HttpOpenAiClient
from app.core.config import get_settings

router = APIRouter(tags=["generation"])

settings = get_settings()
client = HttpOpenAiClient(api_key=settings.gpt_api_key)

class DeepSearchPostRequest(BaseModel):
    query: str


@router.post("/deep_search")
async def deep_search(body: DeepSearchPostRequest):
    return await client.deep_search(body.query)



@router.post("/photo")
async def photo_analyze(file: UploadFile = File(...)):
    file_bytes = await file.read()

    response = await client.photo_analyze(file_bytes, file.content_type)
    return response



@router.get("/get_response")
async def get_response(response_id: str):
    return await client.get_text_response(response_id)
