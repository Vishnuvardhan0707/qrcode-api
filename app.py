from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
import qrcode
import io

# Create the FastAPI app
app = FastAPI(
    title="QR Code API",
    description="Simple API that takes text and returns a QR code image.",
    version="1.0.0",
)

#@app.get("/")
#def read_root():
#    return {"message": "QR Code API is running. Go to /docs to test."}

@app.get("/qr")
def create_qr(text: str):
    """
    Example:
    GET /qr?text=HelloWorld
    Returns: PNG image of QR code
    """
    if not text:
        raise HTTPException(status_code=400, detail="Query parameter 'text' is required")

    # Create QR image in memory (no files on disk)
    img = qrcode.make(text)
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)

    return StreamingResponse(buf, media_type="image/png")
