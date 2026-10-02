# Recursive AI Coder

An agent that writes a script, runs it, reads the result, and iterates — a small
self-improving code-generation loop built on a local LLM via [Ollama](https://ollama.ai).

## How it works
`main.py` prompts the model for code, executes it with `subprocess`, feeds errors/output back,
and repeats until the task succeeds (or a limit is hit). `generated_script.py` is a sample
output.

## Run it
```bash
# requires Ollama running locally with a model pulled, e.g.:
ollama pull gemma:2b
python -m pip install ollama
python main.py
```
