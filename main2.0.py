import sys
import ollama
import subprocess

def primaryAIInput(prompt):
    response = ollama.chat(model='gemma:2b', messages=[
        {
            'role': 'user',
            'content': prompt + "###IMPORTANT - only write code. no other text should be included in your output###"
        },
    ])
    return str(response['message']['content']).strip()

def execute_script(file_name):
    try:
        result = subprocess.run(["python", file_name], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return e.stderr

def stripFirstAndLast(filePath):
        # Open the file for reading
    with open(filePath, 'r') as file:
        lines = file.readlines()

    # Remove the first and last lines
    new_lines = lines[1:-1]

    # Open the file again for writing (overwrite the original file)
    with open(filePath, 'w') as file:
        file.writelines(new_lines)
        
        


InitialPrompt = "Write a text-based game in the coding language python"
fileName = "generated_script.py"

# Generate and write initial AI code to file
with open(fileName, "w") as file:
    output = primaryAIInput(InitialPrompt)
    file.write(output)
    
stripFirstAndLast(fileName)


