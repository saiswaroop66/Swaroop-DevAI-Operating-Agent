from agents.browser_agent import browser_agent
from agents.coding_agent import coding_agent
from agents.image_agent import image_agent

from agents.memory_agent import (
    add_fact,
    get_fact,
    get_all_memory
)

from agents.smart_memory import extract_memory


def supervisor(task):

    task_lower = task.lower()

    # --------------------
    # SMART MEMORY SAVE
    # --------------------

    facts = extract_memory(task)

    if facts:

        for k, v in facts.items():
            add_fact(k, v)

    # --------------------
    # MEMORY QUERIES
    # --------------------

    if "show my memory" in task_lower:

        memory = get_all_memory()

        if memory:
            return memory

        return "Memory is empty."

    elif "what do you know about me" in task_lower:

        memory = get_all_memory()

        if memory:
            return memory

        return "I don't know much about you yet."

    elif "what is my name" in task_lower:

        name = get_fact("name")

        if name:
            return f"Your name is {name}"

        return "I don't know your name yet."

    elif "what is my favorite language" in task_lower:

        lang = get_fact("favorite_language")

        if lang:
            return f"Your favorite language is {lang}"

        return "I don't know your favorite language yet."

    # --------------------
    # IMAGE AGENT
    # --------------------

    elif any(word in task_lower for word in [
        "image",
        "draw",
        "picture",
        "poster",
        "logo",
        "art",
        "generate image"
    ]):

        return image_agent(task)

    # --------------------
    # BROWSER AGENT
    # --------------------

    elif any(word in task_lower for word in [
        "search",
        "latest",
        "news",
        "find"
    ]):

        return browser_agent(task)

    # --------------------
    # CODING AGENT
    # --------------------

    elif any(word in task_lower for word in [
        "code",
        "python",
        "bug",
        "program",
        "streamlit"
    ]):

        return coding_agent(task)

    # --------------------
    # DEFAULT AGENT
    # --------------------

    else:

        return coding_agent(task)