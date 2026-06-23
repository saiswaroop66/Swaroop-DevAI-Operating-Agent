from utils.llm import ask_llm
import json


def extract_memory(user_message):

    prompt = f"""
    Extract personal facts from this message.

    Return ONLY JSON.

    Example:

    {{
        "name":"Swaroop",
        "favorite_language":"Python",
        "career_goal":"AI Engineer"
    }}

    Message:
    {user_message}

    If no facts exist return:
    {{}}
    """

    try:

        response = ask_llm(prompt)

        start = response.find("{")
        end = response.rfind("}") + 1

        json_text = response[start:end]

        return json.loads(json_text)

    except:
        return {}