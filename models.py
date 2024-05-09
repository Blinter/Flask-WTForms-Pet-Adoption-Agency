"""Models for WTForms-Adoption Agency."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """Pet"""

    __tablename__ = "pets"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)

    name = db.Column(db.String(128),
                     nullable=False)

    species = db.Column(db.String(9),
                        nullable=False,
                        default="Dog")

    photo_url = db.Column(db.String(128),
                          nullable=True)

    age = db.Column(db.SmallInteger,
                    nullable=True)

    notes = db.Column(db.String(5000),
                      nullable=True)

    available = db.Column(db.Boolean,
                          nullable=False,
                          default=True)

    @property
    def get_available(self):
        return "Yes" if self.available else "No"

    def __repr__(self):
        """Show info about post."""

        return (f"<Pet id={str(self.id)} "
                f"name={self.name} "
                f"species={self.species} " +
                (f"photo_url={self.photo_url[:24]} " if self.photo_url and
                len(self.photo_url) > 0 else '') +
                (f"age={str(self.age)} " if self.age and self.age >= 0 else '')
                +
                (f"notes={self.notes[:32]} " if self.notes and len(self.notes)
                 > 0 else '') +
                f"available={str(self.get_available)}>")

