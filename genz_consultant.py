import random #random module is used to select a random response from the list of responses
import time #time module is used to create a delay in the response, simulating the AI "thinking"

responses = [
    "Honestly? High-key yes.",
    "Low-key a bad idea, no cap.",
    "My neural networks are sensing big red flags",
    "It's a full-on vibe, go for it",
    "Error 404: Emotion not found. Try again later.",
    "Bet! The odds are definitely in your favor.",
    "That ain't it, chief."
] #possible responses the AI can give to user questions

def ask_ai():
    print("Welcome to Gen-Z AI Consultant!")
    
    while True:
        question = input("\nAsk me anything (or type 'exit' to quit): ")
        
        
        if question.lower().strip() == "exit": #condition to exit the loop if the user types 'exit'
            print("Bye bestie! Stay cool.")
            break
            
        print("Thinking", end="")
        for _ in range(3):
            time.sleep(0.5)
            print(".", end="") #creates an animated effect of the AI "thinking" by printing dots with a delay

        print("\n" + random.choice(responses))

if __name__ == "__main__":
    ask_ai()