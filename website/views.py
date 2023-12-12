from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
import json
from . import db 


views = Blueprint('views', __name__)
##? setting up a blueprint from our views in Flask application

@views.route('/', methods=['GET', 'POST'])
@login_required
##? cannot redirect/return to the home page unless and until the user is logged in
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category="input_error")
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()

            flash('Note added', category='success')
    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    ##? the above function expects a JSON from the deleteNote function
    noteID = note['noteId']
    note = Note.query.get(noteID)

    if note:
        if note.user_id == current_user.id:
        ##? preventing deleting notes of other users
            db.session.delete(note)
            db.session.commit()
            
    return jsonify({})
    ##? returning empty response