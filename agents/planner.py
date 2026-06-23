from utils.llm import ask_llm

def planner(task):

    prompt = f"""
    Break this task into steps:

    {task}
    """

    return ask_llm(prompt)