import os
from tortoise import Tortoise
from dotenv import load_dotenv

load_dotenv()


async def init_db():
    await Tortoise.init(
        db_url=(
            f"postgres://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}"
            f"@{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"
        ),
        modules={"models": ["app.models"]},
    )
    await Tortoise.generate_schemas()
