import ollama
from datetime import datetime, timedelta

start_time = datetime.now()

response = ollama.chat(
    model='llama3.2-vision',
    messages=[{
        'role': 'user',
        'content': """You are a handwriting transcriber. Your task is to transcribe the *entire* handwritten text in this image into a *single* JSON object. Transcribe the text exactly as it is written, character by character. If a word or character is completely illegible or unclear, write "[illegible]" in its place. Do not add any additional context, explanations, or analysis. You should only respond with a single JSON object, and it must adhere to the following JSON format:

{
  "transcript": [Transcription here],
  "notes": [Any notes about the transcription process, such as difficulties reading specific characters or overall legibility]
}

For example:
{
  "transcript": "This is a sample transcription. [illegible] word.",
  "notes": "The last word before the period was difficult to decipher due to smudging."
}
""",
        'images': ['sample1.png']
    }]
)

end_time = datetime.now()
time_diff = end_time - start_time

print(response.message.content)
# print(time_diff)