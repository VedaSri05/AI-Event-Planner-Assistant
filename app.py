from flask import Flask, request, jsonify
import spacy
import spacy.cli
import random
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)

# Load spaCy NLP model
spacy.cli.download("en_core_web_sm")
nlp = spacy.load("en_core_web_sm")

# Sample event data
event_data = {
    "wedding": [
        "Venue: Grand Palace Hall | Vendors: ABC Catering, XYZ Decorators | Budget: ₹5,00,000",
        "Venue: Royal Banquet | Vendors: Foodies Catering, Elegant Decor | Budget: ₹4,50,000"
    ],
    "corporate": [
        "Venue: Business Convention Center | Vendors: Pro Catering, Tech AV Solutions | Budget: ₹3,00,000",
        "Venue: Downtown Hotel | Vendors: Elite Catering, Sound Experts | Budget: ₹2,50,000"
    ],
    "birthday": [
        "Venue: City Clubhouse | Vendors: Party Delights Catering, Fun Decor | Budget: ₹1,00,000",
        "Venue: Family Garden | Vendors: Happy Catering, Balloon Masters | Budget: ₹80,000"
    ]
}

# TF-IDF Vectorizer for matching events
vectorizer = TfidfVectorizer()
event_types = list(event_data.keys())
vectorizer.fit(event_types)

@app.route("/")
def home():
    return "AI Event Planner Assistant is running with Local NLP!"

@app.route("/plan_event", methods=["POST"])
def plan_event():
    data = request.json
    user_input = data.get("event_type", "").lower()

    # Process input with spaCy NLP
    processed_text = " ".join([token.lemma_ for token in nlp(user_input) if not token.is_stop])

    # Match input to the closest event type using TF-IDF
    input_vector = vectorizer.transform([processed_text])
    event_scores = input_vector.dot(vectorizer.transform(event_types).T).toarray().flatten()
    best_match_index = event_scores.argmax()

    best_event = event_types[best_match_index]
    response = random.choice(event_data[best_event])

    return jsonify({"message": response})

if __name__ == "__main__":
    app.run(debug=True)
