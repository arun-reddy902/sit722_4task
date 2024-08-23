import os

class Settings:
    DATABASE_URL: str = os.getenv("postgresql://arunreddy_902_user:9cu30xeoee9L9eyaDw6Y34rnntf2K0Mm@dpg-cr3nfbd6l47c73a8is0g-a.oregon-postgres.render.com/arunreddy_902")

settings = Settings()
