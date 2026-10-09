import random
import time

responses = [
    "Honestly? High-key yes.",
    "Low-key a bad idea, no cap.",
    "My neural networks are sensing big red flags",
    "It's a full-on vibe, go for it",
    "Error 404: Emotion not found. Try again later.",
    "Bet! The odds are definitely in your favor.",
    "That ain't it, chief."
]

def ask_ai():
    print("Welcome to Gen-Z AI Consultant!")
    
    while True:
        question = input("\nAsk me anything (or type 'exit' to quit): ")
        
        
        if question.lower().strip() == "exit":
            print("Bye bestie! Stay cool.")
            break
            
        print("Thinking", end="")
        for _ in range(3):
            time.sleep(0.5)
            print(".", end="", flush=True)
            
        print("\n" + random.choice(responses))

if __name__ == "__main__":
    ask_ai()