from agents.translator_agent_agno import TranslatorAgentAGNO

# Initialize the translator agent
agent = TranslatorAgentAGNO()

print("\n🔤 English ➡️ Nepali Translator (CLI)")
print("Type 'exit' to quit.\n")

# Simple list to store translation history
translation_history = []

while True:
    # Get English input from the user
    english = input("📝 Enter English sentence: ").strip()
    
    # Check for exit command
    if english.lower() == "exit":
        print("👋 Exiting...")
        break

    # Translate the English sentence to Nepali
    nepali = agent.run(english)
    print(f"✅ Nepali: {nepali}")

    # Store the translation in history
    translation_history.append((english, nepali))
    
    # Show recent translations instead of similar ones
    if translation_history:
        print("📚 Recent Translations:")
        # Show last 5 translations (excluding current one)
        for eng, nep in translation_history[-6:-1]:
            print(f" - {eng} → {nep}")
    
    print()