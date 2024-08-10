from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from configs import DB_NAME, DB_PASSWORD, DB_USER, DB_PORT, DB_HOST
def get_url() -> str:
    url = f"""mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"""
    return url
SQLALCHEMY_DATABASE_URL = get_url()

# echo: True => generate sql queries in console
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=False)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

async def get_session():
    db = SessionLocal() 
    try:
        yield db
    finally:
        await db.close()