import qrcode
from io import BytesIO
from typing import Tuple
from app.core.config import settings

def generate_qr_code(unique_code: str) -> Tuple[BytesIO, str]:
    """
    Generate a QR code for a product item.
    Returns a tuple of (BytesIO object containing the QR code image, verification URL)
    """
    verification_url = f"{settings.QR_CODE_BASE_URL}?code={unique_code}"
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(verification_url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Convert to BytesIO
    img_byte_arr = BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    
    return img_byte_arr, verification_url

def generate_qr_codes_batch(batch_size: int, prefix: str) -> list:
    """
    Generate multiple QR codes for a batch of products.
    Returns a list of tuples (unique_code, QR code image BytesIO, verification URL)
    """
    qr_codes = []
    for i in range(batch_size):
        unique_code = f"{prefix}_{i+1}"
        img_byte_arr, verification_url = generate_qr_code(unique_code)
        qr_codes.append((unique_code, img_byte_arr, verification_url))
    return qr_codes 