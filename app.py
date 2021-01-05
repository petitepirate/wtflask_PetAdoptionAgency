from flask import Flask, url_for, render_template, redirect, flash, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField
from models import Pet, db, connect_db
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "shenanigans"

connect_db(app)

# toolbar = DebugToolbarExtension(app)


@app.route("/")
def pet_list():
    """Get list of pets and show them on the homepage"""

    pets = Pet.query.all()
    return render_template("petlist.html", pets=pets)


@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Add a pet."""

    form = AddPetForm()

    species = [(s.species, s.species) for s in Pet.query.all()]
    form.species.choices = species

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data or None
        age = form.age.data
        notes = form.notes.data
        
        newPet = Pet(name = name, species = species, photo_url = photo_url or None, age = age, notes = notes)
        db.session.add(newPet)
        db.session.commit()


        return redirect("/")
    else:
        # re-present form for editing
        return render_template("addpetform.html", form=form)


@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    """Edit pet."""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    species = [(s.species, s.species) for s in Pet.query.all()]
    form.species.choices = species

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data or None
        pet.available = form.available.data
        db.session.commit()
        flash(f"{pet.name} updated.")
        return redirect(url_for('pet_list'))

    else:
        # failed; re-present form for editing
        return render_template("editpetform.html", form=form, pet=pet)


# @app.route("/api/pets/<int:pet_id>", methods=['GET'])
# def api_get_pet(pet_id):
#     """Return basic info about pet in JSON."""

#     pet = Pet.query.get_or_404(pet_id)
#     info = {"name": pet.name, "age": pet.age}

#     return jsonify(info)
