
from nltk.chat.util import Chat, reflections

# Pairs is a list of patterns and responses.
pairs = [
    [
        #r    ---> regular expression
        # %1  ---> replaces with input word
        #  .  ---> Accept any single char except newline character
        #  *  ---> Accept 0 or more of preceeding element
        r"my name is (.*)",
        ["Hello %1, how are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created by OpenAI.",]
    ],
    [
        r"how are you ?",
        ["I'm doing good\nHow about you?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"I am fine",
        ["Great to hear that, How can I help you?",]
    ],
    [
        r"quit",
        ["Bye! Take care.",]
    ],
]

# Create a chatbot using the pairs and reflections
chatbot = Chat(pairs, reflections)

# Start the conversation
def chatbot_conversation():
    print("Hi, I'm the chatbot created by OpenAI. Talk to me!")
    chatbot.converse()

if __name__ == "__main__":
    chatbot_conversation()
