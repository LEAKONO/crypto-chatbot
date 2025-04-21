from data import crypto_db

class CryptoBuddy:
    def __init__(self):
        self.greeting = "Hey there! I'm CryptoBuddy! Let's find you a green and growing crypto! 🚀"
        self.disclaimer = "\n⚠️ Remember: Crypto is risky—always do your own research! ⚠️"
    
    def respond(self, user_query):
        user_query = user_query.lower()
        
        if any(word in user_query for word in ["hi", "hello", "hey"]):
            return self.greeting + "\nHow can I help you today?"
        
        if "trend" in user_query or "rising" in user_query:
            coins = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising"]
            return f"These cryptos are trending up: {', '.join(coins)}! 📈"
        
        # ... rest of your chatbot logic

def main():
    bot = CryptoBuddy()
    print(bot.greeting + bot.disclaimer)
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("CryptoBuddy: Happy investing! Come back anytime! 🚀")
            break
        response = bot.respond(user_input)
        print(f"CryptoBuddy: {response}")

if __name__ == "__main__":
    main()