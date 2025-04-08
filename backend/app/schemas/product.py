from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class ProductBatchBase(BaseModel):
    school_name: str
    product_type: str
    batch_number: str
    quantity: int

class ProductBatchCreate(ProductBatchBase):
    pass

class ProductBatchUpdate(ProductBatchBase):
    school_name: Optional[str] = None
    product_type: Optional[str] = None
    batch_number: Optional[str] = None
    quantity: Optional[int] = None

class ProductBatch(ProductBatchBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True

class ProductItemBase(BaseModel):
    unique_code: str

class ProductItemCreate(ProductItemBase):
    batch_id: int

class ProductItem(ProductItemBase):
    id: int
    batch_id: int
    is_verified: bool
    verification_date: Optional[datetime]
    created_at: datetime

    class Config:
        from_attributes = True

class QRCodeResponse(BaseModel):
    unique_code: str
    verification_url: str
    qr_code_image: bytes

class BatchQRResponse(BaseModel):
    batch: ProductBatch
    qr_codes: List[QRCodeResponse]

class VerificationResponse(BaseModel):
    status: str
    product_info: Optional[ProductItem] = None
    message: str 