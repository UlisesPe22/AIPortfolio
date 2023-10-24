from app import db
class Nouns(db.Model):
    """
    This class represents the Nouns table in the database.
    It stores information about German nouns, including their word, sentence, definition, gender, and plural form.
    """
    __tablename__ = 'Vocabulary_Nouns'
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(255))
    sentence = db.Column(db.String(255))
    definition = db.Column(db.String(255))
    gender = db.Column(db.String(255))
    plural = db.Column(db.String(255))
    def __init__(self, word, sentence, definition, gender, plural):
        """
        Initializes a new Nouns instance with the provided data.

        :param word: The German noun word.
        :param sentence: A sentence using the noun.
        :param definition: The definition of the noun.
        :param gender: The gender of the noun.
        :param plural: The plural form of the noun.
        """
        self.word = word
        self.sentence = sentence
        self.definition = definition
        self.gender = gender
        self.plural = plural
class Verbs(db.Model): 
    """
    This class represents the Verbs table in the database.
    It stores information about German verbs, including their word, sentence, definition, and past tense form.
    """ 
    __tablename__ = 'Vocabulary_Verbs'
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(255))
    sentence = db.Column(db.String(255))
    definition = db.Column(db.String(255))
    past = db.Column(db.String(255))
    def __init__(self, word, sentence, definition,past):
        """
        Initializes a new Verbs instance with the provided data.

        :param word: The German verb word.
        :param sentence: A sentence using the verb.
        :param definition: The definition of the verb.
        :param past: The past tense form of the verb.
        """
        self.word = word
        self.sentence = sentence
        self.definition = definition   
        self.past = past  
class Adjectives(db.Model):
    """
    This class represents the Adjectives table in the database.
    It stores information about German adjectives, including their word, sentence, definition, and plural form.
    """
    __tablename__ = 'Vocabulary_Adjectives'
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(255))
    sentence = db.Column(db.String(255))
    definition = db.Column(db.String(255))
    plural = db.Column(db.String(255))

    def __init__(self, word, sentence, definition, plural):
        """
        Initializes a new Adjectives instance with the provided data.

        :param word: The German adjective word.
        :param sentence: A sentence using the adjective.
        :param definition: The definition of the adjective.
        :param plural: The plural form of the adjective.
        """
        self.word = word
        self.sentence = sentence
        self.definition = definition
        self.plural = plural


