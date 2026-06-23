from utils.llm import ask_llm

def report_agent(data):

    prompt = f"""
    Create a professional report.

    {data}
    """

    return ask_llm(prompt)