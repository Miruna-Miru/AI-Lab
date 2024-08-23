import random as ran

# Define response categories
responses = {
    "Greetings": [
        "Hello {name}! How are you doing today?", 
        "Hi {name}! What can I do for you?", 
        "Hey {name}! How's your day going?"
    ],
    "End": [
        "Goodbye {name}! See you later!",
        "Bye {name}! Have a great day!",
        "Wishing you a fantastic day ahead, {name}!"
    ],
    "Reply": [
        "I'm glad I could help, {name}!",
        "You're welcome, {name}! Feel free to ask more."
    ],
    "Climate": [
        "I can't check the weather right now, {name}. Maybe try a weather app!",
        "Sorry {name}, I don't have weather updates. Please check online."
    ],
    "Help": [
        "Sure, {name}! What do you need help with?",
        "I'm here to help, {name}. Could you explain it again?"
    ],
    "Sad": [
        "Oh, {name}, I hope things get better soon.",
        "Don't worry, {name}. Things will improve with time.",
        "Stay positive, {name}. Good things are on their way!"
    ],
    "Jokes": [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the math book look sad? Because it had too many problems.",
        "What do you call fake spaghetti? An impasta!"
    ],
    "Fun Facts": [
        "Did you know? Honey never spoils.",
        "Fun fact: A group of flamingos is called a 'flamboyance.'",
        "Here's a fun fact: Octopuses have three hearts."
    ],
    "Default": [
        "Sorry, {name}, I didn't understand that.",
        "I'm not sure how to respond to that, {name}. Can you ask something else?",
        "I'm still learning, {name}. I'll try to get better at this!"
    ]
}

def get_response(usr_input, name, preferences, context):
    usr_input = usr_input.lower()
    context.append(usr_input)
    
    if len(context) > 3:  # Keep last 3 interactions for context
        context.pop(0)
    
    if any(word in usr_input for word in ["hi", "hello", "hey"]):
        return ran.choice(responses["Greetings"]).format(name=name)
    elif any(word in usr_input for word in ["bye", "goodbye", "see you later"]):
        return ran.choice(responses["End"]).format(name=name)
    elif any(word in usr_input for word in ["thank you", "thanks", "great", "tq"]):
        return ran.choice(responses["Reply"]).format(name=name)
    elif any(word in usr_input for word in ["help", "please", "will you", "plz"]):
        return ran.choice(responses["Help"]).format(name=name)
    elif any(word in usr_input for word in ["climate", "weather", "temperature"]):
        return ran.choice(responses["Climate"]).format(name=name)
    elif any(word in usr_input for word in ["not good", "tired", "i'm down", "bad"]):
        return ran.choice(responses["Sad"]).format(name=name)
    elif "joke" in usr_input:
        return ran.choice(responses["Jokes"]).format(name=name)
    elif "fun fact" in usr_input:
        return ran.choice(responses["Fun Facts"]).format(name=name)
    elif "preference" in usr_input:
        if "set" in usr_input:
            pref = usr_input.split("set")[1].strip()
            preferences.append(pref)
            return f"Preference '{pref}' has been set, {name}!"
        elif "show" in usr_input:
            if preferences:
                return f"Your current preferences are: {', '.join(preferences)}, {name}!"
            else:
                return "You have no set preferences yet."
        elif "clear" in usr_input:
            preferences.clear()
            return f"All preferences have been cleared, {name}!"
    elif "history" in usr_input:
        return "Conversation history:\n" + "\n".join(context)
    else:
        return ran.choice(responses["Default"]).format(name=name)

def chat_with_me(name):
    preferences = []
    context = []
    print(f"Hello {name}! I'm Chatty. Let's chat!")

    while True:
        usr_input = input(f"{name} : ").strip()
        res = get_response(usr_input, name, preferences, context)
        print(f"Chatty : {res}")

        if any(word in res for word in ["Goodbye", "See you later", "Have a great day"]):
            break


print("Hey there!!👋 I'm Chatty, your friendly chatbot 🤖")
usr_name = input("What's your sweet name 😍 : ")
chat_with_me(usr_name)
