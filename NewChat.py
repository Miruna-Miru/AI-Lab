from transformers import AutoTokenizer, AutoModelForCausalLM

# Load the GPT-Neo model and tokenizer
def load_chatbot():
    print("Loading chatbot model... (this may take a moment)")
    model_name = "EleutherAI/gpt-neo-1.3B"  # You can change this to "EleutherAI/gpt-j-6B" for a larger model
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    print("Chatbot is ready!")
    return tokenizer, model

# Function to chat with the chatbot
def chat_with_bot(tokenizer, model):
    print("Chatbot: Hi! I’m your AI chatbot. Ask me anything! Type 'bye' to exit.")
    chat_history = ""

    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        # Encode user input and append to chat history
        inputs = tokenizer.encode(chat_history + tokenizer.eos_token + user_input + tokenizer.eos_token, return_tensors="pt")
        
        # Generate a response
        outputs = model.generate(inputs, max_length=150, pad_token_id=tokenizer.eos_token_id)
        response = tokenizer.decode(outputs[:, inputs.shape[-1]:][0], skip_special_tokens=True)
        
        print(f"Chatbot: {response}")
        
        # Update the chat history
        chat_history += user_input + tokenizer.eos_token + response + tokenizer.eos_token

# Main function to load and run the chatbot
if __name__ == "__main__":
    tokenizer, model = load_chatbot()
    chat_with_bot(tokenizer, model)
