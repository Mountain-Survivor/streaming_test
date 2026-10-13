import time
import asyncio

words = ["안녕", "나는", "가짜", "AI", "모델이야"]

async def async_batch_model():
    await asyncio.sleep(5)
    return " ".join(words)

def stream_model():
    for word in words:
        time.sleep(1)
        yield word + "\n"

def batch_model():
    time.sleep(5)
    return " ".join(words)

stream_model()
batch_model()