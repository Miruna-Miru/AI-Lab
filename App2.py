from flask import Flask, render_template, request, jsonify
from nltk.chat.util import Chat, reflections
import json
import os

# Create an instance of the Flask class (main application)
app = Flask(__name__)

# Path to the knowledge base JSON file
KNOWLEDGE_BASE_FILE = "knowledge_base.json"

def load_knowledge_base():
    """Load the knowledge base from the JSON file."""
    if os.path.exists(KNOWLEDGE_BASE_FILE):
        with open(KNOWLEDGE_BASE_FILE, "r") as file:
            return json.load(file)
    else:
        return {"pairs": []}

def save_knowledge_base(knowledge_base):
    """Save the updated knowledge base to the JSON file."""
    with open(KNOWLEDGE_BASE_FILE, "w") as file:
        json.dump(knowledge_base, file, indent=4)

# Load the initial knowledge base
knowledge_base = load_knowledge_base()

def create_chatbot():
    """Create a new chatbot instance with the current knowledge base."""
    pairs = [(entry["pattern"], entry["responses"]) for entry in knowledge_base["pairs"]]
    return Chat(pairs, reflections)

# Initialize chatbot
chatbot = create_chatbot()

@app.route("/")
def home():
    """Home page route. Returns the rendered index.html template."""
    return render_template("new_index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    """Route for getting POST responses from the chatbot."""
    global chatbot  # Declare global variable here

    try:
        user_message = request.json.get("message")

        if user_message:
            response = chatbot.respond(user_message)
            
            if response:
                return jsonify({"response": response})
            else:
                # Check if the user input is already in the knowledge base
                existing_entry = next((entry for entry in knowledge_base["pairs"] if entry["pattern"] == user_message), None)
                
                if not existing_entry:
                    # Add new user input to the knowledge base if not recognized
                    new_entry = {
                        "pattern": user_message,
                        "responses": ["I don't understand that yet. Can you tell me more?"]
                    }
                    knowledge_base["pairs"].append(new_entry)
                    save_knowledge_base(knowledge_base)

                    # Reload the chatbot with the updated knowledge base
                    chatbot = create_chatbot()  # Update chatbot instance

                return jsonify({"response": "I don't understand that yet. Can you tell me more?"})
        else:
            return jsonify({"response": "No message received."})
    except Exception as e:
        return jsonify({"response": "An error occurred. Please try again."})

if __name__ == "__main__":
    # Run the Flask application in debug mode
    app.run(debug=True)
