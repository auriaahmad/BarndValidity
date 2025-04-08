from typing import List, Optional
from sqlalchemy.orm import Session
import uuid

from app.crud.base import CRUDBase
from app.models.models import ProductBatch, ProductItem
from app.schemas.product import ProductBatchCreate, ProductItemCreate

class CRUDProductBatch(CRUDBase[ProductBatch, ProductBatchCreate, ProductBatchCreate]):
    def create_with_items(
        self, db: Session, *, obj_in: ProductBatchCreate
    ) -> ProductBatch:
        # Create batch
        db_obj = ProductBatch(
            school_name=obj_in.school_name,
            product_type=obj_in.product_type,
            batch_number=obj_in.batch_number,
            quantity=obj_in.quantity,
        )
        db.add(db_obj)
        db.flush()  # Get the batch ID
        
        # Create items
        for i in range(obj_in.quantity):
            unique_code = f"{obj_in.batch_number}_{str(uuid.uuid4())[:8]}"
            item = ProductItem(
                batch_id=db_obj.id,
                unique_code=unique_code,
            )
            db.add(item)
        
        db.commit()
        db.refresh(db_obj)
        return db_obj

class CRUDProductItem(CRUDBase[ProductItem, ProductItemCreate, ProductItemCreate]):
    def get_by_code(self, db: Session, *, code: str) -> Optional[ProductItem]:
        return db.query(ProductItem).filter(ProductItem.unique_code == code).first()
    
    def get_by_batch(
        self, db: Session, *, batch_id: int, skip: int = 0, limit: int = 100
    ) -> List[ProductItem]:
        return (
            db.query(ProductItem)
            .filter(ProductItem.batch_id == batch_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

product_batch = CRUDProductBatch(ProductBatch)
product_item = CRUDProductItem(ProductItem) 