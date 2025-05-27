import json
from model import generate_response

def demo_json_code_generation():
    code_spec = {
        'name': 'swap_keys_values',
        'description': 'Swaps the keys and values in a given dictionary.',
        'params': {
            'd': 'A dictionary with unique values.'
        },
    }

    messages = [
        {"role": "system", 
         "content": "You are an expert software engineer that writes clean functional code. You always document your functions."},
        {"role": "user", "content": f"Please implement: {json.dumps(code_spec, indent=2)}"}
    ]

    print("📤 Sending JSON specification to the language model...")
    response = generate_response(messages)
    print("🤖 LLM:", response)

def main():
   print("Choose an option:")
   print("1. Enter custom prompt")
   print("2. Demo JSON code generation")
   
   choice = input("Enter choice (1 or 2): ").strip()
   
   if choice == "2":
       demo_json_code_generation()
       return
       
   # Original functionality
   messages = [{"role": "system", "content": "You are a helpful assistant."}]
   
   while True:
       try:
           user_input = input("💬 Enter your prompt: ").strip()
           if not user_input:
               print("⚠️ No prompt entered. Exiting.")
               return

           messages.append({"role": "user", "content": user_input})

           print("📤 Sending prompt to the language model...")
           response = generate_response(messages)
           print("🤖 LLM:", response)
           
           messages.append({"role": "assistant", "content": response})

       except Exception as e:
           print("❌ An error occurred while generating the response:", e)

if __name__ == "__main__":
   main()