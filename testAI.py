import ollama

def primaryAIInput(prompt):
    response = ollama.chat(model='gemma:2b', messages=[
        {'role': 'user', 'content': prompt}
    ])
    print("Raw response:", response['message']['content'])  # Debug: Print raw response
    return str(response).strip()

primaryAIInput("hello")