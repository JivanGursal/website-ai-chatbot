import subprocess

def ask_llm(system_prompt: str, user_message: str) -> str:
    prompt = f"""
{system_prompt}

User: {user_message}
Assistant:
"""

    result = subprocess.run(
        ["ollama", "run", "qwen2.5:0.5b"],
        input=prompt,
        text=True,
        capture_output=True
    )

    if result.returncode != 0:
        return "AI is busy. Please try again."

    return result.stdout.strip()
