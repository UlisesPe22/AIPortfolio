from models import Nouns, Adjectives, Verbs
nouns_data = [
    Nouns(
        word="Haus",
        plural="Häuser",
        gender="N",
        sentence="Das Haus ist groß.",
        definition="A building for human habitation"
    ),
    Nouns(
        word="Stadt",
        plural="Städte",
        gender="F",
        sentence="Die Stadt ist belebt.",
        definition="A large town."
    ),
    Nouns(
        word="Tier",
        plural="Tiere",
        gender="N",
        sentence="Das Tier ist sehr niedlich.",
        definition="A living organism that feeds on organic matter"
    ),
    Nouns(
        word="Rucksack",
        plural="Rucksäcke",
        gender="M",
        sentence="Ich nehme meinen Ruchsack zum Camp",
        definition="Backpack"
    ),
    Nouns(
        word="Hund",
        plural="Hunde",
        gender="M",
        sentence="Der Hund ist treu.",
        definition="Dog" 
    )
]
adjectives_data = [
    Adjectives(
        word="groß",
        sentence="Das Haus ist groß.",
        definition="Large in size.",
        plural="w"
    ),
    Adjectives(
        word="belebt",
        sentence="Die Stadt ist belebt.",
        definition="Full of activity.",
        plural="w"
    ),
    Adjectives(
        word="niedlich",
        sentence="Das Tier ist sehr niedlich.",
        definition="Cute and charming.",
        plural="w"
    ),
    Adjectives(
    word="klein",
    sentence="Die Blume ist klein.",
    definition="Small in size.",
    plural="w"
    ),
    Adjectives(
        word="schnell",
        sentence="Der Zug ist schnell.",
        definition="Fast in speed.",
        plural="w"
    )
]
verbs_data = [
    Verbs(
        word="laufen",
        sentence="Ich laufe schnell.",
        definition="To run quickly.",
        past="gelaufen"
    ),
    Verbs(
        word="sprechen",
        sentence="Wir sprechen Deutsch.",
        definition="To speak German.",
        past="gesprochen"
    ),
    Verbs(
        word="essen",
        sentence="Sie essen Abendessen.",
        definition="To eat dinner.",
        past="gegessen"
    ),
    Verbs(
    word="trinken",
    sentence="Ich trinke Kaffee.",
    definition="To drink coffee.",
    past="getrunken"
    ),
    Verbs(
    word="schlafen",
    sentence="Ich schlafe gut.",
    definition="To sleep",
    past="geschlafen"
    )
]
