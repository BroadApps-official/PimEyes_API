import base64

from openai import AsyncOpenAI

from app.constants.constants import PHOTO_ANALYZE_PROMPT


class HttpOpenAiClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self._client = AsyncOpenAI(api_key=self.api_key)

    async def deep_search(self, query: str) -> str:
        response = await self._client.responses.create(
            model="gpt-4o",
            input=query
        )
        if response.status == "completed":
            return response.output[0].content[0].text
        else:
            return response.id

    async def photo_analyze(self, image_bytes: bytes, content_type: str | None = None):
        if not content_type:
            content_type = "image/jpeg"

        image_b64 = base64.b64encode(image_bytes).decode("utf-8")
        data_url = f"data:{content_type};base64,{image_b64}"

        response = await self._client.responses.create(
            model="gpt-4o",
            input=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "input_text",
                            "text": PHOTO_ANALYZE_PROMPT
                        },
                        {
                            "type": "input_image",
                            "image_url": data_url
                        }
                    ]
                }
            ]
        )
        return response



    async def get_text_response(self, resp_id: str) -> str | None:
        response = await self._client.responses.retrieve(
            response_id=resp_id
        )
        if response.status == "completed":
            return response.output[0].content[0].text
        return None