from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException
from typing import List

from ..models import ProductReview, UpdateProductReview

router = APIRouter()


# Create
@router.post("/", response_description="Review added to the database")
async def add_product_review(review: ProductReview) -> dict:
    await review.create()
    return {"message": "Review added successfully"}


# Read by id
@router.get("/{id}", response_description="Review record retrieved")
async def get_review_record(object_id: PydanticObjectId) -> ProductReview:
    review = await ProductReview.get(object_id)
    return review


# Read all
@router.get("/", response_description="Review records retrieved")
async def get_reviews() -> List[ProductReview]:
    reviews = await ProductReview.find_all().to_list()
    return reviews


# Update
@router.put("/{id}", response_description="Review record updated")
async def update_student_data(object_id: PydanticObjectId, req: UpdateProductReview) -> ProductReview:
    req = {k: v for k, v in req.dict().items() if v is not None}
    update_query = {"$set": {
        field: value for field, value in req.items()
    }}

    review = await ProductReview.get(object_id)
    if not review:
        raise HTTPException(
            status_code=404,
            detail="Review record not found!"
        )

    await review.update(update_query)
    return review


# Delete
@router.delete("/{id}", response_description="Review record deleted from the database")
async def delete_student_data(object_id: PydanticObjectId) -> dict:
    record = await ProductReview.get(object_id)

    if not record:
        raise HTTPException(
            status_code=404,
            detail="Review record not found!"
        )

    await record.delete()
    return {
        "message": "Record deleted successfully"
    }
