import streamlit as st

from agents.planner import planner
from agents.supervisor import supervisor
from agents.memory_agent import get_all_memory

# ----------------------------
# PAGE CONFIG
# ----------------------------

st.set_page_config(
    page_title="🤖 Swaroop DevAI Operating Agent",
    page_icon="🤖",
    layout="wide"
)

# ----------------------------
# SESSION STATE
# ----------------------------

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ----------------------------
# TITLE
# ----------------------------

st.title("🤖 Swaroop DevAI Operating Agent")

st.markdown(
    """
    Your personal AI Operating System with:
    
    - 🧠 Smart Memory
    - 🌐 Web Search
    - 💻 Coding Assistant
    - 🎨 Image Generation
    - 📋 Task Planning
    """
)

# ----------------------------
# SIDEBAR
# ----------------------------

with st.sidebar:

    st.header("🧠 Memory")

    memory = get_all_memory()

    if memory:
        st.json(memory)
    else:
        st.info("No memory stored yet.")

    st.divider()

    st.header("💬 Chat History")

    if st.session_state.chat_history:

        for chat in reversed(st.session_state.chat_history[-10:]):

            st.markdown(
                f"""
                **👤 User**
                
                {chat["user"]}
                
                ---
                """
            )

    else:
        st.info("No chats yet.")

    st.divider()

    if st.button("🗑 Clear History"):

        st.session_state.chat_history = []

        st.rerun()

# ----------------------------
# USER INPUT
# ----------------------------

task = st.text_area(
    "Enter your task",
    height=150,
    placeholder="Ask anything..."
)

# ----------------------------
# RUN AGENT
# ----------------------------

if st.button("🚀 Run Agent"):

    if not task.strip():

        st.warning("Please enter a task.")

    else:

        # Save user query

        st.session_state.chat_history.append(
            {
                "user": task
            }
        )

        # Planner

        with st.spinner("📋 Planning..."):

            plan = planner(task)

        st.subheader("📋 Plan")

        st.write(plan)

        # Supervisor

        with st.spinner("⚡ Executing..."):

            result = supervisor(task)

        st.subheader("✅ Result")

        # Image result

        if isinstance(result, str) and result.endswith(".png"):

            st.image(
                result,
                use_container_width=True
            )

        else:

            st.write(result)