from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/version")
async def get_ffmpeg_version():
    try:
        result = subprocess.run(["ffmpeg", "-version"], capture_output=True, text=True)
        if result.returncode == 0:
            return {"ffmpeg_version": result.stdout}
        else:
            return {"error": "Failed to get ffmpeg version"}
    except FileNotFoundError:
        return {"error": "ffmpeg executable not found"}
