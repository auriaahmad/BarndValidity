from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.utils import qr_code, pdf_generator, excel_generator

router = APIRouter()

@router.post("/batches/", response_model=schemas.ProductBatch)
def create_batch(
    *,
    db: Session = Depends(deps.get_db),
    batch_in: schemas.ProductBatchCreate,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Create new product batch.
    """
    batch = crud.product_batch.create(db=db, obj_in=batch_in)
    return batch

@router.get("/batches/", response_model=List[schemas.ProductBatch])
def read_batches(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Retrieve product batches.
    """
    batches = crud.product_batch.get_multi(db, skip=skip, limit=limit)
    return batches

@router.get("/batches/{batch_id}/qr-codes/pdf")
def get_batch_qr_codes_pdf(
    batch_id: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Generate and download PDF with QR codes for a batch.
    """
    batch = crud.product_batch.get(db=db, id=batch_id)
    if not batch:
        raise HTTPException(status_code=404, detail="Batch not found")
    
    items = crud.product_item.get_by_batch(db=db, batch_id=batch_id)
    qr_codes = []
    for item in items:
        qr_image, verification_url = qr_code.generate_qr_code(item.unique_code)
        qr_codes.append((item.unique_code, qr_image, verification_url))
    
    pdf_buffer = pdf_generator.generate_qr_pdf(
        qr_codes=qr_codes,
        school_name=batch.school_name,
        batch_number=batch.batch_number
    )
    
    return StreamingResponse(
        pdf_buffer,
        media_type="application/pdf",
        headers={
            "Content-Disposition": f"attachment; filename=qr_codes_{batch.batch_number}.pdf"
        }
    )

@router.get("/batches/{batch_id}/qr-codes/excel")
def get_batch_qr_codes_excel(
    batch_id: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Generate and download Excel with QR codes for a batch.
    """
    batch = crud.product_batch.get(db=db, id=batch_id)
    if not batch:
        raise HTTPException(status_code=404, detail="Batch not found")
    
    items = crud.product_item.get_by_batch(db=db, batch_id=batch_id)
    qr_codes = []
    for item in items:
        qr_image, verification_url = qr_code.generate_qr_code(item.unique_code)
        qr_codes.append((item.unique_code, qr_image, verification_url))
    
    excel_buffer = excel_generator.generate_qr_excel(
        qr_codes=qr_codes,
        school_name=batch.school_name,
        batch_number=batch.batch_number
    )
    
    return StreamingResponse(
        excel_buffer,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={
            "Content-Disposition": f"attachment; filename=qr_codes_{batch.batch_number}.xlsx"
        }
    )

@router.get("/verify", response_model=schemas.VerificationResponse)
def verify_product(
    code: str,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Verify a product using its unique code.
    """
    item = crud.product_item.get_by_code(db=db, code=code)
    if not item:
        return schemas.VerificationResponse(
            status="Invalid",
            message="Product not found or invalid code"
        )
    
    if item.is_verified:
        return schemas.VerificationResponse(
            status="Already Verified",
            product_info=item,
            message="This product has already been verified"
        )
    
    # Mark as verified
    item.is_verified = True
    db.add(item)
    db.commit()
    db.refresh(item)
    
    return schemas.VerificationResponse(
        status="Authentic",
        product_info=item,
        message="Product successfully verified"
    ) 