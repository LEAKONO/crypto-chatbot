from data import crypto_db

class CryptoBuddy:
    def __init__(self):
        self.greeting = "Hey there! I'm CryptoBuddy! Let's find you a green and growing crypto! 🚀"
        self.disclaimer = "\n⚠️ Remember: Crypto is risky—always do your own research! ⚠️"
    
    def respond(self, user_query):
        user_query = user_query.lower()
        
        # Greeting responses
        if any(word in user_query for word in ["hi", "hello", "hey"]):
            return self.greeting + "\nHow can I help you today?"
        
        # Help command
        if "help" in user_query:
            return ("I can help with:\n"
                   "- Trending cryptos (ask about 'trending' or 'rising' coins)\n"
                   "- Sustainable investments (ask about 'eco-friendly' or 'sustainable' coins)\n"
                   "- Profit potential (ask about 'growth' or 'profit')\n"
                   "- Risk assessment (ask about 'safe' or 'low risk' options)")
        
        # Trending coins
        if "trend" in user_query or "rising" in user_query:
            coins = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising"]
            if coins:
                return f"These cryptos are trending up: {', '.join(coins)}! 📈"
            return "Currently no cryptocurrencies are trending upward."
        
        # Sustainable coins
        if any(word in user_query for word in ["sustain", "eco", "green", "environment"]):
            recommend = max(crypto_db.items(), key=lambda x: x[1]["sustainability_score"])
            return (f"For sustainability, I recommend {recommend[0]}! 🌱\n"
                   f"Sustainability score: {recommend[1]['sustainability_score']*10}/10\n"
                   f"Energy use: {recommend[1]['energy_use'].capitalize()}")
        
        # Profit potential
        if any(word in user_query for word in ["profit", "growth", "invest"]):
            profitable_coins = [
                coin for coin in crypto_db 
                if crypto_db[coin]["price_trend"] == "rising" 
                and crypto_db[coin]["market_cap"] in ["high", "medium"]
            ]
            if profitable_coins:
                return (f"For growth potential, consider: {', '.join(profitable_coins)} 💰\n"
                       "Remember: Higher potential often means higher risk!")
            return "No strong growth opportunities identified currently."
        
        # Low risk options
        if any(word in user_query for word in ["safe", "low risk", "conservative"]):
            safe_coins = [coin for coin in crypto_db if crypto_db[coin]["risk"] == "low"]
            if safe_coins:
                return f"Lower risk options: {', '.join(safe_coins)} 🛡️"
            return "All cryptocurrencies carry significant risk currently."
        
        # Specific coin queries
        for coin in crypto_db:
            if coin.lower() in user_query:
                info = crypto_db[coin]
                return (f"{coin} info:\n"
                       f"- Price trend: {info['price_trend'].capitalize()}\n"
                       f"- Market cap: {info['market_cap'].capitalize()}\n"
                       f"- Energy use: {info['energy_use'].capitalize()}\n"
                       f"- Sustainability: {info['sustainability_score']*10}/10\n"
                       f"- Risk level: {info['risk'].capitalize()}")
        
        # Default response
        return (f"I'm not sure I understand. Try asking about:\n"
               "- Trending cryptocurrencies\n"
               "- Sustainable crypto options\n"
               "- Profit potential\n"
               "- Risk levels\n"
               f"Or type 'help' for more options.{self.disclaimer}")

def main():
    bot = CryptoBuddy()
    print(bot.greeting + bot.disclaimer)
    print("Type 'help' for options or 'quit' to exit.")
    
    while True:
        try:
            user_input = input("\nYou: ").strip()
            if not user_input:
                continue
                
            if user_input.lower() in ["quit", "exit", "bye"]:
                print("CryptoBuddy: Happy investing! Come back anytime! 🚀")
                break
                
            response = bot.respond(user_input)
            print(f"CryptoBuddy: {response}")
            
        except KeyboardInterrupt:
            print("\nCryptoBuddy: Session ended. Goodbye!")
            break
        except Exception as e:
            print(f"CryptoBuddy: Oops! Something went wrong. Please try again. Error: {str(e)}")

if __name__ == "__main__":
    main()