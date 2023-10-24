from flask import Flask, render_template
from config import SQLALCHEMY_DATABASE_URI, db
from models import Nouns, Adjectives, Verbs
from app import db
import random 

from flask import jsonify
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
db.init_app(app)
app.app_context().push()
db.create_all()
@app.route('/')
def home():
    """
    Renders the 'home.html' template.

    Returns:
    - A rendered HTML page for the home page.
    """
    return render_template('home.html')

@app.route('/get_all_verb_data')
def get_all_verb_data():
    """
    Retrieves and shuffles data from the Verbs table and returns it as JSON.

    Returns:
    - JSON representation of shuffled verb data.
    - If an exception occurs, returns an error JSON with a 500 status code.
    """
    try:
        verbs = Verbs.query.all()

        random.shuffle(verbs)

        # Create a list to store the shuffled verb data
        verb_list = []

        # Iterate over the shuffled verbs and create a dictionary for each
        for verb in verbs:
            verb_data = {
                'word': verb.word,
                'sentence': verb.sentence,
                'definition': verb.definition,
                'past': verb.past,
            }
            verb_list.append(verb_data)

        # Return the shuffled verb list as JSON
        return jsonify(verb_list)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    
@app.route('/verb_review')
def verb_review():
    """
    Renders the 'verb_review.html' template.

    Returns:
    - A rendered HTML page for verb review.
    """
    return render_template('verb_review.html')

@app.route('/get_all_adjective_data')
def get_all_adjective_data():
    """
    Retrieves and shuffles data from the Adjectives table and returns it as JSON.

    Returns:
    - JSON representation of shuffled adjective data.
    - If an exception occurs, returns an error JSON with a 500 status code.
    """
    try:
        adjectives = Adjectives.query.all()

        random.shuffle(adjectives)

        adjective_list = []

        for adjective in adjectives:
            adjective_data = {
                'word': adjective.word,
                'sentence': adjective.sentence,
                'definition': adjective.definition,
            }
            adjective_list.append(adjective_data)

        # Return the shuffled adjective list as JSON
        return jsonify(adjective_list)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/adjective_review')
def adjective_review():
    """
    Renders the 'adjective_review.html' template.

    Returns:
    - A rendered HTML page for adjective review.
    """
    return render_template('adjective_review.html')

@app.route('/get_all_noun_data')
def get_all_noun_data():
    """
    Retrieves and shuffles data from the Nouns table and returns it as JSON.

    Returns:
    - JSON representation of shuffled noun data.
    - If an exception occurs, returns an error JSON with a 500 status code.
    """
    try:
        nouns = Nouns.query.all()

        random.shuffle(nouns)

        # Create a list to store the shuffled noun data
        noun_list = []

        # Iterate over the shuffled nouns and create a dictionary for each
        for noun in nouns:
            noun_data = {
                'word': noun.word,
                'plural': noun.plural,
                'gender': noun.gender,
                'sentence': noun.sentence,
                'definition': noun.definition,
            }
            noun_list.append(noun_data)
        final = jsonify(noun_list)

        return final

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/noun_review')
def noun_review():
    """
    Renders the 'noun_review.html' template.

    Returns:
    - A rendered HTML page for noun review.
    """
    return render_template('noun_review.html')

def push(nouns, adj, verbs):
    """
    Adds lists of noun, adjective, and verb objects to the database.

    Args:
    - nouns (list): A list of Nouns objects to be added to the database.
    - adj (list): A list of Adjectives objects to be added to the database.
    - verbs (list): A list of Verbs objects to be added to the database.
    """
    for e in nouns:
        db.session.add(e)
        db.session.commit()
    for i in adj:
        db.session.add(i)
        db.session.commit()
    for v in verbs:
        db.session.add(v)
        db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
