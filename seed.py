from models import db, Pet
from app import app
import sqlalchemy as db2
from sqlalchemy_utils import database_exists, create_database
from app_long_forms import *

engine = db2.create_engine('postgresql:///pet_adoption_wtforms')
if not database_exists(engine.url):
    create_database(engine.url, encoding='SQL_ASCII')
with app.app_context():
    db.drop_all()
    db.create_all()
    pet1 = Pet(
        name="Scruffy",
        species="Dog",
        photo_url="https://via.placeholder.com/150",
        age=2,
        notes="",
        available=True
    )
    pet2 = Pet(
        name="Rocket",
        species="Dog",
        photo_url="https://via.placeholder.com/150",
        age=1,
        notes="",
        available=True
    )
    pet3 = Pet(
        name="Awoo",
        species="Dog",
        photo_url="https://via.placeholder.com/150",
        age=5,
        notes="",
        available=False
    )
    pet4 = Pet(
        name="Spider",
        species="Porcupine",
        photo_url="https://via.placeholder.com/150",
        age=2,
        notes="",
        available=False
    )
    pet5 = Pet(
        name="Aliyah",
        species="Cat",
        photo_url="https://via.placeholder.com/150",
        age=0,
        notes="",
        available=False
    )
    pet6 = Pet(
        name="Powa",
        species="Cat",
        photo_url="https://via.placeholder.com/150",
        age=3,
        notes=long_text_3677,
        available=False
    )
    try:
        db.session.add_all([pet1, pet2, pet3, pet4, pet5, pet6])
        db.session.commit()
        print("Database seeded successfully!")
    except Exception as e:
        print(f"Error committing data: {e}")
