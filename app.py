from flask import Flask, request, redirect, render_template, flash

from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

#from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adoption_wtforms'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'i_have_a_secret_5'
app.config['SQLALCHEMY_ECHO'] = False
# debug = DebugToolbarExtension(app)

connect_db(app)


@app.route("/")
def home():
    """Home Page: Shows Available pets first, then pets that are unavailable"""
    pets_available = db.session.query(Pet).filter(Pet.available).all()
    pets_not_available = db.session.query(Pet).filter(
        Pet.available == 'n').all()
    return render_template("index.html",
                           pets_available=pets_available,
                           pets_not_available=pets_not_available)


@app.route("/<int:pet_id>", methods=["GET", "POST"])
def pet_details(pet_id):
    """Pet Details Page: Edit form enabled on this page. Disables input
    for values which cannot be changed."""
    pet = db.get_or_404(Pet, pet_id)
    form = EditPetForm(obj=pet)
    form.hidden_species = pet.species
    form.hidden_available = pet.available
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = (True if form.available.data else False)
        db.session.verified = True
        db.session.commit()
        flash(f"Updated {pet}")
        form.hidden_available = pet.available
        return redirect(f"/{pet_id}")
    else:
        for field, errors in form.errors.items():
            for error in errors:
                print(f"Error for field '{field}': {error}")
        form = EditPetForm(obj=pet)
        form.hidden_species = pet.species
        form.hidden_available = pet.available
        return render_template(
            "pet_edit_form.html", form=form, pet=pet)


@app.route("/add", methods=["GET", "POST"])
def add_new_pet():
    """Adds a new pet, form validation is done on the server side and
    set explicitly in model"""
    form = AddPetForm()
    # Form validation
    if form.validate_on_submit():
        pet = Pet(
            name=form.name.data,
            species=form.species.data)
        db.session.add(pet)
        db.session.commit()
        pet.photo_url = (form.photo_url.data if form.photo_url.data and len(
            form.photo_url.data) > 0 else pet.photo_url)
        pet.age = (form.age.data if form.age.data and form.age.data >= 0
                   else pet.age)
        pet.notes = (form.notes.data if form.notes.data and len(
            form.notes.data) > 0 else pet.notes)
        db.session.verified = (form.photo_url.data and
                               len(form.photo_url.data) > 0) or \
                              (form.age.data and form.age.data >= 0) or \
                              (form.notes.data and len(form.notes.data) > 0)
        db.session.commit()
        flash(f"Pet {pet.name} "
              f"({pet.species}) "
              f"added!")
        return redirect("/")
    else:
        return render_template(
            "pet_add_form.html", form=form)
