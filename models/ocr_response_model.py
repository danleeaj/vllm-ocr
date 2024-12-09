from pydantic import BaseModel
from typing import Optional

class OCRResponseModel(BaseModel):
    """
    Represents the response from the OCR agent.

    Attributes:
        transcript (str): The transcription from the OCR agent.
        notes (str): The notes on the transcription.
    """
    transcript: str
    notes: Optional[str]
