from tavily import TavilyClient
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()

# Local (.env) OR Streamlit Cloud (Secrets)
api_key = os.getenv("TAVILY_API_KEY")

if not api_key:
    api_key = st.secrets["TAVILY_API_KEY"]

client = TavilyClient(api_key=api_key)


def web_search(query):

    try:

        result = client.search(
            query=query,
            search_depth="basic",
            max_results=5
        )

        return str(result)

    except Exception as e:

        return f"❌ Search Error: {str(e)}"
