"""Models for adopt app."""

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


DEFAULT_IMAGE_URL = '/static/default-image.jpg'


def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """
    app.app_context().push()
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """Pet."""
    __tablename__ = "pets"
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True)

    name = db.Column(
        db.String(50),
        nullable=False,
        unique=True
    )

    species = db.Column(
        db.String(30),
        nullable=False
    )

    photo_url = db.Column(
        db.String,
        nullable=False,
        default=""
    )

    age = db.Column(
        db.String(10),
        #TODO: Make this work? Do we need to if it's a drop-down select?
        # db.CheckConstraint("age in ['baby', 'young', 'adult', 'senior']"),
        nullable=False
    )

    notes = db.Column(
        db.String
    )

    available = db.Column(
        db.Boolean,
        nullable=False,
        default=True
    )
