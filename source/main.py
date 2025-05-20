from model import generate_response

def main():
    try:
        user_input = input("💬 Enter your prompt: ").strip()
        if not user_input:
            print("⚠️ No prompt entered. Exiting.")
            return

        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ]

        print("📤 Sending prompt to the language model...")
        response = generate_response(messages)
        print("🤖 LLM:", response)

    except Exception as e:
        print("❌ An error occurred while generating the response:", e)

if __name__ == "__main__":
    main()