import os
import io
from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor

input_path = r"C:\Users\PC\Downloads\2342342342312.pdf"
output_path = r"C:\Users\PC\Downloads\plato_pequeno_blush.pdf"

# Blush Header #fce8e4 from the brand palette
BLUSH_COLOR = HexColor("#fce8e4")

def create_background_page(width, height, color):
    packet = io.BytesIO()
    c = canvas.Canvas(packet, pagesize=(width, height))
    c.setFillColor(color)
    c.rect(0, 0, width, height, fill=1, stroke=0)
    c.save()
    packet.seek(0)
    return PdfReader(packet)

reader = PdfReader(input_path)
writer = PdfWriter()

for i, page in enumerate(reader.pages):
    width = float(page.mediabox.width)
    height = float(page.mediabox.height)
    bg_reader = create_background_page(width, height, BLUSH_COLOR)
    bg_page = bg_reader.pages[0]
    bg_page.merge_page(page)
    writer.add_page(bg_page)
    print(f"  Procesada página {i+1}/{len(reader.pages)}")

with open(output_path, "wb") as f:
    writer.write(f)

print(f"\nListo! Guardado en: {output_path}")
