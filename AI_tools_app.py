import streamlit as st
from PIL import Image

# Sample data structure for AI tools
AI_TOOLS = {
    "ChatGPT": {
        "description": "ChatGPT is an AI language model developed by OpenAI, capable of generating human-like text.",
        "link": "https://openai.com/chatgpt",
        "logo": "chatgpt_logo.png"
    },
    "DALL-E": {
        "description": "DALL-E is an AI model developed by OpenAI that generates images from text descriptions.",
        "link": "https://openai.com/dall-e",
        "logo": "dalle_logo.png"
    },
    # Add more tools as needed
}

# App title
st.title("AI Technology & Tools Information")

# Introduction
st.write("""
    Welcome to the AI Technology & Tools Information App!
    Use the search bar below to find information about various AI tools.
""")

# Search bar
search_query = st.text_input("Search for an AI tool...")

# Function to display tool information
def display_tool_info(tool_name, tool_info):
    st.subheader(tool_name)
    st.write(tool_info["description"])
    st.image(tool_info["logo"], width=100)
    st.markdown(f"[Learn more]({tool_info['link']})")

# Search logic
if search_query:
    search_query = search_query.lower()
    results = {name: info for name, info in AI_TOOLS.items() if search_query in name.lower()}
    if results:
        for name, info in results.items():
            display_tool_info(name, info)
    else:
        st.write("No matching tools found.")
else:
    st.write("Please enter a search query to find AI tools.")

# Optionally, display all tools
st.write("### All AI Tools")
for name, info in AI_TOOLS.items():
    display_tool_info(name, info)
