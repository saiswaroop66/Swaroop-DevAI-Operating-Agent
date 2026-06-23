from utils.llm import ask_llm

def coding_agent(task):

    prompt = f"""
    You are a senior software engineer.

    {task}
    """

    return ask_llm(prompt)