import re
import base64
from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import Response
# 1. CORS-Modul importieren
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Minimal Dynamic SVG Placeholder API",
    version="1.0.0"
)

# 2. CORS aktivieren, damit lokale HTML-Dateien die API abfragen dürfen
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Erlaubt alle Quellen (inklusive lokaler file:/// Dateien)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

HEX_COLOR_PATTERN = re.compile(r"^([A-Fa-f0-9]{3}|[A-Fa-f0-9]{6})$")

def validate_color(color: str, default: str) -> str:
    if color and HEX_COLOR_PATTERN.match(color):
        return f"#{color}"
    return f"#{default}"

@app.get("/placeholder/{size}")
def get_placeholder(
    size: str, 
    bg: str = Query(default="eeeeee"), 
    text_color: str = Query(default="aaaaaa"),
    text: str = Query(default=None)
):
    try:
        if "x" in size.lower():
            width_str, height_str = size.lower().split("x")
            width = int(width_str)
            height = int(height_str)
        else:
            width = height = int(size)
            
        if width <= 0 or height <= 0:
            raise ValueError
    except ValueError:
        raise HTTPException(status_code=400, detail="Ungültiges Format.")

    bg_color = validate_color(bg, "eeeeee")
    txt_color = validate_color(text_color, "aaaaaa")
    display_text = text if text else f"{width} x {height}"
    font_size = max(12, min(width, height) * 0.08)

    svg_content = f"""<svg xmlns='http://w3.org' width='{width}' height='{height}' viewBox='0 0 {width} {height}'>
  <rect width='100%' height='100%' fill='{bg_color}'/>
  <text x='50%' y='50%' font-family='Arial, sans-serif' font-size='{font_size}px' fill='{txt_color}' dominant-baseline='middle' text-anchor='middle'>
    {display_text}
  </text>
</svg>"""

    svg_bytes = svg_content.encode("utf-8")
    base64_encoded = base64.b64encode(svg_bytes).decode("utf-8")
    data_url = f"data:image/svg+xml;base64,{base64_encoded}"

    return Response(content=data_url, media_type="text/plain")
