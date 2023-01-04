from beanie import init_beanie
import motor.motor_asyncio

from .models import ProductReview


async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(
        "mongodb://localhost:27017/productreviews"
    )

    await init_beanie(database=client.review_db, document_models=[ProductReview])  # Array of models
