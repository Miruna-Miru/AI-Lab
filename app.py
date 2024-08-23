from flask import Flask, render_template, request, jsonify
from nltk.chat.util import Chat, reflections

# an instance of Flask class is created (main application)
app = Flask(__name__)

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how are you today?"]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there"]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created by OpenAI."]
    ],
    [
        r"how are you ?",
        ["I'm doing good\nHow about you?"]
    ],
    [
        r"sorry (.*)",
        ["It's alright", "It's OK, never mind"]
    ],
    [
        r"I am fine",
        ["Great to hear that, How can I help you?"]
    ],
    [
        r"quit",
        ["Bye! Take care."]
    ]
]

chatbot = Chat(pairs, reflections)

#  @app.route("/"): Decorator that defines the route for the home page (/).
#  home(): Function that handles requests to the home page and returns the rendered index.html template.

@app.route("/")
def home():
    return render_template("index.html")


# route for getting POST responses from chatbot
@app.route("/get_response", methods=["POST"])
def get_response():
    user_message = request.json.get("message") #extract msg from JSON body
    response = chatbot.respond(user_message) # geenreate reply using chatbot response
    return jsonify({"response": response})  # converts response into JSON and send

if __name__ == "__main__":
    app.run(debug=True)
