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

def getAIResponse(pastCode, prompt):
    response = ollama.chat(model='gemma:2b', messages=[
        {
            'role': 'user',
            'content': "Here is the past code you wrote and the output:\n" + pastCode + "\n\nPlease update your past code to be better at: " + prompt + "###IMPORTANT - only write code. no other text should be included in your output###"
        },
    ])
    return str(response['message']['content']).strip()

def execute_script(file_name):
    try:
        result = subprocess.run(["python", file_name], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return e.stderr

InitialPrompt = "Write a text-based game in the coding language python"
fileName = "generated_script.py"
history = ""

def stripFirstAndLast(filePath):
        # Open the file for reading
    with open(filePath, 'r') as file:
        lines = file.readlines()

    # Remove the first and last lines
    new_lines = lines[1:-1]

    # Open the file again for writing (overwrite the original file)
    with open(filePath, 'w') as file:
        file.writelines(new_lines)


# Generate and write initial AI code to file
with open(fileName, "w") as file:
    output = primaryAIInput(InitialPrompt)
    history += output
    file.write(output)

# Execute the generated Python file
codeOutput = execute_script(fileName)




# Clear the file contents for the next iteration
with open(fileName, "w") as file:
    pass

for i in range(5):
    # Generate updated code from AI based on history
    with open(fileName, "w") as file:
        output = getAIResponse(history, InitialPrompt)
        history += output
        file.write(output)
        
    print(output)
    
    # Execute the updated Python file
    codeOutput = execute_script(fileName)

    # Clear the file contents for the next iteration
    with open(fileName, "w") as file:
        pass

    # Optionally print or log the output for debugging
    print(codeOutput)
