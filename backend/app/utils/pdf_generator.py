from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO
from typing import List, Tuple

def generate_qr_pdf(qr_codes: List[Tuple[str, BytesIO, str]], school_name: str, batch_number: str) -> BytesIO:
    """
    Generate a PDF containing QR codes in a grid layout.
    Each QR code is labeled with its unique code.
    """
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()
    
    # Add header
    header = Paragraph(f"School: {school_name}<br/>Batch: {batch_number}", styles["Heading1"])
    elements.append(header)
    
    # Create a grid of QR codes (4 per row)
    data = []
    row = []
    for i, (unique_code, qr_image, _) in enumerate(qr_codes):
        # Convert BytesIO to Image
        qr_image.seek(0)
        img = Image(qr_image, width=100, height=100)
        
        # Create a cell with QR code and label
        cell = [[img], [unique_code]]
        row.append(cell)
        
        if len(row) == 4 or i == len(qr_codes) - 1:
            data.append(row)
            row = []
    
    # Create table
    table = Table(data, colWidths=[150] * 4, rowHeights=[150] * len(data))
    table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    
    elements.append(table)
    doc.build(elements)
    buffer.seek(0)
    return buffer 