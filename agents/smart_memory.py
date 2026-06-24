import re

def extract_memory(user_message):

    facts = {}

    text = user_message.lower()

    # Name

    match = re.search(
        r"my name is\s+(.+)",
        text
    )

    if match:
        facts["name"] = match.group(1).strip().title()

    # Favorite Language

    match = re.search(
        r"my favorite language is\s+(.+)",
        text
    )

    if match:
        facts["favorite_language"] = (
            match.group(1).strip().title()
        )

    # Career Goal

    match = re.search(
        r"my career goal is\s+(.+)",
        text
    )

    if match:
        facts["career_goal"] = (
            match.group(1).strip().title()
        )

    return facts
