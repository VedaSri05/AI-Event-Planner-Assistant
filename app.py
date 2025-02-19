from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import spacy
import spacy.util
import spacy.cli
import random
from sklearn.feature_extraction.text import TfidfVectorizer
import logging

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests

# Logging for debugging
logging.basicConfig(level=logging.DEBUG)

# Check if spaCy model is installed
if not spacy.util.is_package("en_core_web_sm"):
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

# TF-IDF Vectorizer for event matching
vectorizer = TfidfVectorizer()
event_types = list(event_data.keys())
vectorizer.fit(event_types)

@app.route("/")
def home():
    return "AI Event Planner Assistant is running with Local NLP!"

@app.route("/plan_event", methods=["POST"])
def plan_event():
    try:
        # Ensure JSON format
        if request.content_type != "application/json":
            return jsonify({"error": "Content-Type must be application/json"}), 415

        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON format"}), 400

        user_input = data.get("event_type", "").strip().lower()

        if not user_input:
            return jsonify({"error": "Event type is required"}), 400

        # Process NLP
        processed_text = " ".join([token.lemma_ for token in nlp(user_input) if not token.is_stop])
        input_vector = vectorizer.transform([processed_text])
        event_scores = input_vector.dot(vectorizer.transform(event_types).T).toarray().flatten()
        best_match_index = event_scores.argmax()

        best_event = event_types[best_match_index]
        response = random.choice(event_data[best_event])

        return jsonify({"message": response})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use dynamic port for deployment
    app.run(host="0.0.0.0", port=port)
