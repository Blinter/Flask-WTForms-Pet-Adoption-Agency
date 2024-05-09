from flask_wtf import FlaskForm
from wtforms import (validators, StringField, TextAreaField, IntegerField,
                     FloatField, RadioField, BooleanField, HiddenField)


class AddPetForm(FlaskForm):
    """Form for adding Pets."""

    """Must be filled"""
    name = StringField("Pet Name", [
        validators.Length(3, 128),
        validators.InputRequired(message='Pet Name cannot be empty'),
        ],
                     render_kw={
                         'class': "form-control form-control-lg",
                         'placeholder': 'Pet Name'
                     })

    """Only three possible choices"""
    species = RadioField("Species", choices=[("dog", "Dog"), ("cat", "Cat"),
                                             ("porcupine", "Porcupine")],
                         validators=[
                             validators.InputRequired(
                                 message='Species must be filled out'),
                             validators.AnyOf(["dog", "cat", "porcupine"])
                         ],
                         render_kw={
                             'class': "form-check-input"
                         })

    """Additional checking for URL using external libraries"""
    photo_url = StringField("Photo URL", [
        validators.Length(0, 128, message="Photo URL must be less than 128 "
                                          "characters long"),
        validators.URL(require_tld=True, message="URL must contain a .tld"),
        validators.Optional(),
    ],
                     render_kw={
                         'class': "form-control form-control-lg",
                         'placeholder': 'Photo URL'
                     })

    """Age can only be between 0 and 30"""
    age = FloatField("Age", [
        validators.NumberRange(min=0, max=30, message=f"Age must be between "
                                                      f"{min}"
                                                      f" and {max}"),
        validators.Optional(),
        ],
                     render_kw={
                         'class': "form-control form-control-lg",
                         'placeholder': 'Age Between 0 and 30'
                     })

    """Additional variables for input size checking in test_flask_long_forms"""
    notes = TextAreaField("Notes", [
        validators.Length(0, 65535),
        validators.Optional(),
        ],
                          render_kw={
                              'class': "form-control",
                              'placeholder': 'Other notes about your pet'
                          })


class EditPetForm(FlaskForm):
    """Form for Editing Pets."""

    """Must be filled"""
    name = StringField("Pet Name", [
        validators.Optional(),
        ])

    """Only three possible choices"""
    species = RadioField("Species", choices=[("dog", "Dog"), ("cat", "Cat"),
                                             ("porcupine", "Porcupine")],
                         validators=[validators.Optional(),],
                         render_kw={
                             'class': "form-check-input"
                         })
    hidden_species = HiddenField()

    """Additional checking for URL using external libraries"""
    photo_url = StringField("Photo URL", [
        validators.Length(0, 128, message="Photo URL must be less than 128 "
                                          "characters long"),
        validators.URL(require_tld=True, message="URL must contain a .tld"),
        validators.Optional(),
    ])

    """Age can only be between 0 and 30"""
    age = IntegerField("Age", [
        validators.NumberRange(min=0, max=30, message="Age must be between 0"
                                                      " and 30"),
        validators.Optional(),
        ])

    """Additional variables for input size checking in test_flask_long_forms"""
    notes = TextAreaField("Notes", [
        validators.Length(0, 65535),
        validators.Optional(),
        ])

    """Availability Check"""
    available = BooleanField("Available", [
        validators.Optional()
        ])
    hidden_available = HiddenField()
